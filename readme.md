# Documentation du code
## Objectifs

Le programme doit prevoir les fonctionnalités suivantes:
- Demande du nom de la personne
- Demande du nom du magasin
- Demande de l'ajout des articles
- Générer un ticket de caisse prenant en compte les paramètres précédents

## Comment lancer le programme
Pour lancer le programme il faut rentrer la ligne suivante dans le terminal: \n
```bash
Python3 main.py '[Nom du magasin]' '[prenom]' '[Code_article1:quantite|Code_article2:quantite]'
```
Python3 main.py il s'agit du lancement du python main.py est le nom du python 


"BUT market" s'agit du nom du magasin les "" permette de dire que ce soit une chaine de caractère 


"Lisa" est le nom de la parsonne qui l'a servi
C01:10 les caractère avant les deux point s'agit du code produit après les : il s'agit du nombre de produit. Pour ajouté un autre produit il faut rajouté le | et refaire de même pour le second produit.

## Récupération du ticket de caisse
Après execution du programme, le ticket est imprimé dans la console 

Exemple de ticket :
```shell
But Maket mm44
Ticket numéro : 51 

Date : 01/10/2025

Vous avez été servi par : Lisaf

NB   Desc.          Poids/Volume unitaire Poids/Volume total HT unitaire     TVA     Total
1    Crackers       125g                    125.0g           4               20%         4.8
9    Café soluble       250g                    2.25kg           3               10%         32.4


Total HT 31
Total TVA 6.2
Total 37.2
```
## Liste des produits disponible et ajout de nouveau article
#### Article actuellement disponible par défaut
| Code article  | Description  |  Prix HT unitaire | Poid ou volume unitaire | TVA |
|---|---|---|---|---|
| C01  | Pack de coca  | 5  | 2kg  | 20%  |
| C02  | kilo de pdt  | 1  | 1kg  | 10%  |
| C03  | pack Biscotte  | 2  | 950g  | 10%  |
| C04  | Café soluble  | 3  | 250g  | 10%  |
| C05  | Crackers  | 4  | 125g  | 20%  |
| C06  | Eau  | 6 | 1.5L  | 10%  |
| C07  | Pain  | 1  | 250g  | 10%  |



### Comment ajouter un article
il faut modifier cette partie du code :
```python
lst_item = {"C01":{"nom":"pack de coca","prix":5,"Poids":"2kg","Origine":"Lituanie","TVA":"20","Poids_kg":2},
            "C02":{"nom":"kilo de pdt","prix":1,"Poids":"1kg","Origine":"Espagne","TVA":"10","Poids_kg":1},
            "C03":{"nom":"pack Biscotte","prix":2,"Poids":"950g","Origine":"France","TVA":"10","Poids_kg":0.95},
            "C04":{"nom":"Café soluble","prix":3,"Poids":"250g","Origine":"Roumanie","TVA":"10","Poids_kg":0.25},
            "C05":{"nom":"Crackers","prix":4,"Poids":"125g","Origine":"Angleterre","TVA":"20","Poids_kg":0.125},
            "C06":{"nom":"Eau","prix":6,"Poids":"1,5L","Origine":"Suisse","TVA":"10","Poids_kg":1.5},
            "C07":{"nom":"Pain","prix":1,"Poids":"250g","Origine":"France","TVA":"10","Poids_kg":0.250},}

```
Et rajouter cette ligne type (en la modifiant):
``` python
"C07":{"nom":"article","prix":0,"Poids":"0g","Origine":"France","TVA":"0","Poids_kg":0}
```
n'oubilez pas de rajouter la virgule sur l'avant dernière article