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

## Explication du programme

1) L'algorithme va tout d'abord transformer la CLI en dictionnaire.
2) Les données sont mis à jour avec data.py
3) Les données sont ensuite passé dans le fichier ticket.py pour générer le ticket
4) Le ticket est ensuite récupéré en chaîne de caractère et est affiché.
