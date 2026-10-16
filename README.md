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
python3 main.py "Super U" "Alice" "C01:10|C02:2"
```

```
+--------------------------------------------------------+
| Super U                                                |
| Ticket numéro : 1                                      |
| Date : 16/10/2026                                      |
| Vous avez été servi par : Alice                        |
|                                                        |
| NB   Desc.                HT unitaire  TVA   Total TTC |
| 10   pack de coca         5,00 €       10%   55,00 €   |
| 2    kilo de pdt          1,00 €       10%   2,20 €    |
|                                                        |
|                                     Total HT : 52,00 € |
|                                     Total TVA : 5,20 € |
|                                    Total TTC : 57,20 € |
+--------------------------------------------------------+
```

## Fonctionnement

Le script vérifie d'abord les paramètres : il en faut 3, non vides, chaque code doit exister dans l'inventaire et chaque quantité doit être un entier supérieur à 0. Les codes peuvent être écrits en minuscules. S'il y a une erreur, un message s'affiche et le script s'arrête.

Le numéro du ticket est stocké dans le fichier index.txt. A chaque ticket on lit le numéro, on ajoute 1 et on le réécrit. Si le fichier n'existe pas il est créé et on commence à 1. Une commande qui finit en erreur ne change pas le numéro. Pour remettre le compteur à zéro il suffit de mettre 0 dans index.txt.

Pour les calculs :
- total TTC d'une ligne = prix HT x quantité x 1,10
- total HT = somme des prix HT x quantité
- total TVA = total HT x 0,10
- total TTC = total HT + total TVA

La TVA est de 10 %, on peut la changer avec la variable TVA en haut de main.py.

Les descriptions sont coupées à 20 caractères pour que les colonnes restent alignées. Si le nom du magasin ou du caissier est trop long, le ticket s'élargit.

## Ajouter un produit

Les produits sont dans le dictionnaire INVENTAIRE au début de main.py :

```python
INVENTAIRE = {
    "C01": {"description": "pack de coca", "prix_ht": 5.0},
    "C02": {"description": "kilo de pdt", "prix_ht": 1.0},
    "C03": {"description": "pack Biscotte", "prix_ht": 2.0},
    "C04": {"description": "Café soluble", "prix_ht": 3.0},
    "C05": {"description": "Crakers", "prix_ht": 4.0}
}
```

Pour ajouter un produit il suffit de rajouter une ligne, par exemple :

```python
    "C05": {"description": "Crakers", "prix_ht": 4.0},
    "C06": {"description": "Bouteille d'eau", "prix_ht": 0.8}
```

Attention à la virgule à la fin de la ligne d'avant, au code en majuscules et au prix avec un point et pas une virgule. Il n'y a rien d'autre à modifier, le produit est utilisable directement :

```
python3 main.py "Super U" "Alice" "C06:3"
```

## Remarque

Sous Windows les accents et le symbole € peuvent mal s'afficher dans le terminal. Dans ce cas on peut taper `chcp 65001` avant de lancer le script.
