from typing import List
import sys
from datetime import date

def ajout_produits(code:str, description:str, prix: int, produits:dict, ):
    produit: List = [description, prix]
    produits[code] = produit
    return produits



if __name__ == "__main__" :

    # Déclaration des variables
    produits: dict

    # Définition des variables
    produits = {"C01": ["Pack de coca","2 kg", 5, 20], "C02": ["Kilo de pomme de terre","1 kg", 1, 10], "C03": ["Pack de biscottes", "950 g",2, 10], "C04": ["Café soluble", "250 g", 3, 10], "C05": ["Crackers", "125 g",4, 20], "C06" : ["Eau","1,5 L", 6,10], "C07" : ["Pain","250 g", 1,10]}
    try:
        name_magasin = sys.argv[1] #variable de récupération du premier paramétre
        print(name_magasin)
        nb_ticket:int = 12
        print(f"Ticket numéro: {nb_ticket} \n")
        name_vendeur = sys.argv[2] #variable de récupération du deuxiéme paramétre
        print(f"Date : {date.today()} \n")
        print(f"Vous avez été servis par :{name_vendeur} \n")
        course: List = sys.argv[3] #variable de récupération du troisiéme paramétre
        course_list = course.split('|') #list de tous les produits du troisiéme paramétre
        print("NB       Desc.                     Pds/vol. unitaire       Pds/vol. total    HT unitaire     TVA     Total")
        total: float = 0 #variable servant au total du payement sans la tva
        total_tva: float = 0 #variable servant au total du payement avec la tva
        tva_total: float = 0 #variable servant au du prix liée à la tva
        for element in course_list:
            tva:float = 0 #variable servant à la tva du produits
            prix_produits:float = 0 #variable au prix total du produit
            element.split(':') #séparation du produit et du prix
            name_produit = str(produits[element.split(':')[0]][0]) #récupération du nom du produits dans le dictionnaire
            nb_produit = float(element.split(':')[1]) #récupération du nombre de produits acheter
            prix = float(produits[element.split(':')[0]][2]) #récupération du prix du produits dans le dictionnaire
            prix_produits = nb_produit * prix #calcul du prix total lié à ce produits
            tva = (nb_produit * prix)*0.1 #calcul de la tva lié à ce produits
            tva_total = tva_total + tva #calcul de la tva
            total = total + prix_produits # prix total de la recette
            total_tva = total_tva + prix_produits + tva # tva total lié à l'achat
            poids_unitaire = produits[element.split(':')[0]][1]
            poids_total = float(produits[element.split(':')[0]][1].split(' ')[0])*nb_produit
            unite = produits[element.split(':')[0]][1].split(' ')[1]
            print(f"{nb_produit:<8} {name_produit:<25} {poids_unitaire:<23} {poids_total:<2} {unite:<14} {prix:<15} {tva:<7} {prix_produits}")

        print(f"\n                                                                                    total ht     {total}")
        print(f"                                                                                    total tva    {tva_total}")
        print(f"                                                                                    total        {total_tva}")

    except:    
        print("Erreur de syntaxe, impossible d'impirmer la suite du ticket")


