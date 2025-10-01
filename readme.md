# Documentation du code
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
Ticket numéro : 39 

Date : 01/10/2025

Vous avez été servi par : Lisaf

NB   Desc.           HT unitaire     TVA     Total
1    Crackers       4         10%         4.4
5    Café soluble       3         10%         16.5


Total HT 19
Total TVA 1.9
Total 20.9
```
## Liste des produits disponible et ajout de nouveau article
#### Article actuellement disponible par défaut
| Code article  | Description  |  Prix HT unitaire |
|---|---|---|
| C01  | Pack de coca  | 5  |
| C02  | kilo de pdt  | 1  |
| C03  | pack Biscotte  | 2  |
| C04  | Café soluble  | 3  |
| c05  | Crackers  | 4  |

### Comment ajouter un article
il faut modifier cette partie du code :
```python
lst_item = {"C01":{"nom":"pack de coca","prix":5},
            "C02":{"nom":"kilo de pdt","prix":1},
            "C03":{"nom":"pack Biscotte","prix":2},
            "C04":{"nom":"Café soluble","prix":3},
            "C05":{"nom":"Crackers","prix":4}}
```
Et rajouter cette ligne type (en la modifiant):
``` python
"C06":{"nom":"produit","prix":0}
```
n'oubilez pas de rajouter la virgule sur l'avant dernière article