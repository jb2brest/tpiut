import sys
import datetime
from random import randint

dict = {'C01':["pack de coca",5],'C02':["kilo de pdt",1],'C03':["pack Biscotte",2],'C04':["Café soluble",3],'C05':["Crackers",4]}

def calcul_prix(dict, id, quantite):
    """
    Calcule les différents prix pour un article donné.
    
    dict: Dictionnaire contenant les informations des articles
    id: Identifiant de l'article
    quantite: Quantité de l'article
    :return: Tuple contenant le prix HT, la TVA, le prix total TTC et le prix total HT
    """
    assert(type(id)) == str
    assert(type(quantite)) == int
    tva = 0.1
    prix_ht = dict[id][1]
    prix_tva = prix_ht * tva
    prix_total_tva = (prix_ht + prix_tva) * quantite
    prix_total_ht = prix_ht * quantite
    return (prix_ht, prix_tva, prix_total_tva, prix_total_ht)

def parser_articles(dict, articles):
    """
    Parse la liste des articles commandés et calcule les détails pour chaque article.
    
    dict: Dictionnaire contenant les informations des articles
    articles: Liste des articles commandés
    :return: Dictionnaire contenant les détails de chaque article commandé
    """
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

def afficher_ticket(nom_ticket, nom_serveur, ticket):
    """
    Affiche le ticket de caisse avec tous les détails.
    
    nom_ticket: Nom du ticket
    nom_serveur: Nom du serveur
    ticket: Dictionnaire contenant les détails de chaque article commandé
    """
    assert(type(nom_ticket)) == str
    assert(type(nom_serveur)) == str
    print(f'''
{nom_ticket}
Ticket numéro : {randint(0,3000)}

Date : {datetime.date.today().strftime("%d/%m/%Y")}

Vous avez été servi par : {nom_serveur}
''')

    print(f"{'NB':<8} {'Desc.':<20} {'HT unitaire':<15} {'TVA':<8} {'Total':<8}") # les ':<8' permettent de créer des colonnes avec un certains nombre de caractères

    total_ht = 0
    total_tva = 0
    total = 0

    for id_article, details in ticket.items():
        quantite, description, prix_ht, prix_tva, prix_total_tva, prix_total_ht = details
        total_ht += prix_total_ht
        total_tva += prix_tva * quantite
        total += prix_total_tva
        print(f"{quantite:<8} {description:<20} {prix_ht}€{' '*11} {int(prix_tva/prix_ht*100)}%{' '*5} {prix_total_tva:.1f}€")

    print(f"\n{' '*44}Total HT{' '*4}{total_ht:.1f}€") # ici le {' '*4} indique le nombre d'espace à ajouter
    print(f"{' '*44}Total TVA{' '*3}{total_tva:.1f}€")
    print(f"{' '*44}Total{' '*7}{total:.1f}€")

if __name__ == "__main__":
    print(len(sys.argv)) == 4
    # Afficher les items :
    print(f"{'Code article':<20} {'Description':<20} {'Prix unitaire hors taxe':<25}")

    for codeArticle, (description, prix) in dict.items():
        print(f"{codeArticle:<20} {description:<20} {prix:<25}")

    # Traiter la commande
    articles = sys.argv[3].split("|")
    ticket = parser_articles(dict, articles)
    afficher_ticket(sys.argv[1], sys.argv[2], ticket)
