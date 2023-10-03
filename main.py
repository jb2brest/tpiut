import datetime
import sys

class Article:
    def __init__(self, code, description, poids_volume_unitaire, prix_ht, tva, origine):
        self.code = code
        self.description = description
        self.poids_volume_unitaire = poids_volume_unitaire
        self.prix_ht = prix_ht
        self.tva = tva
        self.origine = origine

class TicketDeCaisse:
    def __init__(self, magasin, caissier, numero_ticket):
        self.magasin = magasin
        self.caissier = caissier
        self.articles = []
        self.numero_ticket = numero_ticket

    def ajouter_article(self, article, quantite):
        self.articles.append((article, quantite))

    def generer_ticket(self):
        total_ht = 0
        total_tva = 0

        print(f"{self.magasin}")
        print(f"Ticket numéro : {self.numero_ticket}")
        print(f"Date : {self.generer_date()}")
        print(f"Vous avez été servi par : {self.caissier}\n")
        print("NB    Desc.             Poids/volume unitaire    Poids/volume total    HT unitaire    TVA     Total")

        for article, quantite in self.articles:
            montant_ht = article.prix_ht * quantite
            montant_tva = montant_ht * (article.tva / 100)
            total_ht += montant_ht
            total_tva += montant_tva

            print(f"{quantite}   {article.description}                  {article.poids_volume_unitaire}kg               {quantite * float(article.poids_volume_unitaire)}kg                {article.prix_ht}€         {article.tva}%      {montant_ht + montant_tva}€")

        print(f"\nTotal HT        {total_ht}€")
        print(f"Total TVA       {total_tva}€")
        print(f"Total           {total_ht + total_tva}€")

        self.numero_ticket += 1

    def generer_date(self):
        date_actuelle = datetime.datetime.now()
        return date_actuelle.strftime("%d/%m/%Y")

if __name__ == "__main__":
    # Récupérer les paramètres de ligne de commande
    if len(sys.argv) != 4:
        print("Usage: python3 main.py <magasin> <caissier> <commandes>")
        sys.exit(1)

    magasin = sys.argv[1]
    caissier = sys.argv[2]
    commandes = sys.argv[3].split("|")

    # Lire le numéro de ticket depuis le fichier et l'incrémenter
    with open("numero_ticket.txt", "r") as file:
        numero_ticket = int(file.read())
    numero_ticket += 1
    with open("numero_ticket.txt", "w") as file:
        file.write(str(numero_ticket))

    ticket = TicketDeCaisse(magasin, caissier, numero_ticket)

    articles = {
        "C01": Article("C01", "pack de coca", "2", 5, 20, "Lituanie"),
        "C02": Article("C02", "kilo de pdt", "1", 1, 10, "Espagne"),
        "C03": Article("C03", "pack Biscotte", "0.950", 2, 10, "France"),
        "C04": Article("C04", "Cafe soluble", "0.250", 3, 10, "Roumanie"),
        "C05": Article("C05", "Crackers", "0.125", 4, 20, "Angleterre"),
        "C06": Article("C06", "Eau", "1,5", 6, 10, "Suisse"),
        "C07": Article("C07", "Pain", "0.250", 1, 10, "France")
        # Ajoutez d'autres articles ici si nécessaire
    }

    for commande in commandes:
        code, quantite = commande.split(":")
        article = articles.get(code)
        if article:
            ticket.ajouter_article(article, int(quantite))

    ticket.generer_ticket()
