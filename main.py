# Importation des modules
import sys
from datetime import datetime

# Catalogue : dictionnaire de dictionnaires, une entrée par article
dic_article: dict = {
    "C01": {"description": "Pack de coca",     "prix HT unitaire": 5, "tva": 0.10},
    "C02": {"description": "Kilo de pdt",      "prix HT unitaire": 1, "tva": 0.10},
    "C03": {"description": "Pack de biscotte", "prix HT unitaire": 2, "tva": 0.10},
    "C04": {"description": "Café soluble",     "prix HT unitaire": 3, "tva": 0.10},
    "C05": {"description": "Crackers",         "prix HT unitaire": 4, "tva": 0.10},
}


def lire_arguments():
    # On attend 3 arguments en plus (sys.argv[0] est le nom du script)
    if len(sys.argv) != 4:
        print('Usage : python3 main.py "Magasin" "Vendeur" "C01:10|C02:2"')
        sys.exit(1)

    magasin = sys.argv[1]
    vendeur = sys.argv[2]
    commande = sys.argv[3]

    articles = []
    # Les articles sont séparés par "|"
    for element in commande.split("|"):
        # Chaque article est de la forme "CODE:QUANTITE"
        code, quantite = element.split(":")
        articles.append((code.strip().upper(), int(quantite)))

    return magasin, vendeur, articles


def generer_numero_et_date():
    # Génération du numéro de ticket et de la date
    maintenant = datetime.now()
    numero = maintenant.strftime("%y%m%d%H%M%S")
    date = maintenant.strftime("%d/%m/%Y")
    return numero, date


# Fonction pour calculer les montants
def calcul_montant(articles: list) -> tuple:
    # Initialisation des variables
    lignes = []
    total_ht = 0
    total_tva = 0

    for code, quantite in articles:
        if code in dic_article:
            article = dic_article[code]
            montant_ht = article["prix HT unitaire"] * quantite
            montant_tva = montant_ht * article["tva"]

            # On garde le détail de la ligne pour l'affichage du ticket
            lignes.append({
                "quantite": quantite,
                "description": article["description"],
                "prix_ht": article["prix HT unitaire"],
                "tva": article["tva"],
                "total_ttc": round(montant_ht + montant_tva, 2),
            })

            total_ht += montant_ht
            total_tva += montant_tva

    total_ttc = total_ht + total_tva
    return lignes, round(total_ht, 2), round(total_tva, 2), round(total_ttc, 2)


# Point d'entrée du programme
if __name__ == "__main__":
    magasin, vendeur, articles = lire_arguments()
    numero, date = generer_numero_et_date()
    lignes, total_ht, total_tva, total_ttc = calcul_montant(articles)

    # Affichage temporaire pour vérifier
    print("Ticket numéro :", numero)
    print("Date :", date)
    print(lignes)
    print(total_ht, total_tva, total_ttc)