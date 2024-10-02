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
    produits = {"C01": ["Pack de coca", 5], "C02": ["Kilo de pomme de terre", 1], "C03": ["Pack de biscottes", 2], "C04": ["Café soluble", 3], "C05": ["Crackers", 4]}
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
        print("NB       Desc.                     HT unitaire     TVA     Total")
        total: float = 0 #variable servant au total du payement sans la tva
        total_tva: float = 0 #variable servant au total du payement avec la tva
        tva_total: float = 0 #variable servant au du prix liée à la tva
        for element in course_list:
            tva:float = 0 #variable servant à la tva du produits
            prix_produits:float = 0 #variable au prix total du produit
            element.split(':') #séparation du produit et du prix
            name_produit = str(produits[element.split(':')[0]][0]) #récupération du nom du produits dans le dictionnaire
            nb_produit = float(element.split(':')[1]) #récupération du nombre de produits acheter
            prix = float(produits[element.split(':')[0]][1]) #récupération du prix du produits dans le dictionnaire
            prix_produits = nb_produit * prix #calcul du prix total lié à ce produits
            tva = (nb_produit * prix)*0.1 #calcul de la tva lié à ce produits
            tva_total = tva_total + tva #calcul de la tva
            total = total + prix_produits # prix total de la recette
            total_tva = total_tva + prix_produits + tva # tva total lié à l'achat
            print(f"{nb_produit:<8} {name_produit:<25} {prix:<15} {tva:<7} {prix_produits}")
    
        print(f"\n                                               total ht     {total}")
        print(f"                                               total tva    {tva_total}")
        print(f"                                               total        {total_tva}")
    except :
        print("Erreur de syntaxe, impossible d'imprimer la suite du ticket")
