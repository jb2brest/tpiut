import sys
import datetime
from random import randint

dict = {'C01':["pack de coca","2 kg",5,0.2],'C02':["kilo de pdt","1 kg",1,0.1],'C03':["pack Biscotte","950 g",2,0.1],'C04':["Café soluble","250 g",3,0.1],'C05':["Crackers","125 g",4,0.2],'C06':["Eau","1.5 L",6,0.1],'C07':["Pain","250 g",1,0.1]}

def calcul_poids(dict, id, quantite):
    poids = dict[id][1].split(" ")
    poids_int = int(poids[0])
    poids_str = f"{poids_int} {poids[1]}"
    return (poids_int*quantite, poids_str)

def calc_poids(dict, articles):
    poids_art = {}
    for article in articles:
        id_article, quantite_article = article.split(":")
        assert id_article != ""
        assert quantite_article != ""
        quantite_article = int(quantite_article)
        poids_article, poids_article_str = calcul_poids(dict, id_article, quantite_article)
        poids_art[id_article] = [poids_article, poids_article_str]
    return poids_art

def calcul_prix(dict, id, quantite):
    assert(type(id)) == str
    assert(type(quantite)) == int
    tva = dict[id][3]
    prix_ht = dict[id][2]
    prix_tva = prix_ht * tva
    prix_total_tva = (prix_ht + prix_tva) * quantite
    prix_total_ht = prix_ht * quantite
    return (prix_ht, prix_tva, prix_total_tva, prix_total_ht)

def parser_articles(dict, articles):
    assert(type(articles)) == list
    ticket = {}
    for article in articles:
        id_article, quantite_article = article.split(":")
        assert id_article != ""
        assert quantite_article != ""
        quantite_article = int(quantite_article)
        description_produit = dict[id_article][0]
        prix_ht, prix_tva, prix_total_tva, prix_total_ht = calcul_prix(dict, id_article, quantite_article)
        ticket[id_article] = [quantite_article, description_produit, prix_ht, prix_tva, prix_total_tva, prix_total_ht]
    return ticket

def afficher_ticket(nom_ticket, nom_serveur, poids_dict, ticket):
    assert(type(nom_ticket)) == str
    assert(type(nom_serveur)) == str
    print(f'''
{nom_ticket}
Ticket numéro : {randint(0,3000)}

Date : {datetime.date.today().strftime("%d/%m/%Y")}

Vous avez été servi par : {nom_serveur}
''')

    print(f"{'NB':<8} {'Desc.':<20} {'Pds/vol. unitaire':<20} {'Pds/vol. total':<20} {'HT unitaire':<15} {'TVA':<8} {'Total':<8}")

    total_ht = 0
    total_tva = 0
    total = 0
    poids_total = 0

    for id_article, details in ticket.items():
        quantite, description, prix_ht, prix_tva, prix_total_tva, prix_total_ht = details
        total_ht += prix_total_ht
        total_tva += prix_tva * quantite
        total += prix_total_tva
        poids = poids_dict[id_article][1]
        poids_total += poids_dict[id_article][0]

        poids_total_str = f"{poids_dict[id_article][0]}{poids.split(' ')[1]}"
        print(f"{quantite:<8} {description:<20} {poids:<20} {poids_total_str:<20} {prix_ht}€{' '*12} {int(prix_tva/prix_ht*100)}%{' '*6} {prix_total_tva:.1f}€")

    print(f"\n{' '*85}Total HT{' '*4}{total_ht:.1f}€")
    print(f"{' '*85}Total TVA{' '*3}{total_tva:.1f}€")
    print(f"{' '*85}Total{' '*7}{total:.1f}€")

def ajouter_produit(id,desc,poids,prix_ht,tva,dict=dict):
    has_space=False
    for elem in poids.split():
        if elem == " ":
            has_space=True
    if has_space==False:
        for elem in poids.split(" "):
            if type(elem) == str:
                elem = f" {elem}"
    dict[id] = [desc,poids,prix_ht,tva]

if __name__ == "__main__":
    assert len(sys.argv) == 4
    print(f"{'Code article':<20} {'Description':<20} {'Poids/Vol.':<20} {'Prix unitaire hors taxe':<20} {'TVA':<25}")

    for codeArticle, (description, poids, prix, tva) in dict.items():
        print(f"{codeArticle:<20} {description:<20} {poids:<20} {prix:<20} {tva:<20}")

    articles = sys.argv[3].split("|")
    ticket = parser_articles(dict, articles)
    poids_articles = calc_poids(dict, articles)
    afficher_ticket(sys.argv[1], sys.argv[2], poids_articles, ticket)
    ajouter = str(input("Ajouter produit ? (oui/non) : "))
    if ajouter == "oui":
        ajout = str(input("Ajouter produit au format suivant : id,desc,poids,prix_ht,tva avec les virgules :"))
        id,desc,poids,prix_ht,tva = ajout.split(",")
        ajouter_produit(str(id),str(desc),str(poids),int(prix_ht),float(tva),dict=dict)
        print(f"{'Code article':<20} {'Description':<20} {'Poids/Vol.':<20} {'Prix unitaire hors taxe':<20} {'TVA':<25}")

        for codeArticle, (description, poids, prix, tva) in dict.items():
            print(f"{codeArticle:<20} {description:<20} {poids:<20} {prix:<20} {tva:<20}")