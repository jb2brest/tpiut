import sys
from typing import List, Dict
import csv

# Fonctions

def ParseArgs(arguments: list) -> tuple:
    """Fonction qui retourne un tuple avec le nom du magasin, le nom de la caisière et la quantité de chaque item
    @args: arguments: list -> La liste des arguments
    @return: tuple -> un tuple avec le nom du magasin, le nom de la caisière et la quantité de chaque item
    """
    # Initialisation des variables
    magasin: str = ""
    caisiere: str = ""
    liste_produits: List[str] = []
    dict_produits: Dict[str] = {}
    error: bool = False

    if len(arguments) < 3:
        # Contrôle du nombre d'arguments dans la saisie utiliisateur
        error = True
    else:
        try:
            magasin = arguments[1]
            caisiere = arguments[2]
            liste_produits = str(arguments[3]).split("|")
        except TypeError as e:
            print(f"ERREUR: Entrées de mauvais type ({e})")
        except Exception as e:
            error = True
        
        try:
            dict_produits = {}
            for item in liste_produits:
                reference = str(item).split(":")[0]
                quantite = str(item).split(":")[1]
                dict_produits[reference] = quantite
        except IndexError as e:
            error = True

    return error, magasin, caisiere, dict_produits

# Déclaration des variables
USAGE: str
items: dict
magasin: str
caisiere: str
dict_produits: dict

# Définition des variables
items = {}
with open('data/produits.csv', newline='\n', encoding="utf-8") as csvfile:
    # Boucle pour récupérer tout les produits dans le fichier csv
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        nom = row[0] # Nom du produit
        reference = row[1] # Référence du produit
        prix = row[2] # Prix du produit

        if reference in items.keys():
            print(f"WARNING: La même référence est présente au moins deux fois. Le produit {nom} n'a donc pas été pris en compte.")
        else:
            items[reference] = [nom, prix]

# Récupération des paramètres
USAGE = "Utilisation: python3 main.py [NOM DU MAGASIN] [CAISIERE] [REF:NOMBRE|REF:NOMBRE|...]"
arguments = sys.argv

# Contrôle de la saisie et retour des variables
error, magasin, caisiere, dict_produits = ParseArgs(arguments=arguments)

# Si il n'y a pas eu d'erreurs de l'utilisateur sur la saisie des données
if not error:
    print(magasin)
    print(caisiere)
    print(dict_produits)
else:
    print(USAGE)