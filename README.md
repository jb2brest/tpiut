# tpiut

TP sur la gestion de projet niveau IUT

TRAVERS Gwenn - HENON Quentin

## Projet Ticket de caisse 

### Fonctionnement
"""
Ce programme généer une ticket de caisse en fonction des arguments passés en ligne de commande.

Les arguments a placé en ligne de commande sont les suivant:

le nom du magasin

le nom du vendeur

le numero associé aux articles -> C01:10|C02:2

### Lancement

Il faut renter dans le terminal ouvert à l'emplacement du fichier : python3 main.py <Magasin> <Vendeur> <Items ex: C01:2|C02:1>

Exemple d'exécution en ligne de commande :
    python3 main.py "But Market" "Lisa" "C01:2|C02:1|C03:3"
"""

Résultat attendu:

Le ticket de ciasse s'affiche dans le terminal

### Ajout d'un article

Chaque article est représenté par un dictionnaire avec :

- Un code de l’article.

- Le nom de l’article.

- Le prix HT

Liste des produit  ci dessous:
```Python

PRODUITS = {
    "C01": {"nom": "Coca Cola", "prix_ht": 5.00},
    "C02": {"nom": "kilo de pdt", "prix_ht": 1.00},
    "C03": {"nom": "pack Biscotte", "prix_ht": 2.00},
    "C04": {"nom": "Café soluble", "prix_ht": 3.00},
    "C05": {"nom": "Crackers", "prix_ht": 4.00},    
}
```
Pour ajouter un produit il faut utiliser le même format que ci dessous en lui atribuant un numero de produit unique un nom ainsi qu'un prix HT

Exemple :

"Id unique": {"nom": "mettre le nom d'un produit", "prix_ht": le prix en float}, 
