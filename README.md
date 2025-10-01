# Système de Génération de Tickets de Caisse

## Description

Ce projet est un système de génération de tickets de caisse développé en Python. Il permet de créer des tickets formatés avec calcul automatique des totaux HT, TVA et TTC.

## Fonctionnalités

- ✅ Génération de tickets de caisse formatés
- ✅ Calcul automatique des totaux (HT, TVA, TTC)
- ✅ Gestion d'une base de données d'articles avec poids et origine
- ✅ Affichage des poids unitaires et totaux (formatage automatique g/kg)
- ✅ Numérotation automatique et incrémentale des tickets
- ✅ Gestion de différents taux de TVA par produit
- ✅ Validation des données d'entrée
- ✅ Gestion des erreurs (codes articles invalides, quantités incorrectes)
- ✅ Affichage aligné des colonnes avec ligne de séparation
- ✅ Symbole euro (€) pour les prix

## Structure du Projet

```bash
tpiut/
├── main.py          # Script principal
├── test.py          # Version de test/développement
├── README.md        # Documentation (ce fichier)
└── étapes.txt       # Notes de développement
```

## Installation et Prérequis

### Prérequis

- Python 3.6 ou version supérieure
- Système d'exploitation : Windows, macOS, ou Linux

### Installation

1. Clonez ou téléchargez le projet
2. Aucune dépendance externe requise (utilise uniquement les modules Python standard)

## Utilisation

### Lancement du Programme

```bash
python main.py "<nom_magasin>" "<nom_serveur>" "<articles>"
```

### Paramètres

1. **nom_magasin** : Nom du magasin (entre guillemets)
2. **nom_serveur** : Nom du serveur/vendeur (entre guillemets)
3. **articles** : Liste des articles au format `code:quantité|code:quantité|...`

### Exemple d'Utilisation

```bash
python main.py "But Market" "Lisa" "C01:1|C02:3|C03:2"
```

### Résultat Attendu

```bash
{}
But Market
Ticket numéro : 3

Date : 01/10/2025

Vous avez été servi par : Lisa

NB   Description     Poids Unit.  Poids Total  HT unitaire  TVA   Total
1    pack de coca    2.00kg       2.00kg       5€           20%   6.00€
3    kilo de pdt     1.00kg       3.00kg       1€           10%   3.30€
2    pack Biscotte   950g         1.90kg       2€           10%   4.40€

                                                Total Poids :    6.90kg
                                                Total HT    :    8.00€
                                                Total TVA   :    1.70€
                                                Total TTC   :    9.70€
```

## Base de Données des Articles

Les articles disponibles sont stockés dans le dictionnaire `bdd` avec leurs propriétés complètes :

| Code | Description     | Poids  | Prix HT | TVA | Origine    |
|------|----------------|--------|---------|-----|------------|
| C01  | pack de coca   | 2.0kg  | 5€      | 20% | Lituanie   |
| C02  | kilo de pdt    | 1.0kg  | 1€      | 10% | Espagne    |
| C03  | pack Biscotte  | 950g   | 2€      | 10% | France     |
| C04  | Café soluble   | 250g   | 3€      | 10% | Roumanie   |
| C05  | Crakers        | 125g   | 4€      | 20% | Angleterre |
| C06  | Eau            | 1.5kg  | 6€      | 10% | Suisse     |
| C07  | Pain           | 250g   | 1€      | 10% | France     |

### Ajout de Nouveaux Produits

Pour ajouter un nouveau produit, modifiez le dictionnaire `bdd` dans le fichier `main.py` :

```python
bdd = {
    "C01": {"description": "pack de coca", "poids": 2, "prix": 5, "TVA": 0.2, "Orgine": "Lituanie"},
    "C02": {"description": "kilo de pdt", "poids": 1, "prix": 1, "TVA": 0.1, "Orgine": "Espagne"},
    "C03": {"description": "pack Biscotte", "poids": 0.95, "prix": 2, "TVA": 0.1, "Orgine": "France"},
    # ... autres articles existants
    "C08": {"description": "Nouveau produit", "poids": 0.5, "prix": 6, "TVA": 0.1, "Orgine": "France"}
}
```

### Format d'Ajout

- **Code** : Identifiant unique (ex: "C08")
- **Description** : Nom du produit (string)
- **Poids** : Poids en kilogrammes (float)
- **Prix** : Prix unitaire HT (nombre entier ou décimal)
- **TVA** : Taux de TVA en décimal (0.1 = 10%, 0.2 = 20%)
- **Orgine** : Pays d'origine (string)

## Fonctions Principales

### `calcul_resultat(dico, articles)`

Calcule les totaux pour tous les articles du panier, incluant les poids.

**Paramètres :**

- `dico` : Base de données des articles
- `articles` : Dictionnaire des articles commandés

**Retour :**

- `liste_prix` : Liste détaillée des calculs par article [code, quantité, prix_unitaire, prix_total_ht, tva_montant, poids_unitaire, poids_total]
- `total_ht` : Total hors taxes
- `total_tva` : Total de la TVA

### `formater_poids(poids_kg)`

Formate automatiquement l'affichage des poids pour une meilleure lisibilité.

**Paramètres :**

- `poids_kg` : Poids en kilogrammes

**Retour :**

- String formatée (ex: "950g" pour 0.95kg, "2.00kg" pour 2kg)

### `generer_numero_ticket()`

Génère un numéro de ticket incrémental sauvegardé dans un fichier.

**Retour :**

- Numéro de ticket unique et incrémental

### `affichage(articles, bdd)`

Affiche le ticket de caisse formaté.

**Paramètres :**

- `articles` : Dictionnaire des articles commandés
- `bdd` : Base de données des articles

## Gestion des Erreurs

Le programme gère automatiquement :

### Codes Articles Invalides

```bash
python main.py "Magasin" "Vendeur" "X99:1"
# Résultat : Erreur: Le code article 'X99' n'existe pas dans la base de données.
```

### Quantités Invalides

```bash
python main.py "Magasin" "Vendeur" "C01:abc"
# Résultat : Erreur: La quantité 'abc' n'est pas un nombre valide.
```

### Paramètres Manquants

```bash
python main.py "Magasin"
# Résultat : IndexError (pas assez d'arguments)
```

## Configuration

### Taux de TVA

Chaque produit peut avoir son propre taux de TVA défini dans la base de données :

```python
# Dans le dictionnaire bdd
"C01": {"description": "pack de coca", "poids": 2, "prix": 5, "TVA": 0.2, "Orgine": "Lituanie"},  # TVA 20%
"C02": {"description": "kilo de pdt", "poids": 1, "prix": 1, "TVA": 0.1, "Orgine": "Espagne"},   # TVA 10%
```

### Numéro de Ticket

Les numéros de tickets sont automatiquement incrémentés et sauvegardés dans `numero_ticket.txt`. Le compteur démarre à 1 et s'incrémente à chaque nouvelle vente.

### Formatage des Poids

Le système affiche automatiquement :

- Les poids < 1kg en grammes (ex: 950g, 250g)
- Les poids ≥ 1kg en kilogrammes (ex: 2.00kg, 1.50kg)

## Tests

Le programme inclut des tests automatiques pour vérifier le bon fonctionnement :

```python
# Test automatique dans main.py
art_test = {'C03': 12, 'C01': 10}
resultat_test = calcul_resultat(bdd, art_test)
expected = ([['C03', 12, 2, 24, 2.4, 0.95, 11.4], ['C01', 10, 5, 50, 10.0, 2, 20]], 74, 12.4)
assert resultat_test == expected
```

### Fichiers Générés

Le programme crée automatiquement :

- `numero_ticket.txt` : Stockage du dernier numéro de ticket utilisé

## Exemples d'Utilisation Avancés

### Commande Simple

```bash
python main.py "SuperMarché" "Marie" "C01:2"
```

### Commande Multiple

```bash
python main.py "Épicerie du Coin" "Jean" "C01:1|C02:5|C03:3|C04:2"
```

### Grandes Quantités

```bash
python main.py "Grossiste" "Paul" "C02:100|C05:50"
```

## Nouvelles Fonctionnalités (Version Actuelle)

### 🆕 Affichage des Poids

- Affichage du poids unitaire et total pour chaque article
- Formatage intelligent : grammes pour < 1kg, kilogrammes pour ≥ 1kg
- Calcul automatique du poids total de la commande

### 🆕 TVA Variable

- Chaque produit peut avoir son propre taux de TVA
- Support de différents taux (10%, 20%, etc.)
- Affichage du taux de TVA spécifique pour chaque ligne

### 🆕 Numérotation Automatique

- Numéros de tickets incrémentaux automatiques
- Sauvegarde persistante dans un fichier
- Reprise du compteur après redémarrage

### 🆕 Interface Améliorée

- Colonnes parfaitement alignées
- Ligne de séparation pour l'en-tête
- Totaux alignés à droite pour une meilleure lisibilité
