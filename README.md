# tpiut
TP sur la gestion de projet niveau IUT

L'objectif du programme main.py est un systeme d'édition de ticket de caisse.

Le programme prends 3 paramètres en entrés.

Le premier est le nom du supermarché (Exemple : "BUT Market").

Le deuxième est le nom du vendeur(Exemple :"Lisa").

Le troisième paramètre on rentre les produits que l'on veut ajouter ainsi que leur nombre en vous référent au tableau ci dessous.

![Image tableau](/tableau_produits.png "produits").

Dans les mêmes guillemets on commence par mettre le code de l'article et son nombre séparé de 2 points (:). Exemple: "C01:10"

Il est possible d'accumuler les produits en les séparants d'un "pip" (ALT GR 6). Exemple: "C01:10|C03:3"

Ainsi tout d'abord il va falloir télécharger l'ensemble des fichiers ici présent.

Pour ouvrir et exécuter le fichier vous pouvez utiliser le logiciel Visual Studio Code. 

Il peut être téléchargé à l'aide de ce lien, bien choisir l'OS sur lequel est votre machine : https://code.visualstudio.com/download

Ensuite, ouvrir Visual Studio Code aller dans file en haut à gauche puis open folder et choisir le dossier dans lequel ce trouve les fichier téléchargés.

Puis ouvrir un terminal en allant dans terminal en haut puis new terminal.

Ne pas oublier de vérifier d'être bien placé dans le dossier ou ce trouve le programme avant de l'éxécuter à l'aide du chemin afficher dans le terminal.

Si vous n'êtes pas au bonne endroit, vous pouvez exécuter la commande suivante : cd /le chemin du répertoire ou ce trouve les fichiers.

Puis exécuter le programme avec la commande suivante: python3 .\main.py

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


