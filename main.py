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

    magasin:str = "BUT MARKET"
    ticket_id:int = 2200
    date = datetime.date.today().strftime("%d/%m/%Y")
    caissier:str = "Lisa"

    reception = Reception(magasin, ticket_id, date, caissier)

    reception.afficher_reçu()
