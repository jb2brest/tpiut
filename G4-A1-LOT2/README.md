# BUT Market Ticket Maker

Ce programme permet de générer un ticket de caisse à l'aide des informations passées en paramètres.

Auteurs : Morvant Théo, Riou Théo


# Fichiers
Ce programme comporte 3 fichiers :
- main.py
- nb_tickets.txt
- base_articles.json


## Utilisation du programme :

Dans un premier temps, vérifiez que python est correctement installé sur votre machine.
Le programme prends en compte 3 paramètres :

```python
python .\main.py "BUT Market" "Lisa" "C02:10|C04:6"
```
- Le premier argument ("BUT Market") est une chaîne de caractères contenant de le nom du magasin
- Le deuxième argument ("Lisa") contient de le nom de l'hôte de caisse.
- Le troisième argument ("C01:10|C04:6") représente les achats et leur quantité. Par exemple, C01:10 correspond à 10 Packs de Coca

Tous les articles sont répertoriés de la manière suivante :

```
Code article  Description   Poid/Volume Unit.  Prix Unit. HT    TVA 
C01	          Pack de coca	2kg	               5	            1.20
C04	          Café soluble	250g	           3	            1.1

```

Les valeurs 1.20 et 1.10 sur la TVA représente le multiplicateur. 10% -> x1.1 et 20% -> x1.2


Une fois tout les paramètres donnés, le programme retourne un ticket de caisse :

```python
python .\main.py "BUT Market" "Lisa" "C01:10|C02:5"
BUT Market
Ticket numéro : 16
Date : 2023-10-04
Vous avez été servi par : Lisa

NB    Desc.            HT unitaire    TVA    Total
10    Pack de Coca            5€        20%    60.00€
5    Kilo de pdt            1€        10%    5.50€

                Total HT        55.00€
                Total TVA        5.50€
                Total        65.50€
                Total poids        5.00Kg

```

## Ajout d'un produit dans la liste :

Pour ajouter un article dans la base existante, il suffit de le rajouter dans le fichier base_articles.json.
Les articles sont à inscrire dans le format suivant :
```json
 "Code__Article": ["Nom_article", Volume_Unité, Prix_Unité_HT, TVA]
```
Exemple pour un nouvel article : Kilo de spaghetti

```json
/* base avant ajout */
{
"base":[ 
        {
            "C01": ["Pack de Coca", 2, 5, 1.2],
            "C02": ["Kilo de pdt", 1, 1, 1.1],
            "C03": ["Pack de Biscottes", 0.95, 2, 1.1],
            "C04": ["Cafe Soluble", 0.25, 3, 1.1],
            "C05": ["Crackers", 0.125, 4, 1.1],
            "C06": ["Eau", 1.5, 6, 1.1],
            "C07": ["Pain", 0.250, 1, 1.1]
        }
    ]
}
```

```json
/* base après ajout */
{
"base":[ 
        {
            "C01": ["Pack de Coca", 2, 5, 1.2],
            "C02": ["Kilo de pdt", 1, 1, 1.1],
            "C03": ["Pack de Biscottes", 0.95, 2, 1.1],
            "C04": ["Cafe Soluble", 0.25, 3, 1.1],
            "C05": ["Crackers", 0.125, 4, 1.1],
            "C06": ["Eau", 1.5, 6, 1.1],
            "C07": ["Pain", 0.250, 1, 1.1],
            "C08": ["Kilo de Spaghetti", 1, 1, 1.2]
        }
    ]
}
```