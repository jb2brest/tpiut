# Système de Gestion de Tickets de Caisse

## Description

Ce script Python permet de générer des tickets de caisse formatés à partir de commandes passées en ligne de commande. Il valide les entrées, calcule les totaux TTC avec TVA variable par produit, et enregistre le ticket dans un fichier texte.

## Fonctionnalités

- Validation des noms de magasin et de client
- Validation des commandes de produits
- Calcul automatique des prix TTC avec TVA variable (10% ou 20% selon le produit)
- Génération d'un ticket de caisse formaté avec poids/volume par produit
- Gestion d'un stockage prédéfini avec informations complètes (prix, TVA, poids/volume, origine)

## Prérequis

- Python 3.x
- Aucun module externe requis (utilise uniquement la bibliothèque standard)

## Utilisation

### Syntaxe de commande

```bash
python3 main.py "Nom_Magasin" "Nom_Client" "Commandes"
```
Exemple de commande : 

```bash
python3 main.py "But Market" "Lisa" "C01:1|C02:3"
```

### Arguments

1. **Nom_Magasin** : Nom du magasin (2-50 caractères)
2. **Nom_Client** : Nom du client/vendeur (2-30 caractères, lettres uniquement)
3. **Commandes** : Chaîne des commandes au format `C[numéro]:[quantité]|C[numéro]:[quantité]...`

### Règles de validation

- **Nom_Magasin** : 2 à 50 caractères
- **Nom_Client** : 2 à 30 caractères, contenant uniquement des lettres, espaces, tirets et apostrophes
- **Commandes** :
  - Format : `C[numéro]:[quantité]` (ex: C01:10)
  - Séparateur : `|` entre les commandes
  - Numéros de produits : Doivent exister dans le stockage
  - Quantités : Entre 1 et 999

### Stockage par défaut

Le script initialise automatiquement un stockage avec 7 produits conformes aux exigences :

- **C01**: pack de coca - 5.00€ HT - TVA 20% - 2kg - Lituanie
- **C02**: kilo de pdt - 1.00€ HT - TVA 10% - 1kg - Espagne  
- **C03**: pack Biscotte - 2.00€ HT - TVA 10% - 950g - France
- **C04**: Café soluble - 3.00€ HT - TVA 10% - 250g - Roumanie
- **C05**: Crackers - 4.00€ HT - TVA 20% - 125g - Angleterre
- **C06**: Eau - 6.00€ HT - TVA 10% - 1,5L - Suisse
- **C07**: Pain - 1.00€ HT - TVA 10% - 250g - France

### Structure des produits

Chaque produit contient les informations suivantes :
- **Code produit** : Identifiant unique (C01 à C07)
- **Description** : Nom du produit
- **Prix HT unitaire** : Prix hors taxes
- **Taux de TVA** : 10% ou 20% selon le produit
- **Poids/Volume** : Quantité unitaire du produit
- **Origine** : Pays d'origine du produit

Il est possible de modifier le stockage en éditant la fonction `initialiser_stockage_par_defaut()` dans le code source.

### Exemple d'ajout de produit :
```python
stockage_ajouter_produit("Pain", 1.0, 10.0, "250g", "France")
```

## Exemples

### Exemple valide

```bash
python3 main.py "BUT Market" "Lisa" "C01:1|C02:3|C03:4"
```

Génère un ticket pour :
- 1 pack de coca (2kg, TVA 20%)
- 3 kilos de pdt (3kg total, TVA 10%)  
- 4 packs Biscotte (3,8kg total, TVA 10%)

### Exemple avec erreur

```bash
python3 main.py "But" "Lisa" "C01:10|C99:1"
```

Affiche une erreur car le produit C99 n'existe pas dans le stockage.

### Affichage de l'aide

```bash
python3 main.py
```

Affiche l'usage et la liste des produits disponibles avec leurs détails complets.

## Sortie

- Le ticket est enregistré dans un fichier nommé `ticket_caisse_YYYYMMDD_HHMMSS.txt`
- Le nom du fichier généré est affiché dans la console
- Le ticket contient : 
  - En-tête avec nom du magasin, numéro de ticket, date et vendeur
  - Tableau des articles avec colonnes : NB, Desc., Poids/volume unitaire, Poids/volume total, HT unitaire, TVA, Total
  - Calcul automatique des poids/volumes totaux selon la quantité
  - Totaux HT, TVA et TTC avec TVA variable par produit

### Format du ticket généré

```
BUT Market
Ticket numéro : 1057

Date : 01/10/2025

Vous avez été servi par : Lisa

NB  Desc.           Poids/volume unitaire Poids/volume total HT unitaire  TVA   Total   
1   pack de coca    2kg                  2.0kg              5            20   % 6.00
3   kilo de pdt     1kg                  3.0kg              1            10   % 3.30
4   pack Biscotte   950g                 3.8kg              2            10   % 8.80

Total HT                                                     16€
Total TVA                                                    2.1€
Total                                                        18.1€
```

## Auteur

KLAPSIA Elie
BENIS-DELAHAYE Bastien

## Date

1 octobre 2025
