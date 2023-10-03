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

De plus, chaque erreur à un code, des exemple ci-dessous :

- erreur A2 -> "Erreur A2 : Le nom du magasin ne peut être vide"
- erreur A3 -> "Erreur A3 : Le nom de l'employé ne peut pas être vide"

## Utilisation

Pour pouvoir utiliser ce programme vous devez avoir installer python sur votre machine. Ensuite vous devez le lancer en ligne de commande, ci-dessous des exemple de comment utiliser ce programme.

Voici la syntaxe d'utilisation : `python3 ticket.py <"nom du magasin"> <"Nom du vendeur(euse)"> <"code_article:nombre_article|code_article2:nombre_article2">`

Voici un exemple d'utilisation : `python3 ticket.py "BUT MARKET" "Sarah" "C01:28|C04:57"`

Actuellement, voici la liste des articles qui sont renseignés par défaut :

|Code article|Description| Poids ou volume unitaire |Prix HT unitaire| TVA |
| :--------: | :-------: | :--: | :------------: | :--: |
|    C01     |pack de coca  | 2kg  | 5 | 20% |
|    C02     |kilo de pdt   | 1kg  | 1 | 10% |
|    C03     |pack Biscotte | 950g | 2 | 10%|
|    C04     |Café soluble  | 250g | 3 |10% |
|    C05     |Crakers       | 125g | 4 | 20% |
|    C06     |Eau           | 1,5L | 6 | 10% |
|    C07     | Pain         | 250g | 1 | 10% |

## Ajout d'un produit

Pour ajouter un produit, il faut l'ajouter dans la fonction itemParsing
On ajoute à la ligne dernière ligne ajoutée (/!\ ne pas ajouter avant/supprimer le case _:)
Exemple:
```py
case "C06":
                desc="Eau" # description du produit
                priceHT=6 # prix hors taxe
                priceTot=nb*(priceHT*TVA)
                poids=1500
```
## Fonctionnement du programme

Dans cette partie je vais vous expliquer comment le programme fonctionne et son déroulement:

1. récupère les paramètres fourni en ligne de commande
2. Sépare et traite les arguments fourni
3. Lien entre les code article fourni en paramètres et leurs informations stockés dans le programme
4. Sérialise les informations afin de pouvoir les affocher dans le ticket de caisse
5. Prépare l'affichage du ticket de caisse, met en forme toutes les informations préparé précédement
6. Affiche le ticket de caisse en vérifiant les potentiels erreurs
