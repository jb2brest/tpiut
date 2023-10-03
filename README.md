# Édition de ticket de caisse

## Description

Ce programme permet de générer un ticket de caisse, en affichant les différentes informations de l'article

## Fonctionnalités

Ce programme permet de créer des tickets de caisses détaillés avec toutes les informations qui concerne le produit en question. Les informations se trouvant sur le ticket sont les suivantes :

- Date du jour
- Nom de la personne qui nous a servi
- Nombre de produit achetés
- Description du produit
- Prix HT unitaire
- TVA
- Total du prix des articles avec TVA
- Total HT
- Total TVA
- Total HT + TVA

## Utilisation

Pour pouvoir utiliser ce programme vous devez avoir installer python sur votre machine. Ensuite vous devez le lancer en ligne de commande, ci-dessous des exemple de comment utiliser ce programme.

Voici la syntaxe d'utilisation : `python3 ticket.py <"nom du magasin"> <"Nom du vendeur(euse)"> <"code_article:nombre_article|code_article2:nombre_article2">`

Voici un exemple d'utilisation : `python3 ticket.py "BUT MARKET" "Sarah" "C01:28|C04:57"`

Actuellement, voici la liste des articles qui sont renseignés par défaut :

|Code article|Description|Prix HT unitaire|
| :--------: | :-------: | :------------: |
|    C01     |pack de coca  | 5 |
|    C02     |kilo de pdt   | 1 |
|    C03     |pack Biscotte | 2 |
|    C04     |Café soluble  | 3 |
|    C05     |Crakers       | 4 |

## Fonctionnement du programme

Dans cette partie je vais vous expliquer comment le programme fonctionne et son déroulement:

1.
2.
3.
4. 
