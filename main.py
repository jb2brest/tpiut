class Item:
    def __init__(self, code, description, prix_unite, tva, poids_ou_volume, poids_unitaire):
        self.code = code
        self.description = description
        self.prix_unite = prix_unite
        self.tva = tva
        self.poids_ou_volume = poids_ou_volume  # Poids ou volume unitaire
        self.poids_unitaire = poids_unitaire  # Poids unitaire

class Reception:
    def __init__(self, magasin, num_ticket, date, caissier):
        self.magasin = magasin
        self.num_ticket = num_ticket
        self.date = date
        self.caissier = caissier
        self.items = []

    def ajout_item(self, item, quantite):
        item.poids_ou_volume_total = quantite * item.poids_unitaire  # Calcul du poids ou volume total
        self.items.append((item, quantite))

    def calcul_total(self):
        # Fais la somme totale du prix unitaire multiplié par la quantité de chacun des produits pour obtenir le total hors taxe
        total_ht = sum(item[0].prix_unite * item[1] for item in self.items)
        # Calcul de la TVA seule (taux de tva du produit divisé par 100 pour l'appliquer dans le calcul)
        total_tva = sum((item[0].prix_unite * item[1] * item[0].tva / 100) for item in self.items)
        # Calcul prix total avec la somme HT + la TVA
        total = total_ht + total_tva
        return total_ht, total_tva, total

    def afficher_reçu(self):
        print(f"{self.magasin}\nTicket numéro: {self.num_ticket}\nDate: {self.date}\nVous avez été servi par: {self.caissier}\n")
        print("NB  Desc.                  Poids/volume unitaire  Poids/volume total  HT unitaire  TVA   Total")
        for item, Quantite in self.items:
            resultat = re.search(r'(\d+)([a-zA-Z]+)', item.poids_ou_volume)
            if resultat:
                mesure = resultat.group(2)

            print(f"{Quantite}   {item.description}              {item.poids_ou_volume}           {item.poids_ou_volume_total}{mesure}   {item.prix_unite}€           {item.tva}%    {item.prix_unite * Quantite + (item.prix_unite * Quantite * item.tva / 100)}€")

        total_ht, total_tva, total = self.calcul_total()
        print(f"\nTotal HT: {total_ht:.2f}€")
        print(f"Total TVA: {total_tva:.2f}€")
        print(f"Total: {total:.2f}€")

if __name__ == "__main__":
    import datetime
    import sys
    import re

    # Définition de la base de données des articles
    articles = [
        {"code": "C01", "description": "pack de coca", "prix_unite": 5, "tva": 20, "poids_ou_volume": "2kg", "poids_unitaire": 2},
        {"code": "C02", "description": "kilo de pdt", "prix_unite": 1, "tva": 10, "poids_ou_volume": "1kg", "poids_unitaire": 1},
        {"code": "C03", "description": "pas Biscotte", "prix_unite": 2, "tva": 10, "poids_ou_volume": "950g", "poids_unitaire": 950},
        {"code": "C04", "description": "Café soluble", "prix_unite": 3, "tva": 10, "poids_ou_volume": "250g", "poids_unitaire": 250},
        {"code": "C05", "description": "Crackers", "prix_unite": 4, "tva": 20, "poids_ou_volume": "125g", "poids_unitaire": 125},
        {"code": "C06", "description": "Eau", "prix_unite": 6, "tva": 10, "poids_ou_volume": "1,5L", "poids_unitaire": 1.5},
        {"code": "C07", "description": "Pain", "prix_unite": 1, "tva": 10, "poids_ou_volume": "250g", "poids_unitaire": 250},
    ]

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
            item_poids_ou_volume = item_info_db['poids_ou_volume']
            item_poids_unitaire = item_info_db['poids_unitaire']

            item = Item(item_code, item_description, item_prix, item_tva, item_poids_ou_volume, item_poids_unitaire)
            reception.ajout_item(item, Quantite)
        else:
            print(f"Code article {item_code} non trouvé dans la base de données.")


    reception.afficher_reçu()
