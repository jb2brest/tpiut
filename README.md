# tpiut
TP sur la gestion de projet niveau IUT

## Installation


### Prérequis

- **Python** : Assurez-vous que Python 3.7 ou une version ultérieure est installé sur votre machine.
- **Fichiers nécessaires** : Le fichier `main.py` doit être présent dans le répertoire du projet.
- **Terminal** : Un terminal ou un invite de commande pour exécuter le script.

### Installation

 Clonez le dépôt ou téléchargez les fichiers du projet.


## Utilisation


#### Exécution du programme :

Utilisez la commande suivante :
```bash
python main.py <nom_magasin> <nom_caissier> <articles>
```

- `<nom_magasin>` : Nom du magasin (exemple : `"Supermarché XYZ"`).
- `<nom_caissier>` : Nom du caissier (exemple : `"Jean Dupont"`).
- `<articles>` : Liste des articles sous la forme `Code:Quantité` séparés par `|` (exemple : `C01:2|C02:3|C03:1`).

Exemple :
```bash
python main.py "Supermarché XYZ" "Jean Dupont" "C01:2|C02:3|C03:1"
```

### Options disponibles

- **Codes des articles disponibles dès l'installation du script** :
  - `C01` : pack de coca (5€ HT)
  - `C02` : kilo de pommes de terre (1€ HT)
  - `C03` : pack de biscottes (2€ HT)
  - `C04` : café soluble (3€ HT)
  - `C05` : crackers (4€ HT)

- **Taux de TVA** : 10% (fixe).

### Exemple de ticket généré

exemple de ticket généré par le script :
```
Supermarché XYZ
Ticket numéro : 2200
Date : 01/10/2025

Vous avez été servi par : Jean Dupont

NB  Desc.            HT unitaire  TVA   Total
2   pack de coca       5€          10%   11.0€
3   kilo de pdt        1€          10%   3.3€
1   pack Biscotte      2€          10%   2.2€

Total HT      12€
Total TVA     1.5€
Total         13.5€
```

## Ajout de nouveaux articles

### Structure des fichiers ou dossiers

Les articles disponibles sont définis dans le dictionnaire `ITEMS` du fichier main.py. Chaque article est représenté par un code unique, une description et un prix HT.


## Expliquer la fonction `ajouter_produit` et comment s'en servir :


## Fonction : `ajouter_produit`

### Description

La fonction `ajouter_produit` permet d'ajouter un nouveau produit à la liste des articles disponibles dans le fichier `items.json`. Elle vérifie si le code du produit est unique et si le prix est valide avant d'ajouter le produit.

### Prototype
```python
def ajouter_produit(items, code, desc, prix):
```

### Paramètres

- `items` : Le dictionnaire contenant les articles existants.
- `code` : Le code unique du produit à ajouter (exemple : `"C06"`).
- `desc` : La description du produit (exemple : `"pack de jus d'orange"`).
- `prix` : Le prix HT du produit (exemple : `3.5`).

### Fonctionnement

1. Vérifie si le code du produit existe déjà dans le dictionnaire `items`.
   - Si le code existe, un message d'erreur est affiché : `"Ce code existe déjà."`.
2. Vérifie si le prix est un nombre valide.
   - Si le prix est invalide, un message d'erreur est affiché : `"Prix invalide."`.
3. Si les validations sont réussies, le produit est ajouté au dictionnaire `items` avec ses informations (description et prix).
4. Le fichier `items.json` est mis à jour pour inclure le nouveau produit.
5. Affiche un message de confirmation : `"Produit <code> ajouté."`.

---

## Comment utiliser la fonction `ajouter_produit`

### Utilisation via le script main.py

Pour ajouter un produit, utilisez la commande suivante dans le terminal :

```bash
python main.py Ajout <code> "<description>" <prix>
```

### Arguments

- `<code>` : Le code unique du produit (exemple : `"C06"`).
- `<description>` : La description du produit (exemple : `"pack de jus d'orange"`).
- `<prix>` : Le prix HT du produit (exemple : `3.5`).

### Exemple

Ajout d'un nouveau produit avec le code `C06`, une description `"pack de jus d'orange"`, et un prix de `3.5` :

```bash
python main.py Ajout C06 "pack de jus d'orange" 3.5
```

### Résultat attendu

Si l'ajout est réussi, le message suivant sera affiché dans le terminal :

```
Produit C06 ajouté.
```

Le produit sera également ajouté au fichier `items.json` avec les informations suivantes :

```json
"C06": {
    "desc": "pack de jus d'orange",
    "prix": 3.5
}
```

### Cas d'erreurs

1. **Code déjà existant** :
   Si le code `C06` existe déjà dans la liste des produits, le message suivant sera affiché :
   ```
   Ce code existe déjà.
   ```

2. **Prix invalide** :
   Si le prix fourni n'est pas un nombre valide, le message suivant sera affiché :
   ```
   Prix invalide.
   ```

### Arguments

- `<code>` : Le code unique du produit (exemple : `"C06"`).
- `<description>` : La description du produit (exemple : `"pack de jus d'orange"`).
- `<prix>` : Le prix HT du produit (exemple : `3.5`).

### Exemple

Ajout d'un nouveau produit avec le code `C06`, une description `"pack de jus d'orange"`, et un prix de `3.5` :

```bash
python main.py Ajout C06 "pack de jus d'orange" 3.5
```

### Résultat attendu

Si l'ajout est réussi, le message suivant sera affiché dans le terminal :

```
Produit C06 ajouté.
```

Le produit sera également ajouté au fichier `items.json` avec les informations suivantes :

```json
"C06": {
    "desc": "pack de jus d'orange",
    "prix": 3.5
}
```


## Explication de la fonction `enlever_produit` et comment s'en servir :


## Fonction : `enlever_produit`

### Description

La fonction `enlever_produit` permet de supprimer un produit existant de la liste des articles disponibles dans le fichier `items.json`. Elle vérifie si le code du produit existe avant de le supprimer.

### Prototype
```python
def enlever_produit(items, code):
```

### Paramètres

- `items` : Le dictionnaire contenant les articles existants.
- `code` : Le code unique du produit à supprimer (exemple : `"C06"`).

### Fonctionnement

1. Vérifie si le code du produit existe dans le dictionnaire `items`.
   - Si le code n'existe pas, un message d'erreur est affiché : `"Code produit introuvable."`.
2. Si le code existe, le produit est supprimé du dictionnaire `items`.
3. Le fichier `items.json` est mis à jour pour refléter la suppression.
4. Affiche un message de confirmation : `"Produit <code> supprimé."`.

---

## Comment utiliser la fonction `enlever_produit`

### Utilisation via le script main.py

Pour supprimer un produit, utilisez la commande suivante dans le terminal :

```bash
python main.py Suppression <code>
```

### Arguments

- `<code>` : Le code unique du produit à supprimer (exemple : `"C06"`).

### Exemple

Suppression d'un produit avec le code `C06` :

```bash
python main.py Suppression C06
```

### Résultat attendu

Si la suppression est réussie, le message suivant sera affiché dans le terminal :

```
Produit C06 supprimé.
```

Le produit sera également supprimé du fichier `items.json`.

### Cas d'erreurs

1. **Code introuvable** :
   Si le code `C06` n'existe pas dans la liste des produits, le message suivant sera affiché :
   ```
   Code produit introuvable.
   ```


### Expliquation de la fonction `modifier_produit` et comment s'en servir :

## Fonction : `modifier_produit`

### Description

La fonction `modifier_produit` permet de modifier la description ou le prix d'un produit existant dans la liste des articles disponibles. Elle vérifie si le produit existe avant d'appliquer les modifications.

### Prototype
```python
def modifier_produit(items, code, desc=None, prix=None):
```

### Paramètres

- `items` : Le dictionnaire contenant les articles existants.
- `code` : Le code unique du produit à modifier (exemple : `"C06"`).
- `desc` : La nouvelle description du produit (facultatif, exemple : `"pack de jus d'orange amélioré"`).
- `prix` : Le nouveau prix HT du produit (facultatif, exemple : `4.0`).

### Fonctionnement

1. Vérifie si le code du produit existe dans le dictionnaire `items`.
   - Si le code n'existe pas, un message d'erreur est affiché : `"Code produit introuvable."`.
2. Si une nouvelle description (`desc`) est fournie, elle remplace l'ancienne description.
3. Si un nouveau prix (`prix`) est fourni, il est converti en nombre flottant.
   - Si la conversion échoue, un message d'erreur est affiché : `"Prix invalide, modification annulée."`.
4. Le fichier `items.json` est mis à jour pour refléter les modifications.
5. Affiche un message de confirmation : `"Produit <code> modifié."`.

---

## Comment utiliser la fonction `modifier_produit`

### Utilisation via le script main.py

Pour modifier un produit, utilisez la commande suivante dans le terminal :

```bash
python main.py Modification <code> "<nouvelle_description>" <nouveau_prix>
```

### Arguments

- `<code>` : Le code unique du produit à modifier (exemple : `"C06"`).
- `<nouvelle_description>` : La nouvelle description du produit (facultatif, exemple : `"pack de jus d'orange amélioré"`).
- `<nouveau_prix>` : Le nouveau prix HT du produit (facultatif, exemple : `4.0`).

### Exemple

1. Modification de la description et du prix d'un produit avec le code `C06` :
   ```bash
   python main.py Modification C06 "pack de jus d'orange amélioré" 4.0
   ```

2. Modification uniquement de la description d'un produit avec le code `C06` :
   ```bash
   python main.py Modification C06 "pack de jus d'orange premium"
   ```

3. Modification uniquement du prix d'un produit avec le code `C06` :
   ```bash
   python main.py Modification C06 "" 5.0
   ```

### Résultat attendu

Si la modification est réussie, le message suivant sera affiché dans le terminal :

```
Produit C06 modifié.
```

Le produit sera également mis à jour dans le fichier `items.json`. Par exemple, après modification, le produit pourrait ressembler à ceci :

```json
"C06": {
    "desc": "pack de jus d'orange amélioré",
    "prix": 4.0
}
```

### Cas d'erreurs

1. **Code introuvable** :
   Si le code `C06` n'existe pas dans la liste des produits, le message suivant sera affiché :
   ```
   Code produit introuvable.
   ```

2. **Prix invalide** :
   Si le prix fourni n'est pas un nombre valide, le message suivant sera affiché :
   ```
   Prix invalide, modification annulée.
   ```

### Expliquation de la fonction `afficher_liste_produits` et comment s'en servir :

## Fonction : `afficher_liste_produits`

### Description

La fonction `afficher_liste_produits` permet d'afficher la liste des produits disponibles dans le dictionnaire `items`. Elle affiche chaque produit avec son code, sa description et son prix HT dans un format lisible.

### Prototype
```python
def afficher_liste_produits(items):
```

### Paramètres

- `items` : Le dictionnaire contenant les articles existants. Chaque article est représenté par un code unique, une description et un prix HT.

### Fonctionnement

1. Affiche un en-tête contenant les colonnes suivantes :
   - **Code** : Le code unique du produit.
   - **Description** : La description du produit.
   - **Prix HT** : Le prix hors taxes du produit.
2. Parcourt le dictionnaire `items` et affiche chaque produit dans un format aligné.
3. Ajoute une ligne vide à la fin pour une meilleure lisibilité.

---

## Comment utiliser la fonction `afficher_liste_produits`

### Utilisation via le script main.py

Pour afficher la liste des produits, utilisez la commande suivante dans le terminal :

```bash
python main.py Liste
```

### Exemple

Si vous exécutez la commande suivante :
```bash
python main.py Liste
```

Et que le fichier `items.json` contient les produits suivants :
```json
{
    "C01": {"desc": "pack de coca", "prix": 5},
    "C02": {"desc": "kilo de pdt", "prix": 1},
    "C03": {"desc": "pack Biscotte", "prix": 2},
    "C04": {"desc": "Café soluble", "prix": 3},
    "C05": {"desc": "Crakers", "prix": 4}
}
```

Le résultat affiché dans le terminal sera :
```
Liste des produits :
Code   Description         Prix HT
C01    pack de coca        5€
C02    kilo de pdt         1€
C03    pack Biscotte       2€
C04    Café soluble        3€
C05    Crakers             4€
```

### Cas d'erreurs

- Si le dictionnaire `items` est vide (aucun produit disponible), la fonction affichera uniquement l'en-tête sans produits listés.
```markdown
Liste des produits :
Code   Description         Prix HT
```
