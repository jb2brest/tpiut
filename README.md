# Système édition ticket de caisse

## Description

Programme qui permet de générer un ticket en affichant les différents informations d'un article.

## Fonctionnalités

Ce programme permet la création de tickets de caisse détaillés avec des informations sur les articles achetés, les prix, les taxes, etc. La possibilité d'ajouter des articles, de les supprimer et de les modifier avant d'afficher le résultat.

## Utilisation du programme

Assurez-vous d'avoir Python installé sur votre système.
Exécutez le fichier principal `main.py` en ligne de commande pour lancer le programme.

Voici l'usage et un exemple :

usage : `python3 main.py <market_name> <seller_name> <cart>`

exemple : `python3 main.py "But Maket" "Lisa" "C01:10|C02:3"`

Voici la tableau récapitulatif des produits intégré au système par défaut :

| Code article | Description  | Poids ou volume unitaire | Prix HT unitaire | TVA | Origine    |
|--------------|--------------|--------------------------|------------------|-----|------------|
|C01           | pack de coca | 2Kg                      | 5                | 20% | Lituanie   |
|C02           | kilo de pdt  | 1Kg                      | 1                | 10% | Espagne    |
|C03           | pack Biscotte| 950g                     | 2                | 10% | France     |
|C04           | Café soluble | 250g                     | 3                | 10% | Roumanie   |
|C05           | Crakers      | 125g                     | 4                | 20% | Angleterre |
|C06           | Eau          | 1.5L                     | 6                | 10% | Suisse     |
|C07           | Pain         | 250g                     | 1                | 10% | France     |

## Explication du programme

1) L'algorithme va tout d'abord transformer la CLI en dictionnaire.
2) Les données sont mis à jour avec data.py
3) Les données sont ensuite passé dans le fichier ticket.py pour générer le ticket
4) Le ticket est ensuite récupéré en chaîne de caractère et est affiché.

Chaque ticket présente plusieurs informations :

-> NB 
-> Desc.   
-> Pds/vol. unitaire  
-> Pds/vol.
-> total 
-> Orig.  
-> HT unitaire  
-> TVA Total
