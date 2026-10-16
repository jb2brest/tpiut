# Importation des modules
import sys

# Dictionnaire des articles
dic_article: dict = {
    "C01": {"description": "Pack de coca",     "prix HT unitaire": 5, "tva": 0.10},
    "C02": {"description": "Kilo de pdt",      "prix HT unitaire": 1, "tva": 0.10},
    "C03": {"description": "Pack de biscotte", "prix HT unitaire": 2, "tva": 0.10},
    "C04": {"description": "Café soluble",     "prix HT unitaire": 3, "tva": 0.10},
    "C05": {"description": "Crackers",         "prix HT unitaire": 4, "tva": 0.10},
}

# Fonction pour lire les arguments de la ligne de commande
def lire_arguments():
    """Récupère le magasin, le vendeur et la liste des articles commandés
    depuis la ligne de commande.
    Exemple : python3 main.py "But Market" "Lisa" "C01:10|C02:2"
    Retourne : ("But Market", "Lisa", [("C01", 10), ("C02", 2)])
    """
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

def calcul_montant(arguments : tuple) -> tuple :
    for code, quantite in arguments[2] :
        if code not in dic_article :
            article = dic_article[code]
        
        montant_ht = article["prix HT unitaire"] * quantite
        montant_tva = montant_ht * article["tva"]

        total_ht += montant_ht
        total_tva += montant_tva

    total_ttc = total_ht + total_tva
    return total_ht, total_tva, total_ttc

# Point d'entrée du programme
if __name__ == "__main__":
    magasin, vendeur, articles = lire_arguments()
    print(magasin, vendeur, articles)
