produits:list[dict] = [
    {"code_article":"C01", "description":"pack de coca", "prix_HT":5},
    {"code_article":"C02", "description":"kilo de pdt", "prix_HT":1},
    {"code_article":"C03", "description":"pack Biscotte", "prix_HT":2},
    {"code_article":"C04", "description":"Café soluble", "prix_HT":3},
    {"code_article":"C05", "description":"Crackers", "prix_HT":4}
]

import sys
import datetime

if len(sys.argv) != 4:  # 4 car sys.argv[0] = nom du script + 3 paramètres
    print("Usage: python script.py nom_du_magasin nom_du_vendeur liste_des_articles")
    sys.exit(1)
    
nom_magasin:str = sys.argv[1]
nom_vendeur:str = sys.argv[2]
list_articles_brut:str = sys.argv[3]

list_articles: list[list[str | int]] = []

# Séparer par le pipe |
articles = list_articles_brut.split("|")

for article in articles:
    # Séparer par le deux-points :
    parties = article.split(":")
    code_article = parties[0]
    nb_article = int(parties[1])
    list_articles.append([code_article, nb_article])

today = datetime.datetime.now()
date = today.strftime("%d/%m/%y")


