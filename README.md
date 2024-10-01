# tpiut
TP sur la gestion de projet niveau IUT

L'objectif du programme main.py est un systeme d'édition de ticket de caisse.

Le programme prends 3 paramètres en entrés.

Le premier est le nom du supermarché (Exemple : "BUT Market").

Le deuxième est le nom du vendeur(Exemple :"Lisa").

Le troisième paramètre on rentre les produits que l'on veut ajouter ainsi que leur nombre en vous référent au tableau ci dessous.

![Image tableau](/tableau_produits.png "produits").

Ne pas oublier de ce placer dans le dossier du programme avant de l'éxécuter.
Exemple d'éxécution

```python
python3 .\main.py   "But Maket" "Lisa" "C01:10|C02:2" 

```

Résultat:
```python
But Maket
Ticket numéro : 16 

Date : 01/10/2024

Vous avez été servi par : Lisa

+----+--------------+-------------+-----+-------+
| NB | Desc.        | HT unitaire | TVA | Total |
+----+--------------+-------------+-----+-------+
| 10 | pack de coca | 5           | 10% | 55.0  |
+----+--------------+-------------+-----+-------+
| 2  | kilo de pdt  | 1           | 10% | 2.2   |
+----+--------------+-------------+-----+-------+
                                  Total HT : 52 €
                               Total TVA : 13.2 €
                                   Total : 57.2 €
```


