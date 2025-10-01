# Option 1: Dictionnaire avec code article comme clé
bdd = {
    "C01": {"description": "pack de coca", "prix": 5},
    "C02": {"description": "kilo de pdt", "prix": 1},
    "C03": {"description": "pack Biscotte", "prix": 2},
    "C04": {"description": "Café soluble", "prix": 3},
    "C05": {"description": "Crakers", "prix": 4}
}

# Option 2: Liste de dictionnaires
articles_liste = [
    {"code": "C01", "description": "pack de coca", "prix": 5},
    {"code": "C02", "description": "kilo de pdt", "prix": 1},
    {"code": "C03", "description": "pack Biscotte", "prix": 2},
    {"code": "C04", "description": "Café soluble", "prix": 3},
    {"code": "C05", "description": "Crakers", "prix": 4}
]




def affichage(liste: list) -> str:
    
    for i in liste:
        