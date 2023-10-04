class Item:
    def __init__(self, code, description, prix_unite, tva): 
        self.code = code
        self.description = description
        self.prix_unite = prix_unite
        self.tva = tva

class Reception:
    def __init__(self, magasin, num_ticket, date, caissier):
        self.magasin = magasin
        self.num_ticket = num_ticket
        self.date = date
        self.caissier = caissier
        self.items = []


    def ajout_item(self, item, quantite):
        self.items.append((item, quantite))

    def calcul_total(self):
        # fais la somme totale du prix unitaire multiplié par la quantité de chacun des produits pour obtenir le total hors taxe
        total_ht = sum(item[0].prix_unite * item[1] for item in self.items)
        # calcul de la TVA seule ( taux de tva du produit divisé par 100 pour l'appliquer dans le calcul ) 
        total_tva = sum((item[0].prix_unite * item[1] * item[0].tva / 100) for item in self.items) 
        # calcul prix total avec la somme HT + la TVA
        total = total_ht + total_tva 
        return total_ht, total_tva, total

    def afficher_reçu(self):
        print(f"{self.magasin}\nTicket numéro: {self.num_ticket}\nDate: {self.date}\nVous avez été servi par: {self.caissier}\n")
        print("NB  Desc.                  HT unitaire  TVA   Total")
        for item, Quantite in self.items:
            print(f"{Quantite}   {item.description}              {item.prix_unite}           {item.tva}%    {item.prix_unite * Quantite + (item.prix_unite * Quantite * item.tva / 100)}")
        
        total_ht, total_tva, total = self.calcul_total()
        print(f"\nTotal HT: {total_ht}€\nTotal TVA: {total_tva}€\nTotal: {total}€")



if __name__ == "__main__":
    import datetime
    import sys


     # Définition de la base de données des articles
    articles = [
        {"code": "C01", "description": "pack de coca", "prix_unite": 5, "tva": 10},
        {"code": "C02", "description": "kilo de pdt", "prix_unite": 1, "tva": 10},
        {"code": "C03", "description": "pack Biscotte", "prix_unite": 2, "tva": 10},
        {"code": "C04", "description": "Café soluble", "prix_unite": 3, "tva": 10},
        {"code": "C05", "description": "Crakers", "prix_unite": 4, "tva": 10},
    ]

    # Définition des données d'entêtes du ticket
    magasin = sys.argv[1:]
    ticket_id = 2200
    date = datetime.date.today().strftime("%d/%m/%Y")
    caissier = sys.argv[2:]

    reception = Reception(magasin, ticket_id, date, caissier)

    item_1 = sys.argv[3:].split('|')
    print(item_1)

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
