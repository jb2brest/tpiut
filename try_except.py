if __name__ == "__main__":
    import datetime

    # ... (le reste du code)

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

            try:
                Quantite = int(input("Quantite : "))
                if Quantite <= 0:
                    print("La quantité doit être un nombre entier positif.")
                else:
                    reception.ajout_item(item, Quantite)
            except ValueError:
                print("Veuillez entrer un nombre entier pour la quantité.")
        else:
            print("Code article non trouvé dans la base de données.")

    reception.afficher_reçu()
