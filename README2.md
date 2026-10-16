# Générateur de Tickets de Caisse

Projet développé dans le cadre du module IUT, en duo. Ce programme en ligne de commande génère un ticket de caisse formaté à partir d'un catalogue d'articles et d'une commande passée en argument.

Suite à la modification du besoin client, le ticket :

- applique la **TVA à 20 %** sur certains produits (10 % pour les autres) ;
- affiche le **poids ou volume** de chaque produit (unitaire et total) ;
- affiche l'**origine** du produit, uniquement pour le **format trinôme**.

## Structure du projet

- `main.py` : script principal, génère et affiche le ticket de caisse
- `README.md` : documentation du projet

## Prérequis

- Python 3.6 ou supérieur
- Aucune bibliothèque externe (uniquement la bibliothèque standard : `sys`, `datetime`)

## Catalogue

Le catalogue est défini dans le dictionnaire `CATALOGUE` de `main.py` :

| Code | Description   | Poids / volume | Prix HT | TVA | Origine    |
|------|---------------|----------------|---------|-----|------------|
| C01  | Pack de coca  | 2kg            | 5.00 €  | 20% | Lituanie   |
| C02  | Kilo de pdt   | 1kg            | 1.00 €  | 10% | Espagne    |
| C03  | Pack Biscotte | 950g           | 2.00 €  | 10% | France     |
| C04  | Café soluble  | 250g           | 3.00 €  | 10% | Roumanie   |
| C05  | Crakers       | 125g           | 4.00 €  | 20% | Angleterre |
| C06  | Eau           | 1.5L           | 6.00 €  | 10% | Suisse     |
| C07  | Pain          | 250g           | 1.00 €  | 10% | France     |

Les poids sont stockés en grammes (`"g"`) ou en millilitres (`"ml"`) et convertis à l'affichage (`2000 g` → `2kg`, `1500 ml` → `1.5L`).

## Format binôme

## Lancement

### Générer un ticket

```bash
python main.py "Magasin" "Caissier" "CODE:QUANTITÉ|CODE:QUANTITÉ"
```

Le script prend 3 arguments obligatoires :

1. Nom du magasin
2. Nom du caissier
3. Contenu de la commande au format `CODE:QUANTITÉ`, plusieurs articles séparés par `|`

Exemple :

```bash
python main.py "Mon Magasin" "Hugo" "C01:2|C02:3|C03:1"
```

Résultat en format binôme (`AFFICHER_ORIGINE = False`) :

```text
Mon Magasin
Ticket numéro : 2200
Date : 16/10/2026

Vous avez été servi par : Hugo

NB  Desc.          Pds/vol. unitaire  Pds/vol. total  HT unitaire  TVA   Total
2   pack de coca   2kg                4kg             5€           20%   12€
3   kilo de pdt    1kg                3kg             1€           10%   3.3€
1   pack Biscotte  950g               950g            2€           10%   2.2€

                                                      Total HT   15€
                                                      Total TVA  2.5€
                                                      Total      17.5€
```

## Lancement

### Générer un ticket

```bash
python main.py "Magasin" "Caissier" "CODE:QUANTITÉ|CODE:QUANTITÉ"
```

Le script prend 3 arguments obligatoires :

1. Nom du magasin
2. Nom du caissier
3. Contenu de la commande au format `CODE:QUANTITÉ`, plusieurs articles séparés par `|`

Exemple :

```bash
python main.py "Mon Magasin" "Hugo" "C01:2|C02:3|C03:1"
```

Résultat en format binôme (`AFFICHER_ORIGINE = False`) :

```text
Mon Magasin
Ticket numéro : 2200
Date : 16/10/2026

Vous avez été servi par : Hugo

NB  Desc.          Pds/vol. unitaire  Pds/vol. total  HT unitaire  TVA   Total
2   pack de coca   2kg                4kg             5€           20%   12€
3   kilo de pdt    1kg                3kg             1€           10%   3.3€
1   pack Biscotte  950g               950g            2€           10%   2.2€

                                                      Total HT   15€
                                                      Total TVA  2.5€
                                                      Total      17.5€
```


## Fonctionnement

Pour chaque ligne de la commande, le programme :

1. Cherche le code dans le catalogue
2. Calcule le total HT de la ligne : `prix HT × quantité`
3. Calcule la TVA : `total HT × taux / 100`
4. Calcule le poids/volume total : `poids unitaire × quantité`
5. Affiche le total TTC de la ligne (HT + TVA)

À la fin, il affiche le total HT, le total de TVA et le total TTC du ticket.

Gestion des erreurs :

- Code inconnu : la ligne est ignorée avec le message `Ligne ignorée (code inconnu)`
- Quantité invalide : la ligne est ignorée avec le message `Ligne ignorée (quantité invalide)`
- Arguments manquants : un message d'utilisation est affiché

## Ajout de produits

Un produit s'ajoute dans `main.py` avec la fonction `ajouter_article_catalogue` (ou directement dans le dictionnaire `CATALOGUE`) :

```python
ajouter_article_catalogue("C08", "Jus", 3.5, 10, 1000, "ml", "Espagne")
```

Paramètres : `code, nom, prix_ht, tva, poids, unite, origine`.

## Tests

Tests manuels réalisés :

| Objectif | Commande | Résultat attendu |
|----------|----------|------------------|
| Ticket standard (TVA 10 % et 20 %) | `python main.py "BUT Market" "Lisa" "C01:1\|C02:3\|C03:4"` | Total HT 16€, TVA 2.1€, Total 18.1€ |
| Produit en litres | `python main.py "BUT Market" "Lisa" "C06:2"` | Poids unitaire `1.5L`, total `3L` |
| Code inconnu | `python main.py "BUT Market" "Lisa" "C99:1"` | Ligne ignorée |
| Quantité invalide | `python main.py "BUT Market" "Lisa" "C01:abc"` | Ligne ignorée |
| Arguments manquants | `python main.py` | Message d'utilisation |
| Colonne origine | passer `AFFICHER_ORIGINE` à `True` / `False` | Colonne `Orig.` affichée / masquée |

## Livraison

```bash
git add .
git commit -m "Ajout TVA 20%, poids/volume et origine sur le ticket"
git push
git tag v1.0
git push --tags
```

## Auteurs

- *Hugo Guegan*
- *Jules Derrien*
