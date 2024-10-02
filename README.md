# TP Gestion de Projet - Manuel d'utilisation

## Téléchargement des ressources:

Pour créer un ticket de caisse avec ce nouvel outil, vous devez tout d'abord télécherger l'ensemble des ressources à partir du dépot.
```
git clone https://github.com/jb2brest/tpiut.git
```

Si la commande <code>git</code> est indisponible, vous pouvez l'installer à partir d'<a href="https://git-scm.com/book/fr/v2/D%C3%A9marrage-rapide-Installation-de-Git">ici</a>.

Ensuite, déplacez vous dans le dossier du projet et changez de branche Git avec les commandes suivantes:
```
cd 2024-tpiut
git checkout 2024-Lannion-GA1-MARTIN-BEAUPEL
```

Ensuite, si vous effectuez la commande <code>dir</code> dans votre dossier courant vous devriez trouver le fichier <code>main.py</code>.
Si ce n'est pas le cas, recommencez les étapes présédentes.


## Utilisation de l'outil

L'utilisation se fait avec python3, si la version n'est pas installée sur votre ordinateur veuillez l'installer <a href="https://www.python.org/downloads/release/python-3127/">ici</a>.

Une fois installée, vous pouvez lancez le programme avec la commande suivante, en adaptant les paramètres:
```
python3 main.py [NOM DU MAGASIN] [CAISIERE] [REF:NOMBRE|REF:NOMBRE|...]
```

Exemple d'utilisation:
```
python3 main.py “But Maket” “Lisa” “C01:10|C02:2”
```

Exemple de résultat de la commande


## Ajout d'un produit

Pour ajouter un produit vous devez modifier le fichier présent dans le dossier [https://github.com/jb2brest/tpiut/blob/2024-Lannion-GA1-MARTIN-BEAUPEL/data/produits.csv](data/produits.csv) en rajoutant une ligne sous la forme:
```csv
Nom produit,Référence,Prix,TVA,Poids,Unité Poids
```

Exemple:
```
Pack de coca,C01,5,0.2,2,kg;
Kilo de pomme de terre,C02,1,0.1,1,kg
```

NOTE: Si deux produits possèdent la même référence, vous aurez un warning de ce type à l'éxécution du programme:
```
WARNING: La même référence est présente au moins deux fois. Le produit [NOM DU PRODUIT] n'a donc pas été pris en compte.
```
