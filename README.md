# tpiut

TP sur la gestion de projet niveau IUT

TRAVERS Gwenn - HENON Quentin

## Projet Ticket de caisse V1

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

liste_produits = {
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



## Projet Ticket de caisse V2


### Fonctionnement
"""
Ce programme fonctionne pratiquement comme le programme v1 :

Les arguments a placé en ligne de commande sont les mêmes:

le nom du magasin"""
Ce programme généer une ticket de caisse en fonction des arguments passés en ligne de commande.


le nom du vendeur

le numero associé aux articles -> C01:10|C02:2

### Lancement

Pour le lancement c'est exactement la mếme chose:
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

- le poids de l'article

- Le prix HT

- la TVA

- l'origine

Liste des produit ci dessous dont 2 ajoutés:
```Python

liste_produits = {
    "C01": {"nom": "pack de coca", "poids": "2kg", "prix_ht": 5.0, "tva": 0.20, "origine": "Lituanie"},
    "C02": {"nom": "kilo de pdt", "poids": "1kg", "prix_ht": 1.0, "tva": 0.10, "origine": "Espagne"},
    "C03": {"nom": "pack Biscotte", "poids": "950g", "prix_ht": 2.0, "tva": 0.10, "origine": "France"},
    "C04": {"nom": "Café soluble", "poids": "250g", "prix_ht": 3.0, "tva": 0.10, "origine": "Roumanie"},
    "C05": {"nom": "Crakers", "poids": "125g", "prix_ht": 4.0, "tva": 0.20, "origine": "Angleterre"},
    "C06": {"nom": "Eau", "poids": "1,5L", "prix_ht": 6.0, "tva": 0.10, "origine": "Suisse"},
    "C07": {"nom": "Pain", "poids": "250g", "prix_ht": 1.0, "tva": 0.10, "origine": "France"},
}

```
Pour ajouter un produit il faut utiliser le même format que ci dessous en lui atribuant un numero de produit unique un nom ainsi qu'un prix HT

Exemple :

"Id unique": {"nom": "mettre le nom d'un produit", "poids": "le poids en kilo / grammes / litres", "prix_ht": "le prix en float", "tva": "la valeur de la TVA entre 0 et 1", "origine": "Le pays d'origine de l'atrticle"}
