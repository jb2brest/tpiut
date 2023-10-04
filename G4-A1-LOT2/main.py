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
    total_poids = 0

    for article, quantite in commande.items():
        for articleItem in articles:
            if articleItem.get(article):
                nom_article, poids_unitaire, prix_unitaire, tva = articleItem[article]
                art_ht = prix_unitaire * quantite
                art_ttc = art_ht * tva
                total_ht = total_ht + art_ht  # Total de chaque produit
                total_ttc = total_ttc + art_ttc
                total_tva = total_ttc - total_tva
                total_poids = poids_unitaire * quantite
                print(art_ttc, art_ht)

    return total_ht, total_tva, total_ttc, total_poids


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

    total_ht, total_tva, total_ttc, total_poids = total_calculation(articles, commande)

    # Entête du ticket
    print(nom_magasin)
    print(f"Ticket numéro : {total_order_txt()}")
    print(f"Date : {datetime.date.today()}")
    print(f"Vous avez été servi par : {nom_hote_caisse}")

    # Articles
    print("\nNB\tDesc.\t\t\tHT unitaire\tTVA\tTotal")
    for article, quantite in commande.items():
        nom_article = "Produit Inconnu"
        poids_unitaire = 0
        prix_unitaire = 0
        tva = 0
        for item in articles:
            if item.get(article):
                nom_article, poids_unitaire, prix_unitaire, tva = item[article]
        # Calcul du total du prix par chaque article en fonction de ca quantité et de son prix
        printable_tva: int = round((tva - 1) * 100)
        prix_total = prix_unitaire * quantite
        prix_total_ttc = prix_total * tva  # Ajout de la TVA
        print(f"{quantite}\t{nom_article}\t\t\t{prix_unitaire}€\t\t{printable_tva}%\t{prix_total_ttc:.2f}€")

    # Totaux des prix par chaque article en fonction de ca quantité et de son prix

    print("\n\t\t\t\tTotal HT\t\t{:.2f}€".format(total_ht))
    print("\t\t\t\tTotal TVA\t\t{:.2f}€".format(total_tva))
    print("\t\t\t\tTotal\t\t{:.2f}€".format(total_ttc))
    print("\t\t\t\tTotal poids\t\t{:.2f}Kg".format(total_poids))

    # PS J'ai pas reussi à print correctement les valeurs faudrait revoire cette ligne ci dessous
    # "print(f"{quantite}\t{nom_article}\t\t\t{prix_unitaire}€\t\t{printable_tva}%\t{prix_total_ttc:.2f}€")"


if __name__ == "__main__":
    main()
