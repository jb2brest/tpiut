"""
Système d'édition de ticket de caisse.

Usage :
    python3 main.py "<magasin>" "<vendeur>" "<CODE:QTE|CODE:QTE|...>"

Exemple :
    python3 main.py "BUT Market" "Lisa" "C01:1|C02:3|C03:4"
"""

import csv
import os
import sys
from datetime import date
from decimal import Decimal, ROUND_HALF_UP

# Dossier du script : les fichiers de données sont cherchés à côté de main.py
DOSSIER = os.path.dirname(os.path.abspath(__file__))
FICHIER_PRODUITS = os.path.join(DOSSIER, "produits.csv")
FICHIER_COMPTEUR = os.path.join(DOSSIER, "compteur.txt")
PREMIER_NUMERO = 2200


class ErreurTicket(Exception):
    """Erreur fonctionnelle (code inconnu, quantité invalide...)."""


def charger_produits(chemin=FICHIER_PRODUITS):
    """Lit le catalogue CSV et renvoie un dict {code: {description, prix_ht, tva}}."""
    produits = {}
    with open(chemin, encoding="utf-8") as f:
        for ligne in csv.DictReader(f, delimiter=";"):
            code = ligne["code"].strip().upper()
            produits[code] = {
                "description": ligne["description"].strip(),
                # Decimal évite les erreurs d'arrondi des float (ex: 0.1 + 0.2)
                "prix_ht": Decimal(ligne["prix_ht"].strip().replace(",", ".")),
                "tva": Decimal(ligne["tva"].strip().replace(",", ".")),
            }
    return produits


def parser_panier(texte):
    """Transforme "C01:10|C02:2" en liste [("C01", 10), ("C02", 2)]."""
    panier = []
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
        panier.append((code, qte))
    if not panier:
        raise ErreurTicket("Le panier est vide")
    return panier


def calculer_lignes(panier, produits):
    """Calcule le détail de chaque ligne du ticket (HT, TVA, TTC)."""
    lignes = []
    for code, qte in panier:
        if code not in produits:
            raise ErreurTicket(f"Code article inconnu : {code}")
        p = produits[code]
        total_ht = p["prix_ht"] * qte
        montant_tva = total_ht * p["tva"] / 100
        lignes.append({
            "nb": qte,
            "description": p["description"],
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


def euro(montant):
    """Formate un montant à la française : 5 -> '5€', 5.5 -> '5,5€', 1.25 -> '1,25€'."""
    montant = Decimal(montant).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    texte = f"{montant:.2f}".rstrip("0").rstrip(".")
    return texte.replace(".", ",") + "€"


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
        f"{'NB':<6}{'Desc.':<20}{'HT unitaire':<14}{'TVA':<7}Total",
    ]
    for l in lignes:
        sortie.append(
            f"{l['nb']:<6}{l['description']:<20}{euro(l['prix_ht']):<14}"
            f"{pourcent(l['tva']):<7}{euro(l['total_ttc'])}"
        )
    sortie += [
        "",
        f"{'':<33}{'Total HT':<14}{euro(total_ht)}",
        f"{'':<33}{'Total TVA':<14}{euro(total_tva)}",
        f"{'':<33}{'Total':<14}{euro(total_ttc)}",
    ]
    return "\n".join(sortie)


def main(argv):
    if len(argv) != 4:
        print(__doc__.strip())
        return 1
    magasin, vendeur, panier_texte = argv[1], argv[2], argv[3]
    try:
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
