import sys, json
from datetime import date
from typing import List

def donnes_generales(title:str, server:str) -> None:
    # Incrémentation ticket - test si variable sauvegardée #
    try:
        with open("exec.json", "r") as f: 
            exec = json.load(f) # Récupération num ticket
    except:
        exec = 1
    
    # Affichage des informations générales du ticket #
    print(f"\n{title}\n")    
    print(f"Ticket numéro : {exec}")
    print(f"Date : {date.today()}\n")
    print(f"Vous avez été servi par : {server}\n")

    # Incrémentation ticket - Sauvegarde nouvelle incrémentation #
    exec += 1
    with open("exec.json", "w") as f:
        json.dump(exec, f)

def Ticket(liste_commande:List):

    #définition de la liste globale des produits et des variables importantes
    produits=(("Code article","Description","Prix HT unitaire"),("C01","pack de coca",5),("C02","kilo de pdt",1),("C03","pack Biscotte",2),("C04","Café soluble",3),("C05","crakers",4))
    tva = 0.1                                                                               #variable du pourcentage de tva
    glob = 0                                                                                #variable de prix total
    glob_Tva = 0                                                                            #variable de TVA total
    glob_HT = 0                                                                             #variable de prix HT total


    print(f"NB \t{produits[0][1]} \tprix HT\tTVA \tTotal")                                  #Print qui affiche la ligne des catégories du ticket
    for prod in liste_commande:                                                             #Boucle prenant en compte toutes les valeurs dans la liste var (données d'entrée)
        for produit in produits:                                                            #boucle prenant en compte touts les produits disponibles
            if prod[0] == produit[0]:                                                       #Comparateur de l'ID de chaque produit de VAR avec l'id des différents produits dispos pour trouver celui correspondant
                prix_item = produit[2] * int(prod[1]) + ((produit[2] * tva) * int(prod[1])) #Prix total de l'article prennant en compte le prix du produit, le nombre d'articles, et la TVA
                glob += prix_item                                                           #incrémentation du prix global des articles
                glob_HT += produit[2] * int(prod[1])                                        #incrémentation du prix global HT des articles
                glob_Tva += (produit[2] * tva) * int(prod[1])                               #incrémentation de la valeur totale de la tva
                print(f"{int(prod[1])} \t{produit[1]} \t{produit[2]}€ \t10% \t{prix_item}" )#Print qui affiche le nmbr d'article, la description du produit, son prix HT, le pourcentage de la tva et la valeur totale pour cet article
    print(f"\n\t\t\t    Total HT\t{glob_HT}")                                               # print de la valeur totale des article HT
    print(f"\t\t\t    Total TVA\t{glob_Tva:.2f}")                                           # print de la valeur totale de la TVA
    print(f"\t\t\t    Total\t{glob:.2f}")                                                   # print de la valeur totale des articles plus la TVA


if __name__=="__main__":
    titre:str = sys.argv[1] # Argument 1 de la commande de démarrage
    serveur:str = sys.argv[2]
    codes_nb_articles:str = sys.argv[3].split("|") 
    liste_commande:List[list] = []
    for valeur in codes_nb_articles:
        liste_commande.append(valeur.split(":")) # Listes de chaque article avec le nb commandé
    
    #print(liste_commande) # Listes de chaque article avec le nb commandé

    # params:list = [titre, serveur, codes_articles]

    donnes_generales(titre, serveur) # Affichage des données générales
    Ticket(liste_commande)