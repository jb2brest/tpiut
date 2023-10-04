class Item:
    def __init__(self, code, description, prix_unite, tva): 
        self.code = code
        self.description = description
        self.prix_unite = prix_unite
        self.tva = tva

if __name__ == "__main__":
    import datetime

magasin:str = "BUT MARKET"
ticket_id:int = 2200
date = datetime.date.today().strftime("%d/%m/%Y")
caissier:str = "Lisa"
