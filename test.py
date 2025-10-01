import sys
import datetime


# Option 1: Dictionnaire avec code article comme clé
bdd = {
    "C01": {"description": "pack de coca", "prix": 5},
    "C02": {"description": "kilo de pdt", "prix": 1},
    "C03": {"description": "pack Biscotte", "prix": 2},
    "C04": {"description": "Café soluble", "prix": 3},
    "C05": {"description": "Crakers", "prix": 4}
}

try:
    nom_magasin = str(sys.argv[1])
except:
    print("Erreur: Veuillez entrer un nom de magasin valide.")
    exit()
try:
    serveur = str(sys.argv[2])
except:
    print("Erreur: Veuillez entrer un nom de serveur valide.")
    exit()
articles = sys.argv[3].split("|")

articles_dict = {}
print(articles_dict)
for article in articles :
    code, qnt = article.split(":")

    try:
        bdd[code]
    except KeyError:
        print(f"Erreur: Le code article '{code}' n'existe pas dans la base de données.")
        exit()
    try:
        qnt = int(qnt)
    except ValueError:
        print(f"Erreur: La quantité '{qnt}' n'est pas un nombre valide.")
        exit()
        
    articles_dict[code] = qnt


def calcul_resultat(dico: dict, articles:dict) -> tuple:
    prix:list = []
    liste_prix:list = []
    total = 0
    TVA_total = 0
    
    for article in articles.keys():
        if article in dico:
            quantite = articles[article]
            prix_unitaire = dico[article]["prix"]
            prix_total_ht = prix_unitaire * quantite
            tva_montant = prix_total_ht * 0.1
            prix=[article, quantite, prix_unitaire, prix_total_ht, tva_montant]
            liste_prix.append(prix)
            total += prix_total_ht
            TVA_total += tva_montant
    
    return liste_prix, total, TVA_total

def affichage(articles: dict, bdd: dict) -> str:
    # Utiliser la fonction calcul_resultat
    liste_prix, total_ht, total_tva = calcul_resultat(bdd, articles)
    total_ttc = total_ht + total_tva
    
    print(nom_magasin)
    print(f"Ticket numéro : 2200")
    print()
    print(f"Date : {datetime.date.today().strftime('%d/%m/%Y')}")
    print()
    print(f"Vous avez été servi par : {serveur}")
    print()
    
    print(f"{'NB':<6} {'Description':<15} {'HT unitaire':<12} {'TVA':<6} {'Total':<8}")
    
    # Utiliser les données calculées par calcul_resultat
    for prix_info in liste_prix:
        article_code = prix_info[0]
        quantite = prix_info[1]
        prix_unitaire = prix_info[2]
        prix_total_ht = prix_info[3]
        total_ligne_ttc = prix_total_ht * 1.1
        
        print(f"{quantite:<6} {bdd[article_code]['description']:<15} {prix_unitaire}€{'':<10} {'10%':<6} {total_ligne_ttc:.1f}€")
    
    print()
    # Afficher les totaux calculés par calcul_resultat
    print(f"{'':<26}{'Total HT':<9} : {total_ht:>8.2f}€")
    print(f"{'':<26}{'Total TVA':<9} : {total_tva:>8.2f}€")
    print(f"{'':<26}{'Total TTC':<9} : {total_ttc:>8.2f}€")

affichage(articles_dict, bdd)
    
# res=calcul_resultat(articles, articles_dict)
# affichage(res)