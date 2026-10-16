"""Générateur de tickets de caisse.

Utilisation :
    python3 main.py "BUT Market" "Lisa" "C01:1|C02:3|C03:4"
"""

import json
import sys
from datetime import date

FICHIER_ARTICLES = "articles_2.json"
FICHIER_NUMERO = "dernier_ticket.txt"
NUMERO_DEPART = 2200


# ---------- Données ----------

def charger_articles(chemin=FICHIER_ARTICLES):
    """Charge la liste des articles depuis le fichier JSON."""
    with open(chemin, encoding="utf-8") as f:
        return json.load(f)


def prochain_numero_ticket(chemin=FICHIER_NUMERO):
    """Renvoie le numéro du nouveau ticket et le sauvegarde."""
    try:
        with open(chemin) as f:
            numero = int(f.read().strip()) + 1
    except FileNotFoundError:
        numero = NUMERO_DEPART
    with open(chemin, "w") as f:
        f.write(str(numero))
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


# ---------- Poids / volume ----------

def lire_poids(texte):
    """Sépare "950g" en (950.0, "g") et "1,5L" en (1.5, "L")."""
    i = 0
    while i < len(texte) and (texte[i].isdigit() or texte[i] in ",."):
        i += 1
    valeur = float(texte[:i].replace(",", "."))
    unite = texte[i:]
    return valeur, unite


def poids_total(texte_unitaire, quantite):
    """Calcule le poids total : 4 x "950g" -> "3,8kg"."""
    valeur, unite = lire_poids(texte_unitaire)
    total = valeur * quantite
    # On passe à l'unité supérieure quand on dépasse 1000
    if unite == "g" and total >= 1000:
        total, unite = total / 1000, "kg"
    elif unite == "mL" and total >= 1000:
        total, unite = total / 1000, "L"
    return nombre(total) + unite


# ---------- Calculs ----------

def calculer_lignes(panier, articles):
    """Calcule le détail de chaque ligne du ticket."""
    lignes = []
    for code, quantite in panier:
        article = articles[code]
        total_ht = quantite * article["prix_ht"]
        total_tva = total_ht * article["tva"]
        lignes.append({
            "quantite": quantite,
            "description": article["description"],
            "poids": article["poids"],
            "poids_total": poids_total(article["poids"], quantite),
            "prix_ht": article["prix_ht"],
            "tva": article["tva"],
            "total_ht": total_ht,
            "total_tva": total_tva,
            "total_ttc": total_ht + total_tva,
        })
    return lignes


def calculer_totaux(lignes):
    total_ht = sum(l["total_ht"] for l in lignes)
    total_tva = sum(l["total_tva"] for l in lignes)
    return total_ht, total_tva, total_ht + total_tva


# ---------- Affichage ----------

def nombre(valeur):
    """Formate 5.0 en '5' et 5.5 en '5,5'."""
    return f"{round(valeur, 2):g}".replace(".", ",")


def euros(montant):
    return nombre(montant) + "€"


def generer_ticket(magasin, vendeur, numero, lignes):
    total_ht, total_tva, total_ttc = calculer_totaux(lignes)

    sortie = [
        magasin,
        f"Ticket numéro : {numero}",
        "",
        f"Date : {date.today():%d/%m/%Y}",
        "",
        f"Vous avez été servi par : {vendeur}",
        "",
        f"{'NB':<5}{'Desc.':<16}{'Poids/volume unitaire':>22}{'Poids/volume total':>20}"
        f"   {'HT unitaire':<13}{'TVA':>4}{'Total':>8}",
    ]
    for l in lignes:
        tva = f"{int(l['tva'] * 100)}%"
        sortie.append(
            f"{l['quantite']:<5}{l['description']:<16}{l['poids']:>22}{l['poids_total']:>20}"
            f"   {euros(l['prix_ht']):<13}{tva:>4}{euros(l['total_ttc']):>8}"
        )
    sortie += [
        "",
        f"{'':<66}{'Total HT':<12}{euros(total_ht):>7}",
        f"{'':<66}{'Total TVA':<12}{euros(total_tva):>7}",
        f"{'':<66}{'Total':<12}{euros(total_ttc):>7}",
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