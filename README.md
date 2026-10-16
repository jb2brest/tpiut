# Générateur de Tickets de Caisse (Projet Python)

Projet développé dans le cadre du module IUT. Ce programme en ligne de commande génère un ticket de caisse formaté à partir d'un catalogue d'articles et d'une commande passée en argument. Le catalogue est stocké dans un fichier JSON, ce qui permet d'ajouter des produits de façon permanente.

## Structure du projet

- `main.py` : script principal, génère et affiche le ticket de caisse
- `test.py` : script de test simple pour vérifier le catalogue et les calculs de TVA
- `catalogue.json` : catalogue des articles (créé automatiquement au premier lancement)
- `README.md` : documentation du projet

## Prérequis

- Python 3.6 ou supérieur
- Aucune bibliothèque externe (uniquement la bibliothèque standard : `sys`, `json`, `os`, `datetime`)

## Catalogue par défaut

Au premier lancement, `catalogue.json` est créé avec 5 articles, TVA à 10 % :

| Code | Description   | Prix HT | TVA |
|------|---------------|---------|-----|
| C01  | Pack de coca  | 5.00 €  | 10% |
| C02  | Kilo de pdt   | 1.00 €  | 10% |
| C03  | Pack Biscotte | 2.00 €  | 10% |
| C04  | Café soluble  | 3.00 €  | 10% |
| C05  | Crakers       | 4.00 €  | 10% |

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

Résultat :

```text
Mon Magasin
Ticket numéro : 2200
Date : 16/10/2026

Vous avez été servi par : Hugo

NB   Desc.            HT unitaire  TVA    Total 
2    pack de coca     5.00€        10%    11.00€
3    kilo de pdt      1.00€        10%    3.30€
1    pack Biscotte    2.00€        10%    2.20€

                    Total HT        15.00€
                    Total TVA       1.50€
                    Total           16.50€
```

## Fonctionnement

Pour chaque ligne de la commande, le programme :

1. Cherche le code dans le catalogue
2. Calcule le total HT de la ligne : `prix HT × quantité`
3. Calcule la TVA : `total HT × taux / 100`
4. Affiche le total TTC de la ligne (HT + TVA)

À la fin, il affiche le total HT, le total de TVA et le total TTC du ticket.

Gestion des erreurs :

- Code inconnu : la ligne est ignorée avec le message `Ligne ignorée (code inconnu)`
- Quantité invalide : la ligne est ignorée avec le message `Ligne ignorée (quantité invalide)`
- Arguments manquants : un message d'utilisation est affiché

## Ajout de produits

Un produit s'ajoute avec un 4e argument optionnel au format `CODE:NOM:PRIX:TVA` :

```bash
python main.py "Mon Magasin" "Hugo" "C01:1" "C06:Jus d'orange:3.5:10"
```

- `CODE` : identifiant unique du produit (ex. `C06`)
- `NOM` : nom affiché sur le ticket
- `PRIX` : prix HT, avec un point comme séparateur décimal
- `TVA` : taux de TVA en pourcentage (entier)

Le produit est enregistré dans `catalogue.json` : il reste disponible aux lancements suivants, sans repasser le 4e argument.

Notes :

- Le 3e argument (la commande) reste obligatoire lors d'un ajout, utiliser par exemple `C01:1`
- Si le code existe déjà, le script affiche `Erreur : le code ... existe déjà.` et s'arrête
- Pour repartir du catalogue par défaut, supprimer `catalogue.json`

Une fois ajouté, le produit s'utilise normalement :

```bash
python main.py "Mon Magasin" "Hugo" "C01:2|C06:3"
```

## Tests

```bash
python test.py
```

Si tout fonctionne, le terminal affiche :

```text
TEST RÉUSSI : Le catalogue et les calculs fonctionnent parfaitement !
```
