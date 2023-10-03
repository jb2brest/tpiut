# tpiut
TP sur la gestion de projet niveau IUT

# Prérequis

Avoir une machine sous un système d'exploitation Windows ou Linux
Avoir le package Python d'installer sur la machine

# Utilisation du produit

Déplacer le produit dans un dossier que vous retrouverez exemple Documents.

Ouvrir un terminal

Lancer la commande "python3 BUT_MARKET <nom_magasin> <serveur> <articles>"
-> les variables entre <> sont à modifier selon votre besoin. Par exemple pour le magasin "BUT_MARKET", pour serveur "Lisa".
Les articles seront à mettre de la façon suivante: "<num_article>:<quantité>|<num_article2>:<quantité2>|...

Exemple d'une commande "python3 BUT_Market "BUT Market" "Lisa" "C01:10|C02:2|C05:4"

Voici le résultat que vous obtenez :

BUT Market
Ticket numéro : 2

Date : 2023-10-03 11:05:18

Vous avez été servi par : Lisa

Code	Desc.			HT unitaire	Total
10	pack de coca		5€		50.0€
2	pack Biscotte		2€		4.0€
4	Crakers		4€		16.0€

				Total HT	70.0€
				Total TVA	7.0€
				Total		77.0€

# Ajout d'un produit 
Dans articles_info: ajouter une ligne de la façon suivante
"<num_article>": {"description": "<nom_article>", "prix_unitaire_ht": <prix>}

Exemple: 
"C06":{"description": "Chips", "prix_unitaire_ht": 3}

