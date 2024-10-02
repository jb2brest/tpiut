# Système d'édition de ticket de caisse

Ce programme permet l'édition de ticket de caisse de manière simple en mode console. 

# Lancement du programme 

Pour lancer le programme d'edition de ticket de caisse il suffit de télécharger le fichier main.py et de l'éxecuter en ligne de commande avec les bon paramètres pour pouvoir sortir le ticket de caisse. 

Voici un exemple du rendu d'un ticket avec la commande suivante : 
```
Python3 main.py “But Maket” “Lisa” “C01:1|C02:3|C03:4”
```
```
BUT Market
Ticket numéro : 2200

Date : 08/09/2023

Vous avez été servi par : Lisa

NB	Desc.			HT unitaire 	TVA	Total
1 	pack de coca	 	5€		10%	5,5€
3	kilo de pdt		    1€		10%	3,3€
4	pack Biscotte		2€		10%	8,8€

					Total HT	16€
					Total TVA	1,6€
					Total 		17,6€
```
Les nom des produits sont définis avec un code correspondant qu'on peut voir ci dessous : 
```
Code article                Description

C01                         pack de coca
C02                         kilo de pdt
C03                         pack Biscotte
C04                         Café soluble
C05                         Crakers
```
Pour renseigner par exemple 2 Crackers il suffit d'écrire "C05:02", pour ajouter un autre produit au ticket de caisse il faut les séparer par un |

# Fonctionnement

Le fonctionnement du code est le suivant : 

Nous avons une liste de produit insérer dans un dictionnaire qui fait office de base de données. Nous récuperons depuis les paramètres inséré : Le nom du magasin, le produit a ajouté, sa quantité et le nom de la personne qui a édité le ticket de caisse. 

une fois que tout les paramètres ont étés récupérés le programme va parcourir la liste des produits données en paramètres afin de récupérer les noms des produits, le nombre de produit et le prix des produits afin de calculer le prix total liés a ce produit en fonction de la TVA appliqué et ajouter ces valeurs au prix total de la commande afin de faire paraitre ce prix dans le ticket de caisse.  

# Ajouts de produits

Pour ajouter des nouveau produits il faut aller dans le programme et ajouter des produits manuellement dans le dictionnaire qui fait office de référence.

La syntaxe a respecté est la suivante : 

"C06": ["Brioches", 2]

Par exemple ici nous ajoutons la référence produit C06 pour des brioches qui vont coutés 2€
