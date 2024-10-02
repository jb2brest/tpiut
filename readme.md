

<!-- 
Groupe 3A1
BOEZ Lucas
CHICHEPORTICHE Axel

TP Cycle De Vie D'Un Projet

La documentation permettre de comprendre comment utiliser notre produit (lancement, fonctionnement, ajout de produits,...)

lot 3 -->

**<h1>Fonctionnement d'un programme de génération de ticket </h1>**

**<h2>1 : Description du programme</h2>**


L'objectif du programme `"main.py"` est la réalisation d'un programme d'un systeme d'édition de ticket de caisse.


Pour permettre la compréhension de notre documentation, nous allons utiliser l'exemple d'une commande d'exécution du programme suivant :
```python
python3 .\main.py "But Maket" "Lisa" "C01:10|C02:2" 
```
(si il y a une erreur **"Python est introuvable. ExÚcutez sans argument pour procÚder Ó l"** utiliser `py` à la place de `python3`)

Le programme prends en compte 3 variables en entrée.

La première est le nom du supermarché, ici `"BUT Market"`. La deuxième est le nom du vendeur `"Lisa"` et pour la troisième, on rentre les `"items"` que l'on veut ajouter ainsi que la quantité. Pour la troisième variable, on reprend les items dans le tableau ci dessous :


**<h2>2 : Exécution du programme</h2>**


Pour pouvoir exécuter le programme, vous devez au préalable posséder un logiciel d'éditeur de code comme Vscode, Thonny, Spider, ...
Dans notre cas nous allons détailler la façon de faire sur VS Code.

Après avoir lancé l'application, pour que se soit plus simple, vous pouvez ouvrir le dossier dans lequel ce trouve les fichiers téléchargés avec l'onglet `"File"` en haut à gauche puis `"Open folder"` et choisir le dossier.

Maintenant que le dossier est ouvert, vous devez vous déplacer dans le fichier `"main.py"`. A partir de là, vous pouvez ouvrir un terminal où vous pourrez exécuter le programme.

Pour cela, il vous suffit simplement de cliquer sur `"Terminal` puis `"New Terminal"`.
Ensuite, vous pouvez commencer à tester le code. Pour pouvoir le faire, vous devez saisir dans le terminal les commandes suivantes :

**Attention !**

Ne pas oublier de vérifier d'être bien placé dans le dossier ou ce trouve le programme avant de l'éxécuter à l'aide du chemin afficher dans le terminal.

```python
py3.\main.py   "But Maket" "Lisa" "C01:10|C02:2" 

Le résultat qui doit être renvoyé est le suivant :

Résultat:

But Maket
Ticket numéro : 16 

Date : 01/10/2024

Vous avez été servi par : Lisa


 NB Desc.         HT unitaire  TVA  Total 
 10  pack de coca  5            10% 55.0  
 2   kilo de pdt   1            10%  2.2   

Total HT : 52 €
Total TVA : 13.2 €
Total : 57.2 €

```


**<h3> Annexe : AJOUT D'UN ARTCILE DANS LE CATALOGUE**

Pour rajouter un article, il faut suivre la même syntaxe que le tableau, il faut juste changer l'identifiant, ce dernier doit etre unique.  

Si l'on veut rajouter l'article amongus à 69€, faisant 2 Kg avec une TVA de 0% d'origine France, il faut ajouter cette ligne à la fin du dictionnaire :

"identifiant de la ligne du dessous + 1 ": {"description": "amongus", "poids_volume": "2kg", "prix": 69, "tva": 0.10, "origine": "France"}

**Attention !**
Ne pas enlever le ``"}"` à la fin du dictionnaire.


Exemple :
```python
"C01": {"description": "pack de coca", "poids_volume": "2kg", "prix": 5, "tva": 0.20, "origine": "Lituanie"},
"C02": {"description": "kilo de pdt", "poids_volume": "1kg", "prix": 1, "tva": 0.10, "origine": "Espagne"},
"C03": {"description": "pack Biscotte", "poids_volume": "950g", "prix": 2, "tva": 0.10, "origine": "France"},
"C04": {"description": "Café soluble", "poids_volume": "250g", "prix": 3, "tva": 0.10, "origine": "Roumanie"},
"C05": {"description": "Crakers", "poids_volume": "125g", "prix": 4, "tva": 0.20, "origine": "Angleterre"},
"C06": {"description": "Eau", "poids_volume": "1,5L", "prix": 6, "tva": 0.10, "origine": "Suisse"},
"C07": {"description": "amongus", "poids_volume": "2kg", "prix": 69, "tva": 0.10, "origine": "France"},
}
```


# Liste des articles
articles = {
    "C01": {"description": "pack de coca", "poids_volume": "2kg", "prix": 5, "tva": 0.20, "origine": "Lituanie"},
    "C02": {"description": "kilo de pdt", "poids_volume": "1kg", "prix": 1, "tva": 0.10, "origine": "Espagne"},
    "C03": {"description": "pack Biscotte", "poids_volume": "950g", "prix": 2, "tva": 0.10, "origine": "France"},
    "C04": {"description": "Café soluble", "poids_volume": "250g", "prix": 3, "tva": 0.10, "origine": "Roumanie"},
    "C05": {"description": "Crakers", "poids_volume": "125g", "prix": 4, "tva": 0.20, "origine": "Angleterre"},
    "C06": {"description": "Eau", "poids_volume": "1,5L", "prix": 6, "tva": 0.10, "origine": "Suisse"},
    "C07": {"description": "amongus", "poids_volume": "2kg", "prix": 69, "tva": 0.10, "origine": "France"},
}
