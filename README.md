# Tutoriel d'utilisation du Système d'Édition de Ticket de Caisse

## Étape 1 : Télécharger le code
Tout d'abord, assurez-vous d'avoir téléchargé le code du projet depuis le référentiel Git ou le dossier où il est stocké.


## Étape 2 : Prérequis
Assurez-vous que vous avez Python 3 installé sur votre système. Vous pouvez vérifier cela en ouvrant un terminal et en exécutant la commande suivante :
```bash
python3 -–version
```

Résultats de commande si c'est bon.
```bash
Python 3.11.6
```

Si Python 3 n'est pas installé, vous pouvez le télécharger à partir du site officiel de Python : https://www.python.org/downloads/.


## Étape 3 : Exécuter le programme
Ouvrez un terminal (ou une invite de commande) et accédez au répertoire où vous avez téléchargé les fichiers du projet.

Exemple : 
```bash
cd "/chemin au se situe le code"
```

Utilisez la commande suivante pour exécuter le programme principal :
bash
python3 main.py "Nom du magasin" "Nom du caissier" "Liste des articles"
    • "Nom du magasin" est le nom de votre magasin.
    • "Nom du caissier" est le nom du caissier.
    • "Liste des articles" est une liste d'articles que vous souhaitez ajouter au ticket, au format "CodeArticle:Quantité|CodeArticle:Quantité". Par exemple, "C01:10|C02:2" signifie 10 packs de coca (C01) et 2 kilos de pommes de terre (C02).

Exemple : 
```bash
Python3 main.py “But Maket” “Lisa” “C01:10|C02:2”
```

## Étape 4 : Visualiser le ticket
Après avoir exécuté la commande, le programme générera un ticket au format spécifié et l'affichera dans la console. Vous verrez le nom du magasin, le numéro de ticket, la date, le nom du caissier, la liste des articles avec leurs détails, ainsi que les totaux HT, TVA et le total général.


## Étape 5 : Personnalisation
Vous pouvez personnaliser le programme en ajoutant de nouveaux articles ou en modifiant les articles existants dans le code source. Vous pouvez également ajouter des fonctionnalités supplémentaires au système selon vos besoins.


## Étape 6 : Ajouter de nouveaux articles

Pour personnaliser votre système et ajouter de nouveaux articles, suivez ces étapes :

- Ouvrez le fichier main.py dans votre éditeur de code.

- Recherchez la section du code où les articles existants sont définis. Vous devriez avoir une structure similaire à ceci :

```python

articles = {
    "C01": Article("C01", "pack de coca", 5, 10),
    "C02": Article("C02", "kilo de pdt", 1, 10),
    "C03": Article("C03", "pack Biscotte", 2, 10),
    # Ajoutez d'autres articles ici si nécessaire
}
```

- Pour ajouter un nouvel article, ajoutez une nouvelle ligne dans le dictionnaire articles. Par exemple, pour ajouter un "Café soluble" à 3€ HT avec une TVA de 10%, vous pouvez ajouter la ligne suivante :

```python

"C04": Article("C04", "Café soluble", 3, 10),
```
