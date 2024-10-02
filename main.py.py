from typing import List
import sys

def ajout_produits(code:str, description:str, prix: int, produits:dict, ):
    produit: List = [description, prix]
    produits[code] = produit
    return produits



if __name__ == "__main__" :

    # Déclaration des variables
    produits: dict

    # Définition des variables
    produits = {"C01": ["Pack de coca", 5], "C02": ["Kilo de pomme de terre", 1], "C03": ["Pack de biscottes", 2], "C04": ["Café soluble", 3], "C05": ["Crackers", 4]}
    name_magasin = sys.argv[0] #variable de récupération du premier paramétre
    name_vendeur = sys.argv[1] #variable de récupération du deuxiéme paramétre
    course: List = sys.argv[2] #variable de récupération du troisiéme paramétre
    course_list = course.split('|') #list de tous les produits du troisiéme paramétre
    total: float = 0 #variable servant au total du payement sans la tva
    total_tva: float = 0 #variable servant au total du payement avec la tva
    tva_total: float = 0 #variable servant au du prix liée à la tva
    for element in course_list:
        tva:float = 0 #variable servant à la tva du produits
        prix_produits:float = 0 #variable au prix total du produit
        element.split(':') #séparation du produit et du prix
        name_produit = str(produits[element.split(':')[0]]) #récupération du nom du produits dans le dictionnaire
        nb_produit = float(element.split(':')[1]) #récupération du nombre de produits acheter
        prix = float(produits[element.split(':')[1]]) #récupération du prix du produits dans le dictionnaire
        prix_produits = nb_produit * prix #calcul 
        tva = (nb_produit * prix)*0.1
        tva_total = tva_total + tva
        total = total + prix_produits
        total_tva = total_tva + prix_produits + tva


