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
- Le troisième argument ("C01:10|C04:6") représente la liste des articles et leur quantité. Les articles sont répertoriés de la manière suivante :

```
Code article     Description       Prix unitaire HT
C01              Pack de coca      5 
C04              Café Soluble      3 
```

Par exemple, C01:10 correspond à 10 Packs de Coca

Une fois tout les paramètres donnés, le programme retourne un ticket de caisse :

```python
python .\main.py "BUT Market" "Lisa" "C01:10|C02:5"
BUT Market
Ticket numéro : 107
Date : 2023-10-04
Vous avez été servi par : Lisa

NB    Desc.            HT unitaire    TVA    Total
10    Pack de Coca        5€        10%    55.00€
5    Kilo de pdt        1€        10%    5.50€

                Total HT    55.00€
                Total TVA    5.50€
                Total        60.50€

```

## Ajout d'un produit dans la liste :

Pour ajouter un article dans la base existante, il suffit de la rajouter dans le fichier base_articles.json.

Exemple pour un nouvel article : Kilo de spaghetti

```json
/* base avant ajout */
{
"base": [ 
    {
    "C01": ["Pack de Coca", 5],
    "C02": ["Kilo de pdt", 1],
    "C03": ["Pack de Biscottes", 2],
    "C04": ["Cafe Soluble", 3],
    "C05": ["Crackers", 4]
    }
]

}
```

```json
/* base après ajout */
{
"base": [ 
    {
    "C01": ["Pack de Coca", 5],
    "C02": ["Kilo de pdt", 1],
    "C03": ["Pack de Biscottes", 2],
    "C04": ["Cafe Soluble", 3],
    "C05": ["Crackers", 4],
    "C06": ["Kilo de Spaghetti",1]
    }
]

}
```