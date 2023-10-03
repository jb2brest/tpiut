# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 09:33:19 2023

@author: Papam
"""

class Item:
    def __init__(self, code, description, prix_unitaire, tva): 
        self.code = code
        self.description = description
        self.prix_unitaire = prix_unitaire
        self.tva = tva

class Reception:
    def __init__(self, nom_magasin, numéro_ticket, date, nom_caissier):
        self.nom_magasin = nom_magasin
        self.numéro_ticket = numéro_ticket
        self.date = date
        self.nom_caissier = nom_caissier
        self.items = []

    def ajout_item(self, item, Quantite):
        self.items.append((item, Quantite))

    def calcul_total(self):
        total_ht = sum(item[0].prix_unitaire * item[1] for item in self.items)
        total_tva = sum((item[0].prix_unitaire * item[1] * item[0].tva / 100) for item in self.items)
        total = total_ht + total_tva
        return total_ht, total_tva, total

    def generer_reçu(self):
        print(f"{self.nom_magasin}\nTicket numéro: {self.numéro_ticket}\nDate: {self.date}\nVous avez été servi par: {self.nom_caissier}\n")
        print("NB  Desc.                  HT unitaire  TVA   Total")
        for item, Quantite in self.items:
            print(f"{Quantite}   {item.description}              {item.prix_unitaire}           {item.tva}%    {item.prix_unitaire * Quantite + (item.prix_unitaire * Quantite * item.tva / 100)}")
        
        total_ht, total_tva, total = self.calcul_total()
        print(f"\nTotal HT: {total_ht}€\nTotal TVA: {total_tva}€\nTotal: {total}€")


if __name__ == "__main__":
    import datetime  # Nous utilisons cette bibliothèque pour obtenir la date actuelle

    store_name = "BUT Market"
    ticket_number = 2200
    date = datetime.date.today().strftime("%d/%m/%Y")
    cashier_name = "Mathis, Mballo, Antoine"

    reception = Reception(store_name, ticket_number, date, cashier_name)

#Cette boucle while nous permet de rajouter des articles autant qu'on veut et de renseigner nous mêmes tous les paramètres
    while True:
        item_code = input("Code de l'article (ou 'q' pour quitter) : ")
        if item_code.lower() == 'q':
            break

        item_description = input("Description de l'article : ")
        item_prix = float(input("Prix unitaire HT : "))
        item_tva = float(input("Taux de TVA (%) : "))

        item = Item(item_code, item_description, item_prix, item_tva)
        

        Quantite = int(input("Quantite : "))
        reception.ajout_item(item, Quantite)

    reception.generer_reçu()
