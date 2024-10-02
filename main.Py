#──────────────────────────────────────────────────────────────────────────────────────────────────────────
#─────────────────────────────────────IMPORTATION DES BIBLIOTHEQUES────────────────────────────────────────
#──────────────────────────────────────────────────────────────────────────────────────────────────────────

import sys
from datetime import datetime 


#────────────────────────────────────────CREATION DU DICTIONNAIRE──────────────────────────────────────────

# Liste des articles
articles = {
    "C01": {"description": "pack de coca", "prix": 5},               #Chaque ligne correspond à un article
    "C02": {"description": "kilo de pdt", "prix": 1},                #l'identifiant doit être unique (C01, C02 ...),
    "C03": {"description": "pack Biscotte", "prix": 2},              #Pour rajouter un article, il faut suivre la même syntaxe
    "C04": {"description": "Café soluble", "prix": 3},
    "C05": {"description": "Crakers", "prix": 4}
}

#────────────────────────────────────────CREATION DE LA FONCTION──────────────────────────────────────────

def calculer_ticket(nom_magasin, employe, achats):
    """Fonction qui permet le calcul et l'affichage du ticket de caisse. Exemple : python3 main.py "Nom Magasin" "Employe" "Achats" """
    date : str= datetime.now().strftime("%d/%m/%Y")                  #on récupère la date du jour
    
    #création des differentes variables.
    ticket_numero : int = 2200
    taux_tva : float = 0.10                           
    total_ht : int = 0
    total_tva : int = 0
    total_ttc : int = 0

    print(nom_magasin,"\n Ticket numéro :", ticket_numero,"\n")
    print("Date :",date,"\n")
    print("Vous avez été servi par :",employe,"\n")
    print(f"{'NB':<3} {'Desc.':<20} {'HT unitaire':<15} {'TVA':<5} {'Total':<10}")
    
    for achat in achats:                                            #calcule le prix total pour chaque article
        code, quantite = achat.split(':')
        quantite = int(quantite)

        if code in articles:
            article = articles[code]
            prix_ht = article["prix"]
            total_article_ht = prix_ht * quantite
            tva = total_article_ht * taux_tva
            total_article_ttc = total_article_ht + tva

            total_ht += total_article_ht                             #calcul de la TVA etc
            total_tva += tva
            total_ttc += total_article_ttc

            print(f"{quantite:<3} {article['description']:<20} {prix_ht}€"
                  f"{' ':<10} {int(taux_tva * 100)}%  {total_article_ttc:.1f}€")

    print(f"\n{'Total HT':<30} {total_ht:.1f}€")                     #affichage du prix
    print(f"{'Total TVA':<30} {total_tva:.1f}€")
    print(f"{'Total':<30} {total_ttc:.1f}€")


#────────────────────────────────────────PROGRAMME PRINCIPAL──────────────────────────────────────────

if __name__ == "__main__":
    if len(sys.argv) != 4:                                          
        #on vérifie si le nombre d'argument rentré est bien égal à 4 (nom du script python, nom du magasin, vendeur ainsi que les produits)
        print('Utilisation : python3 main.py "Nom Magasin" "Employe" "Achats"')  #si ce n'est pas le cas, on affiche un exemple de commande 
        sys.exit(1)

    nom_magasin = sys.argv[1]                                  
    employe = sys.argv[2]
    achats = sys.argv[3].split("|")

    calculer_ticket(nom_magasin, employe, achats)
