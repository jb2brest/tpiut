import datetime

class Article:
    def __init__(self, code, description, prix_ht, tva):
        self.code = code
        self.description = description
        self.prix_ht = prix_ht
        self.tva = tva

class TicketDeCaisse:
    def __init__(self, magasin, caissier):
        self.magasin = magasin
        self.caissier = caissier
        self.articles = []
        self.numero_ticket = 2000

    def ajouter_article(self, article, quantite):
        self.articles.append((article, quantite))

    def generer_ticket(self):
        total_ht = 0
        total_tva = 0

        print(f"{self.magasin}")
        print(f"Ticket numéro : {self.numero_ticket}")
        print(f"Date : {self.generer_date()}")
        print(f"Vous avez été servi par : {self.caissier}\n")
       print("NB    Desc.             HT unitaire    TVA     Total")

        for article, quantite in self.articles:
            montant_ht = article.prix_ht * quantite
            montant_tva = montant_ht * (article.tva / 100)
            total_ht += montant_ht
            total_tva += montant_tva

            print(f"{quantite}     {article.description}      {article.prix_ht}€              {article.tva}%      {montant_ht + montant_tva}€")

        print(f"\nTotal HT        {total_ht}€")
        print(f"Total TVA       {total_tva}€")
        print(f"Total           {total_ht + total_tva}€")

        self.numero_ticket += 1

    def generer_date(self):
        # Utilisez le module datetime pour obtenir la date actuelle au format DD/MM/YYYY
        date_actuelle = datetime.datetime.now()
        return date_actuelle.strftime("%d/%m/%Y")

if __name__ == "__main__":
    magasin = "But Market"
    caissier = "Lisa"
    ticket = TicketDeCaisse(magasin, caissier)

    articles = {
        "C01": Article("C01", "pack de coca", 5, 10),
        "C02": Article("C02", "kilo de pdt", 1, 10),
        "C03": Article("C03", "pack Biscotte", 2, 10),
        # Ajoutez d'autres articles ici si nécessaire
    }

    commandes = ["C01:10", "C02:2"]

    for commande in commandes:
        code, quantite = commande.split(":")
        article = articles.get(code)
        if article:
            ticket.ajouter_article(article, int(quantite))

    ticket.generer_ticket()
