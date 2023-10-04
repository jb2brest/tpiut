import json
import sys
import datetime


# Charger la base d'articles depuis le fichier JSON
def load_json():
    with open('base_articles.json', 'r') as fichier:
        data = json.load(fichier)
        return data['base']


# Lire et modifier le fichier texte contenant le numéro du ticket
def total_order_txt() -> str:
    # Fonction qui permet de lire la valeur d'un fichier texte contenant le numéro de ticket actuel

    fichier = open('nb_ticket.txt', 'r')
    nb = fichier.read()
    fichier.close()
    modif_txt(int(nb))
    return nb


def modif_txt(nb):
    # Fonction qui permet d'ajouter 1 au fichier contenant le numéro de ticket actuel

    fichier = open('nb_ticket.txt', 'w+')
    fichier.write(f'{int(nb) + 1}')
    fichier.close()


# Calculer le total de tous les achats en fonction des articles et des quantités

def total_calculation(articles, commande):

    # Permet de calculer le cout totaux de chaques articles

    total_ht = 0
    total_tva = 0
    total_ttc = 0
    items = []

    for article, quantite in commande.items():
        for articleItem in articles:
            if articleItem.get(article):
                nom_article, prix_unitaire = articleItem[article]
                art_ht = prix_unitaire * quantite
                art_ttc = art_ht * 1.1
                total_ht = total_ht + art_ht  # Total de chaque produit
                total_ttc = total_ttc + art_ttc
                total_tva = total_ttc - total_tva
                items.append((nom_article, quantite, prix_unitaire, art_ttc))
                print(art_ttc, art_ht)

    items.append(("Total HT", "", "", total_ht))
    items.append(("Total TVA", "", "", total_tva))
    items.append(("Total", "", "", total_ttc))

    return items, total_ht, total_tva, total_ttc


def main():
    # Vérifier le nombre d'arguments passés en ligne de commande
    if len(sys.argv) != 4:
        print("Usage: python main.py <nom_magasin> <nom_hote_caisse> <commande>")
        return
    nom_magasin = sys.argv[1]
    nom_hote_caisse = sys.argv[2]
    commande_texte = sys.argv[3]

    # Use for Debug Only
    # nom_magasin = "BUT Market"
    # nom_hote_caisse = "Lisa"
    # commande_texte = "C01:10|C02:5"

    # Charger la base d'articles
    articles = load_json()

    # Parser(térifiant le sax(xml) d'ailleur) la commande et calculer le total
    commande = {}
    for element in commande_texte.split('|'):
        article, quantite = element.split(':')
        commande[article] = int(quantite)

    # Généreration du ticket de caisse

    items, total_ht, total_tva, total_ttc = total_calculation(articles, commande)

    # Entête du ticket
    print(nom_magasin)
    print(f"Ticket numéro : {total_order_txt()}")
    print(f"Date : {datetime.date.today()}")
    print(f"Vous avez été servi par : {nom_hote_caisse}")

    # Articles
    print("\nNB\tDesc.\t\t\tHT unitaire\tTVA\tTotal")
    for article, quantite in commande.items():
        nom_article = "Produit Inconnu"
        prix_unitaire = 0
        for item in articles:
            if item.get(article):
                nom_article, prix_unitaire = item[article]
        # Calcul du total du prix par chaque article en fonction de ca quantité et de son prix
        prix_total = prix_unitaire * quantite
        prix_total_ttc = prix_total * 1.1  # Ajout de la TVA
        print(f"{quantite}\t{nom_article}\t\t{prix_unitaire}€\t\t10%\t{prix_total_ttc:.2f}€")

    # Totaux des prix par chaque article en fonction de ca quantité et de son prix
    print("\n\t\t\t\tTotal HT\t{:.2f}€".format(total_ht))
    print("\t\t\t\tTotal TVA\t{:.2f}€".format(total_tva))
    print("\t\t\t\tTotal\t\t{:.2f}€".format(total_ttc))

if __name__ == "__main__":
    main()
