import sys
from typing import List, Dict

# Fonctions

def ParseArgs(arguments: list) -> tuple:
    """Fonction qui retourne un tuple avec le nom du magasin, le nom de la caisière et la quantité de chaque item
    @args: arguments: list -> La liste des arguments
    @return: tuple -> un tuple avec le nom du magasin, le nom de la caisière et la quantité de chaque item
    """
    # Initialisation des variables
    magasin: str
    caisiere: str
    liste_produits: List[str]
    dict_produits: Dict[str]

    if len(arguments) < 3:
        # Contrôle du nombre d'arguments dans la saisie utiliisateur
        print(USAGE)
    else:
        try:
            magasin = arguments[1]
            caisiere = arguments[2]
            liste_produits = str(arguments[3]).split("|")
        except TypeError as e:
            print(f"ERREUR: Entrées de mauvais type ({e})")

        dict_produits = {}
        for item in liste_produits:
            reference = str(item).split(":")[0]
            quantite = str(item).split(":")[1]
            dict_produits[reference] = quantite

    return magasin, caisiere, dict_produits

# Déclaration des variables
USAGE: str
items: dict
magasin: str
caisiere: str
dict_produits: dict

# Définition des variables
items = {"C01": ["Pack de coca", 5], 
         "C02": ["Kilo de pomme de terre", 1],
         "C03": ["Pack de biscottes", 2],
         "C04": ["Café soluble", 3],
         "C05": ["Crackers", 4]
         }

# Récupération des paramètres
USAGE = "Utilisation: python main.py [NOM DU MAGASIN] [CAISIERE] [REF:NOMBRE|REF:NOMBRE|...]"
arguments = sys.argv

# Contrôle de la saisie et retour des variables
magasin, caisiere, dict_produits = ParseArgs(arguments=arguments)

print(magasin)
print(caisiere)
print(dict_produits)