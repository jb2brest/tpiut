if __name__ == "__main__":
    import datetime

    # Définition de la base de données des articles
    articles = [
        {"code": "C01", "description": "pack de coca", "prix_unite": 5, "tva": 20},
        {"code": "C02", "description": "kilo de pdt", "prix_unite": 1, "tva": 10},
        {"code": "C03", "description": "pack Biscotte", "prix_unite": 2, "tva": 10},
        {"code": "C04", "description": "Café soluble", "prix_unite": 3, "tva": 5},
        {"code": "C05", "description": "Crakers", "prix_unite": 4, "tva": 10},
    ]

    magasin = "BUT MARKET"
    ticket_id = 2200
    date = datetime.date.today().strftime("%d/%m/%Y")
    caissier = "Lisa"

    reception = Reception(magasin, ticket_id, date, caissier)

    while True:
        item_code = input("Code de l'article (ou 'q' pour quitter) : ")
        if item_code.lower() == 'q':
            break

        # Recherche de l'article dans la base de données en fonction du code
        item_info = next((item for item in articles if item['code'] == item_code), None)

        if item_info:
            item_description = item_info['description']
            item_prix = item_info['prix_unite']
            item_tva = item_info['tva']

            item = Item(item_code, item_description, item_prix, item_tva)

            Quantite = int(input("Quantite : "))
            reception.ajout_item(item, Quantite)
        else:
            print("Code article non trouvé dans la base de données.")

    reception.afficher_reçu()
