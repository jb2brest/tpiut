import sys
import datetime

produits:list[dict] = [
    {"code_article":"C01", "description":"pack de coca", "prix_HT":5},
    {"code_article":"C02", "description":"kilo de pdt", "prix_HT":1},
    {"code_article":"C03", "description":"pack Biscotte", "prix_HT":2},
    {"code_article":"C04", "description":"Café soluble", "prix_HT":3},
    {"code_article":"C05", "description":"Crackers", "prix_HT":4}
]

def calcule_TVA(prix_ht) -> int:
    prix_ttc = prix_ht*1.1
    return prix_ttc

def poids_total(code_article, nb_article) -> int:
    for produits in produits :
        if code_article == produits["code_article"] :
            poids = produits["poids"]
            poids = poids.split(" ")
            poids_total = int(poids[0]) * nb_article
            return poids_total

def recup_tva(code_article) -> int :
    for produits in produits :
        if code_article == produits["code_article"] :
            tva = produits["TVA"]
            tva = tva.split(" ")
            tva = int(tva[0])
            return tva
    
    
if len(sys.argv) != 4:  # 4 car sys.argv[0] = nom du script + 3 paramètres
    print("Usage: python script.py nom_du_magasin nom_du_vendeur liste_des_articles")
    sys.exit(1)

num_ticket=0
    
f = open('num_ticket.txt', 'r+')
num_ticket = int(f.read().strip())

try :
    nom_magasin:str = sys.argv[1]
    nom_vendeur:str = sys.argv[2]
    list_articles_brut:str = sys.argv[3]

    list_articles: list[list[str | int]] = []
    list_articles.append(["NB", "Desc.", "HT unitaire", "TVA", "Total"])

    # Séparer par le pipe |
    list_articles_brut = list_articles_brut.split("|")

    for article in list_articles_brut:
        # Séparer par le deux-points :
        parties = article.split(":")
        code_article = parties[0]
        nb_article = int(parties[1])
        for i in range (len(produits)):
            if code_article == produits[i]["code_article"] :
                prix_HT:int = produits[i]["prix_HT"]
                description = produits[i]["description"]
        prix_HT = prix_HT*nb_article
        total_TVA:float = calcule_TVA(prix_HT)  
        list_articles.append([nb_article, description, prix_HT, "10%", round(total_TVA, 2)])

    today = datetime.datetime.now()
    date = today.strftime("%d/%m/%y")

    print(f"{nom_magasin}\nTicket numéro : {num_ticket}\n\nDate : {date}\n")
    print(f"Vous avez été servi par : {nom_vendeur}\n")

    for ligne in list_articles:
        print("{:<5} {:<20} {:<12} {:<6} {:<8}".format(*ligne))
    print("\n")

    def calcul_total(list_article:list):
        total_HT = 0
        for i in range(1, len(list_article)):
            prix_HT = list_article[i][2]
            total_HT += float(prix_HT)
        total_TVA = calcule_TVA(total_HT)
        return [["","Total HT : ", f"{total_HT}€"], ["","Total TVA : ", f"{round(total_TVA-total_HT, 2)}€"], ["", "Total : ", f"{round(total_TVA, 2)}€"]]

    list_total = calcul_total(list_articles)

    for ligne in list_total:
        print("{:<35} {:<6} {:<8}".format(*ligne))

    num_ticket += 1
    f.seek(0)
    f.write(str(num_ticket))
    f.close()
except :
    print("Mauvaise syntaxe, merci de suivre cette syntaxe : main.py <nom_du_magasin> <nom_du_vendeur> <liste_des_articles au format CODE:QUANTITE|CODE:QUANTITE|... >")