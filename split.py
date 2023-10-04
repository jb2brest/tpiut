import datetime
import sys

# Le code de la classe Item et de la classe Reception reste inchangé.

if __name__ == "__main__":
    # Vérification du nombre d'arguments de la ligne de commande
    if len(sys.argv) != 4:
        print("Utilisation : python3 main.py <nom_magasin> <nom_caissier> <articles>")
        sys.exit(1)

    # Récupération des arguments de la ligne de commande
    magasin = sys.argv[1]
    caissier = sys.argv[2]
    articles_str = sys.argv[3]

    # Diviser la chaîne d'articles en une liste d'articles (code:quantité)
    articles_list = articles_str.split('|')

    # Définition des données d'en-tête du ticket
    ticket_id = 2200
    date = datetime.date.today().strftime("%d/%m/%Y")

    reception = Reception(magasin, ticket_id, date, caissier)

    for item_str in articles_list:
        # Diviser la chaîne de l'article en code et quantité
        item_info = item_str.split(':')

        item_code = item_info[0]
        Quantite = int(item_info[1])

        # Recherche de l'article dans la base de données en fonction du code
        item_info_db = next((item for item in articles if item['code'] == item_code), None)

        if item_info_db:
            item_description = item_info_db['description']
            item_prix = item_info_db['prix_unite']
            item_tva = item_info_db['tva']

            item = Item(item_code, item_description, item_prix, item_tva)
            reception.ajout_item(item, Quantite)
        else:
            print(f"Code article {item_code} non trouvé dans la base de données.")

    reception.afficher_reçu()
