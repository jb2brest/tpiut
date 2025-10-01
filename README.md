# Système de Génération de Tickets de Caisse

## Description

Ce projet est un système de génération de tickets de caisse développé en Python. Il permet de créer des tickets formatés avec calcul automatique des totaux HT, TVA et TTC.

## Fonctionnalités

- ✅ Génération de tickets de caisse formatés
- ✅ Calcul automatique des totaux (HT, TVA, TTC)
- ✅ Gestion d'une base de données d'articles
- ✅ Validation des données d'entrée
- ✅ Gestion des erreurs (codes articles invalides, quantités incorrectes)
- ✅ Affichage aligné des colonnes
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
{'C01': 1, 'C02': 3, 'C03': 2}
But Market
Ticket numéro : 2200

Date : 01/10/2025

Vous avez été servi par : Lisa

NB     Description     HT unitaire  TVA    Total
1      pack de coca    5€           10%    5.5€
3      kilo de pdt     1€           10%    3.3€
2      pack Biscotte   2€           10%    4.4€

                          Total HT  :    10.00€
                          Total TVA :     1.00€
                          Total TTC :    11.00€
```

## Base de Données des Articles

Les articles disponibles sont stockés dans le dictionnaire `bdd` :

| Code | Description     | Prix HT |
|------|----------------|---------|
| C01  | pack de coca   | 5€      |
| C02  | kilo de pdt    | 1€      |
| C03  | pack Biscotte  | 2€      |
| C04  | Café soluble   | 3€      |
| C05  | Crakers        | 4€      |

### Ajout de Nouveaux Produits

Pour ajouter un nouveau produit, modifiez le dictionnaire `bdd` dans le fichier `main.py` :

```python
bdd = {
    "C01": {"description": "pack de coca", "prix": 5},
    "C02": {"description": "kilo de pdt", "prix": 1},
    "C03": {"description": "pack Biscotte", "prix": 2},
    "C04": {"description": "Café soluble", "prix": 3},
    "C05": {"description": "Crakers", "prix": 4},
    "C06": {"description": "Nouveau produit", "prix": 6}  # Nouveau produit
}
```

### Format d'Ajout

- **Code** : Identifiant unique (ex: "C06")
- **Description** : Nom du produit (string)
- **Prix** : Prix unitaire HT (nombre entier ou décimal)

## Fonctions Principales

### `calcul_resultat(dico, articles)`

Calcule les totaux pour tous les articles du panier.

**Paramètres :**

- `dico` : Base de données des articles
- `articles` : Dictionnaire des articles commandés

**Retour :**

- `liste_prix` : Liste détaillée des calculs par article
- `total_ht` : Total hors taxes
- `total_tva` : Total de la TVA

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

Le taux de TVA est fixé à 10% dans le code. Pour le modifier :

```python
# Dans la fonction calcul_resultat
tva_montant = round(prix_total_ht * 0.1, 2)  # Changer 0.1 pour le nouveau taux
```

### Numéro de Ticket

Le numéro de ticket est fixe (2200). Pour le rendre dynamique :

```python
# Remplacer dans la fonction affichage
import random
numero_ticket = random.randint(1000, 9999)
print(f"Ticket numéro : {numero_ticket}")
```

## Tests

Le programme inclut des tests automatiques pour vérifier le bon fonctionnement :

```python
# Test automatique dans main.py
art_test = {'C03': 12, 'C01': 10}
resultat_test = calcul_resultat(bdd, art_test)
assert resultat_test == expected
```

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
