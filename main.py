"""Générateur de tickets de caisse.
SALAUN - DUCAUD

   test de l'exo:  python3 main.py "BUT Market" "Lisa" "C01:1|C02:3|C03:4"
"""

import json
import sys
from datetime import date
from pathlib import Path

DOSSIER = Path(__file__).parent
FICHIER_ARTICLES = DOSSIER / "articles.json"
FICHIER_NUMERO = DOSSIER / "dernier_ticket.txt"
TAUX_TVA = 0.10
NUMERO_DEPART = 2200


# ---------- Données ----------

def charger_articles(chemin=FICHIER_ARTICLES):
    """Charge la liste des articles depuis le fichier JSON."""
    with open(chemin, encoding="utf-8") as f:
        return json.load(f)


def prochain_numero_ticket(chemin=FICHIER_NUMERO):
    """Renvoie le numéro du nouveau ticket et le sauvegarde."""
    if chemin.exists():
        numero = int(chemin.read_text().strip()) + 1
    else:
        numero = NUMERO_DEPART
    chemin.write_text(str(numero))
    return numero


# ---------- Parsing du panier ----------

def parser_panier(texte, articles):
    """Transforme "C01:10|C02:2" en [("C01", 10), ("C02", 2)]."""
    panier = []
    for element in texte.split("|"):
        try:
            code, quantite = element.split(":")
            code = code.strip().upper()
            quantite = int(quantite)
        except ValueError:
            raise ValueError(f"Élément de panier invalide : '{element}' (format attendu CODE:QUANTITE)")
        if code not in articles:
            raise ValueError(f"Code article inconnu : '{code}'")
        if quantite <= 0:
            raise ValueError(f"Quantité invalide pour {code} : {quantite}")
        panier.append((code, quantite))
    return panier


# ---------- Calculs ----------

def calculer_lignes(panier, articles):
    """Calcule le détail de chaque ligne du ticket."""
    lignes = []
    for code, quantite in panier:
        article = articles[code]
        total_ht = quantite * article["prix_ht_unitaire"]
        lignes.append({
            "quantite": quantite,
            "description": article["description"],
            "prix_ht_unitaire": article["prix_ht_unitaire"],
            "total_ht": total_ht,
            "total_ttc": total_ht * (1 + TAUX_TVA),
        })
    return lignes


def calculer_totaux(lignes):
    total_ht = sum(l["total_ht"] for l in lignes)
    total_tva = total_ht * TAUX_TVA
    return total_ht, total_tva, total_ht + total_tva


# ---------- Affichage ----------

def euros(montant):
    """Formate 5.5 en '5,5€' et 16.0 en '16€'."""
    texte = f"{round(montant, 2):.2f}".rstrip("0").rstrip(".")
    return texte.replace(".", ",") + "€"


def generer_ticket(magasin, vendeur, numero, lignes):
    total_ht, total_tva, total_ttc = calculer_totaux(lignes)
    tva = f"{int(TAUX_TVA * 100)}%"

    sortie = [
        magasin,
        f"Ticket numéro : {numero}",
        "",
        f"Date : {date.today():%d/%m/%Y}",
        "",
        f"Vous avez été servi par : {vendeur}",
        "",
        f"{'NB':<4}{'Desc.':<18}{'HT unitaire':<14}{'TVA':<6}{'Total':>8}",
    ]
    for l in lignes:
        sortie.append(
            f"{l['quantite']:<4}{l['description']:<18}{euros(l['prix_ht_unitaire']):<14}"
            f"{tva:<6}{euros(l['total_ttc']):>8}"
        )
    sortie += [
        "",
        f"{'':<22}{'Total HT':<20}{euros(total_ht):>8}",
        f"{'':<22}{'Total TVA':<20}{euros(total_tva):>8}",
        f"{'':<22}{'Total':<20}{euros(total_ttc):>8}",
    ]
    return "\n".join(sortie)


# ---------- Programme principal ----------

def main(arguments):
    if len(arguments) != 3:
        print(__doc__)
        return 1

    magasin, vendeur, texte_panier = arguments
    articles = charger_articles()

    try:
        panier = parser_panier(texte_panier, articles)
    except ValueError as erreur:
        print(f"Erreur : {erreur}")
        return 1

    lignes = calculer_lignes(panier, articles)
    numero = prochain_numero_ticket()
    print(generer_ticket(magasin, vendeur, numero, lignes))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))