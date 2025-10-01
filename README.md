# Système de Gestion de Tickets de Caisse

## Description

Ce script Python permet de générer des tickets de caisse formatés à partir de commandes passées en ligne de commande. Il valide les entrées, calcule les totaux TTC avec TVA, et enregistre le ticket dans un fichier texte.

## Fonctionnalités

- Validation des noms de magasin et de client
- validation des commandes de produits
- Calcul automatique des prix TTC avec TVA (fixée à 10%)
- Génération d'un ticket de caisse formaté dans un fichier .txt
- Gestion d'un stockage prédéfini de produits

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

Le script initialise automatiquement un stockage avec 10 produits :

- C01: pack de coca (5.00€)
- C02: kilo de pdt (1.00€)
- C03: pack Biscotte (2.00€)
- C04: Pain complet (1.50€)
- C05: Fromage de chèvre (4.20€)
- C06: Salade verte (1.80€)
- C07: Lait (1.20€)
- C08: Yaourts (3.50€)
- C09: Bananes (2.30€)
- C10: Pommes (2.80€)

## Exemples

### Exemple valide

```bash
python3 main.py "But Market" "Lisa" "C01:10|C02:2"
```

Génère un ticket pour 10 packs de coca et 2 kilos de pdt.

### Exemple avec erreur

```bash
python3 main.py "But" "Lisa" "C01:10|C99:1"
```

Affiche une erreur car le produit C99 n'existe pas.

### Affichage de l'aide

```bash
python3 main.py
```

Affiche l'usage et la liste des produits disponibles.

## Sortie

- Le ticket est enregistré dans un fichier nommé `ticket_caisse_YYYYMMDD_HHMMSS.txt`
- Le nom du fichier généré est affiché dans la console
- Le ticket contient : en-tête, liste des articles, totaux HT/TVA/TTC

## Auteur

KLAPSIA Elie
BENIS-DELAHAYE Bastien

## Date

1 octobre 2025
