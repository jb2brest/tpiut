"""
Système d'édition de ticket de caisse.

Usage :
    python3 main.py "<magasin>" "<vendeur>" "<CODE:QTE|CODE:QTE|...>"

Exemple :
    python3 main.py "BUT Market" "Lisa" "C01:1|C02:3|C03:4"
"""

import csv
import os
import re
import sys
from datetime import date
from decimal import Decimal, ROUND_HALF_UP

# Dossier du script : les fichiers de données sont cherchés à côté de main.py
DOSSIER = os.path.dirname(os.path.abspath(__file__))
FICHIER_PRODUITS = os.path.join(DOSSIER, "produits.csv")
FICHIER_COMPTEUR = os.path.join(DOSSIER, "compteur.txt")
PREMIER_NUMERO = 2200

# Unités de poids/volume acceptées -> (unité de base, coefficient)
# Les poids sont ramenés en grammes, les volumes en millilitres
UNITES = {
    "g": ("g", 1), "kg": ("g", 1000),
    "ml": ("ml", 1), "cl": ("ml", 10), "l": ("ml", 1000),
}


class ErreurTicket(Exception):
    """Erreur fonctionnelle (code inconnu, quantité invalide...)."""


def lire_poids_volume(texte):
    """Convertit "950g" / "2kg" / "1,5L" en (valeur en unité de base, unité de base)."""
    m = re.fullmatch(r"\s*(\d+(?:[.,]\d+)?)\s*([a-zA-Z]+)\s*", texte)
    if not m or m.group(2).lower() not in UNITES:
        raise ErreurTicket(f"Poids/volume invalide : '{texte}' (ex: 950g, 2kg, 1,5L)")
    base, coef = UNITES[m.group(2).lower()]
    return Decimal(m.group(1).replace(",", ".")) * coef, base


def charger_produits(chemin=FICHIER_PRODUITS):
    """Lit le catalogue CSV et renvoie un dict {code: {description, poids, prix_ht, tva, origine}}."""
    produits = {}
    with open(chemin, encoding="utf-8") as f:
        for ligne in csv.DictReader(f, delimiter=";"):
            code = ligne["code"].strip().upper()
            produits[code] = {
                "description": ligne["description"].strip(),
                "poids_volume": ligne["poids_volume"].strip(),
                # Decimal évite les erreurs d'arrondi des float (ex: 0.1 + 0.2)
                "prix_ht": Decimal(ligne["prix_ht"].strip().replace(",", ".")),
                "tva": Decimal(ligne["tva"].strip().replace(",", ".")),
                # Origine stockée pour une évolution future (pas affichée en binôme)
                "origine": (ligne.get("origine") or "").strip(),
            }
    return produits


def parser_panier(texte):
    """Transforme "C01:10|C02:2" en liste [("C01", 10), ("C02", 2)].
    Un même code saisi plusieurs fois est regroupé sur une seule ligne."""
    panier = {}  # dict : garde l'ordre de saisie et cumule les quantités
    for element in texte.split("|"):
        element = element.strip()
        if not element:
            continue
        if ":" not in element:
            raise ErreurTicket(f"Format invalide '{element}' (attendu CODE:QUANTITE)")
        code, qte = element.split(":", 1)
        code = code.strip().upper()
        try:
            qte = int(qte)
        except ValueError:
            raise ErreurTicket(f"Quantité invalide pour {code} : '{qte}'")
        if qte <= 0:
            raise ErreurTicket(f"La quantité de {code} doit être positive")
        panier[code] = panier.get(code, 0) + qte
    if not panier:
        raise ErreurTicket("Le panier est vide")
    return list(panier.items())


def calculer_lignes(panier, produits):
    """Calcule le détail de chaque ligne du ticket (HT, TVA, TTC)."""
    lignes = []
    for code, qte in panier:
        if code not in produits:
            raise ErreurTicket(f"Code article inconnu : {code}")
        p = produits[code]
        total_ht = p["prix_ht"] * qte
        montant_tva = total_ht * p["tva"] / 100
        valeur, unite = lire_poids_volume(p["poids_volume"])
        lignes.append({
            "nb": qte,
            "description": p["description"],
            "poids_unitaire": p["poids_volume"],
            "poids_total": poids_volume(valeur * qte, unite),
            "prix_ht": p["prix_ht"],
            "tva": p["tva"],
            "total_ht": total_ht,
            "montant_tva": montant_tva,
            "total_ttc": total_ht + montant_tva,
        })
    return lignes


def calculer_totaux(lignes):
    """Renvoie (total HT, total TVA, total TTC) du ticket."""
    total_ht = sum((l["total_ht"] for l in lignes), Decimal(0))
    total_tva = sum((l["montant_tva"] for l in lignes), Decimal(0))
    return total_ht, total_tva, total_ht + total_tva


def nombre(valeur, decimales=2):
    """Formate un nombre à la française sans zéros inutiles : 5.50 -> '5,5', 16.00 -> '16'."""
    valeur = Decimal(valeur).quantize(Decimal(1).scaleb(-decimales), rounding=ROUND_HALF_UP)
    texte = f"{valeur:.{decimales}f}"
    if "." in texte:
        texte = texte.rstrip("0").rstrip(".")
    return texte.replace(".", ",")


def euro(montant):
    """Formate un montant à la française : 5 -> '5€', 5.5 -> '5,5€', 1.25 -> '1,25€'."""
    return nombre(montant) + "€"


def poids_volume(valeur, unite):
    """Affiche un poids (g) ou un volume (ml) dans l'unité la plus lisible : 3800g -> '3,8kg'."""
    if unite == "g":
        return nombre(valeur / 1000, 3) + "kg" if valeur >= 1000 else nombre(valeur) + "g"
    return nombre(valeur / 1000, 3) + "L" if valeur >= 1000 else nombre(valeur) + "mL"


def pourcent(taux):
    """Formate un taux de TVA : 10 -> '10%', 5.5 -> '5,5%'."""
    texte = f"{Decimal(taux):f}"
    if "." in texte:
        texte = texte.rstrip("0").rstrip(".")
    return texte.replace(".", ",") + "%"


def prochain_numero(chemin=FICHIER_COMPTEUR):
    """Lit le dernier numéro de ticket, l'incrémente et le sauvegarde."""
    numero = PREMIER_NUMERO
    if os.path.exists(chemin):
        with open(chemin, encoding="utf-8") as f:
            numero = int(f.read().strip()) + 1
    with open(chemin, "w", encoding="utf-8") as f:
        f.write(str(numero))
    return numero


def generer_ticket(magasin, vendeur, numero, jour, lignes):
    """Construit le texte du ticket au format demandé par le client."""
    total_ht, total_tva, total_ttc = calculer_totaux(lignes)
    sortie = [
        magasin,
        f"Ticket numéro : {numero}",
        "",
        f"Date : {jour.strftime('%d/%m/%Y')}",
        "",
        f"Vous avez été servi par : {vendeur}",
        "",
    ]
    # Tableau : chaque colonne s'adapte à son contenu le plus long
    entete = ["NB", "Desc.", "Poids/volume unitaire", "Poids/volume total",
              "HT unitaire", "TVA", "Total"]
    tableau = [
        [str(l["nb"]), l["description"], l["poids_unitaire"], l["poids_total"],
         euro(l["prix_ht"]), pourcent(l["tva"]), euro(l["total_ttc"])]
        for l in lignes
    ]
    nb_col = len(entete)
    largeurs = [max(len(ligne[i]) for ligne in [entete] + tableau) + 3 for i in range(nb_col - 1)]
    for ligne in [entete] + tableau:
        sortie.append("".join(c.ljust(w) for c, w in zip(ligne, largeurs)) + ligne[-1])
    # Totaux : libellé sous "HT unitaire", montant aligné sur la colonne "Total"
    marge = " " * sum(largeurs[:4])
    largeur_libelle = largeurs[4] + largeurs[5]
    sortie.append("")
    for libelle, montant in (("Total HT", total_ht), ("Total TVA", total_tva), ("Total", total_ttc)):
        sortie.append(marge + libelle.ljust(largeur_libelle) + euro(montant))
    return "\n".join(sortie)


def main(argv):
    if len(argv) != 4:
        print(__doc__.strip())
        return 1
    magasin, vendeur, panier_texte = argv[1].strip(), argv[2].strip(), argv[3]
    try:
        if not magasin or not vendeur:
            raise ErreurTicket("Le nom du magasin et du vendeur sont obligatoires")
        produits = charger_produits()
        lignes = calculer_lignes(parser_panier(panier_texte), produits)
    except ErreurTicket as e:
        print(f"Erreur : {e}")
        return 2
    except FileNotFoundError:
        print(f"Erreur : catalogue introuvable ({FICHIER_PRODUITS})")
        return 2
    # Le numéro n'est consommé que si le ticket est valide
    print(generer_ticket(magasin, vendeur, prochain_numero(), date.today(), lignes))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
