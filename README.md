# Ticket de caisse

Script Python qui affiche un ticket de caisse à partir du nom du magasin, du nom du caissier et d'une liste d'articles.

LE GUEN Théo & SIMON Axel - 3A2

## Prérequis

Python 3 (pas de bibliothèque à installer).

## Lancement

Depuis le dossier du projet :

```
python3 main.py "Nom Magasin" "Nom Caissier" "C01:10|C02:2"
```

Sous Windows il faut mettre `python` à la place de `python3`.

Il faut 3 paramètres :
- le nom du magasin
- le nom du caissier
- la liste des articles au format CODE:QUANTITE, séparés par des |

Il faut bien mettre les guillemets autour de la liste d'articles, sinon le terminal prend le | pour un pipe.

Exemple :

```
python3 main.py "Super U" "Jean" "C01:2|C02:3|C06:1"
```

```
+-----------------------------------------------------------------------------------------+
| Super U                                                                                 |
| Ticket numéro : 4                                                                       |
|                                                                                         |
| Date : 16/10/2026                                                                       |
|                                                                                         |
| Vous avez été servi par : Jean                                                          |
|                                                                                         |
| NB    Desc.              Pds/vol. unitaire  Pds/vol. total   HT unitaire   TVA    Total |
| 2     pack de coca       2kg                4kg              5€            20%    12€   |
| 3     kilo de pdt        1kg                3kg              1€            10%    3,3€  |
| 1     Eau                1,5L               1,5L             6€            10%    6,6€  |
|                                                                                         |
|                                                                        Total HT :   19€ |
|                                                                       Total TVA :  2,9€ |
|                                                                           Total : 21,9€ |
+-----------------------------------------------------------------------------------------+
```

## Fonctionnement

Le script vérifie d'abord les paramètres : il en faut 3, non vides, chaque code doit exister dans l'inventaire et chaque quantité doit être un entier supérieur à 0. Les codes peuvent être écrits en minuscules. S'il y a une erreur, un message s'affiche et le script s'arrête.

Le numéro du ticket est stocké dans le fichier index.txt. A chaque ticket on lit le numéro, on ajoute 1 et on le réécrit. Si le fichier n'existe pas il est créé et on commence à 1. Une commande qui finit en erreur ne change pas le numéro. Pour remettre le compteur à zéro il suffit de mettre 0 dans index.txt.

Chaque produit a son propre taux de TVA (10 % ou 20 %), défini dans l'inventaire. Pour les calculs :
- total d'une ligne = prix HT x quantité x (1 + TVA du produit)
- total HT = somme des prix HT x quantité
- total TVA = somme des prix HT x quantité x TVA du produit
- total = total HT + total TVA

Le ticket affiche aussi le poids ou volume unitaire du produit et le poids/volume total (unitaire x quantité). Les montants sont affichés sans zéros inutiles (19€, 3,3€).

Les descriptions sont coupées à 18 caractères pour que les colonnes restent alignées.

Les totaux sont regroupés en bas à droite : les « : » sont alignés entre eux, ainsi que les montants (les « € » tombent dans la même colonne).

La largeur du ticket s'adapte à son contenu : le cadre fait la largeur de la ligne la plus longue (en général le tableau des articles), avec un minimum de 40 caractères (constante LARGEUR). Si le nom du magasin ou du caissier est trop long, le ticket s'élargit.

## Ajouter un produit

Les produits sont dans le dictionnaire INVENTAIRE au début de main.py :

```python
INVENTAIRE = {
    "C01": {"description": "pack de coca", "poids_vol": 2, "unite": "kg", "prix_ht": 5.0, "tva": 0.20},
    "C02": {"description": "kilo de pdt", "poids_vol": 1, "unite": "kg", "prix_ht": 1.0, "tva": 0.10},
    "C03": {"description": "pack Biscotte", "poids_vol": 950, "unite": "g", "prix_ht": 2.0, "tva": 0.10},
    "C04": {"description": "Café soluble", "poids_vol": 250, "unite": "g", "prix_ht": 3.0, "tva": 0.10},
    "C05": {"description": "Crakers", "poids_vol": 125, "unite": "g", "prix_ht": 4.0, "tva": 0.20},
    "C06": {"description": "Eau", "poids_vol": 1.5, "unite": "L", "prix_ht": 6.0, "tva": 0.10},
    "C07": {"description": "Pain", "poids_vol": 250, "unite": "g", "prix_ht": 1.0, "tva": 0.10}
}
```

Pour ajouter un produit il suffit de rajouter une ligne, par exemple :

```python
    "C07": {"description": "Pain", "poids_vol": 250, "unite": "g", "prix_ht": 1.0, "tva": 0.10},
    "C08": {"description": "Jus d'orange", "poids_vol": 1, "unite": "L", "prix_ht": 2.5, "tva": 0.10}
```

Attention à la virgule à la fin de la ligne d'avant, au code en majuscules et au prix, au poids et à la TVA avec un point et pas une virgule (0.20 pour 20 %). Il n'y a rien d'autre à modifier, le produit est utilisable directement :

```
python3 main.py "Super U" "Alice" "C08:3"
```
