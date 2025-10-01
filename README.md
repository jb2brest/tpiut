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


### Explication la fonction `ticket` et comment s'en servir :

## Fonction : `ticket`

### Description

La fonction `ticket` génère un ticket de caisse détaillé pour un achat. Elle affiche les informations générales du magasin, du caissier, et des articles achetés, ainsi que les totaux HT, TVA et TTC. Elle prend en compte des informations supplémentaires comme le poids ou volume unitaire des produits et calcule le poids total en fonction de la quantité.

### Prototype
```python
def ticket(magasin, caissier, panier, items, ticket_number):
```

### Paramètres

- `magasin` : Le nom du magasin (exemple : `"Supermarché XYZ"`).
- `caissier` : Le nom du caissier (exemple : `"Jean Dupont"`).
- `panier` : Une liste de tuples contenant le code produit et la quantité (exemple : `[("C01", 2), ("C02", 3)]`).
- `items` : Le dictionnaire contenant les articles existants.
- `ticket_number` : Le numéro unique du ticket.

### Fonctionnement

1. Affiche les informations générales du ticket :
   - Nom du magasin.
   - Numéro du ticket.
   - Date actuelle.
   - Nom du caissier.
2. Affiche un tableau détaillé des articles achetés avec les colonnes suivantes :
   - **NB** : La quantité de l'article.
   - **Desc.** : La description du produit.
   - **Pds/vol. uni.** : Le poids ou le volume unitaire du produit.
   - **Pds/vol.** : Le poids ou le volume total (calculé en fonction de la quantité).
   - **HT uni.** : Le prix HT unitaire.
   - **TVA** : Le taux de TVA applicable.
   - **Total** : Le montant total TTC pour cet article.
3. Calcule et affiche les totaux HT, TVA et TTC pour tous les articles.
4. Incrémente le numéro de ticket pour le prochain achat.

---

## Comment utiliser la fonction `ticket`

### Utilisation via le script mainv2.py

Pour générer un ticket, utilisez la commande suivante dans le terminal :

```bash
python mainv2.py "<nom_magasin>" "<nom_caissier>" "<articles>"
```

### Arguments

- `<nom_magasin>` : Le nom du magasin (exemple : `"Supermarché XYZ"`).
- `<nom_caissier>` : Le nom du caissier (exemple : `"Jean Dupont"`).
- `<articles>` : Une liste d'articles sous la forme `Code:Quantité` séparés par `|` (exemple : `"C01:2|C02:3|C03:1"`).

### Exemple

Si vous exécutez la commande suivante :
```bash
python mainv2.py "Supermarché XYZ" "Jean Dupont" "C01:2|C02:3|C03:1"
```

Et que le fichier items.json contient les produits suivants :
```json
{
    "C01": {"desc": "pack de coca", "poids_unitaire": "2kg", "prix": 5, "tva": 20, "origine": "Lituanie"},
    "C02": {"desc": "kilo de pdt", "poids_unitaire": "1kg", "prix": 1, "tva": 10, "origine": "Espagne"},
    "C03": {"desc": "pack Biscotte", "poids_unitaire": "950g", "prix": 2, "tva": 10, "origine": "France"}
}
```

Le résultat affiché dans le terminal sera :
```
Supermarché XYZ
Ticket numéro : 2200
Date : 01/10/2025

Vous avez été servi par : Jean Dupont

NB  Desc.            Pds/vol. uni.  Pds/vol.   HT uni.   TVA    Total
-------------------------------------------------------------------------------------
2   pack de coca      2kg            4.0kg      5€       20 %   12.0€
3   kilo de pdt       1kg            3.0kg      1€       10 %   3.3€
1   pack Biscotte     950g           950.0g     2€       10 %   2.2€
-------------------------------------------------------------------------------------
Total HT                                         12.0€
Total TVA                                        1.5€
Total                                            13.5€
```

### Cas d'erreurs

1. **Produit inconnu** :
   Si un code produit dans la liste des articles n'existe pas dans items.json, un message d'erreur sera affiché :
   ```
   Produit inconnu : <code>
   ```

2. **Quantité invalide** :
   Si la quantité d'un produit est invalide (non entière ou négative), un message d'erreur sera affiché :
   ```
   Quantité invalide pour <code> : <quantité>
   ```

3. **Format invalide** :
   Si un article est mal formaté (par exemple, `C01-2` au lieu de `C01:2`), un message d'erreur sera affiché :
   ```
   Format invalide pour l'article : '<article>' (attendu CODE:QTE)
   ```

4. **Aucun produit valide** :
   Si aucun produit valide n'est trouvé dans la commande, le script affichera :
   ```
   Aucun produit valide dans la commande.
   ```

### Notes

- Le numéro de ticket est automatiquement incrémenté après chaque commande et sauvegardé dans ticket_number.json.
- Si certains articles sont ignorés en raison d'erreurs, un avertissement sera affiché, mais le ticket sera généré pour les articles valides.


## Ajout de nouveaux articles

### Structure des fichiers ou dossiers

Les articles disponibles sont définis dans le dictionnaire `ITEMS` du fichier main.py. Chaque article est représenté par un code unique, une description et un prix HT.




### Explication de la fonction `ajouter_produit` et comment s'en servir :

## Fonction : `ajouter_produit`

### Description

La fonction `ajouter_produit` permet d'ajouter un nouveau produit à la liste des articles disponibles. Elle vérifie si le code du produit est unique et si les champs fournis (prix et TVA) sont valides avant d'ajouter le produit. Les informations sont ensuite sauvegardées dans le fichier JSON.

### Prototype
```python
def ajouter_produit(items, code, desc, poids_unitaire, prix, tva, origine):
```

### Paramètres

- `items` : Le dictionnaire contenant les articles existants.
- `code` : Le code unique du produit à ajouter (exemple : `"C08"`).
- `desc` : La description du produit (exemple : `"pack de jus d'orange"`).
- `poids_unitaire` : Le poids ou le volume unitaire du produit (exemple : `"1.5L"`).
- `prix` : Le prix HT du produit (exemple : `3.5`).
- `tva` : Le taux de TVA applicable au produit (exemple : `10`).
- `origine` : Le pays d'origine du produit (exemple : `"France"`).

### Fonctionnement

1. Vérifie si le code du produit existe déjà dans le dictionnaire `items`.
   - Si le code existe, un message d'erreur est affiché : `"Ce code existe déjà."`.
2. Vérifie si le prix et la TVA sont des valeurs valides.
   - Si l'une des valeurs est invalide, un message d'erreur est affiché : `"Prix ou TVA invalide."`.
3. Si les validations sont réussies, le produit est ajouté au dictionnaire `items` avec ses informations (description, poids unitaire, prix, TVA et origine).
4. Le fichier items.json est mis à jour pour inclure le nouveau produit.
5. Affiche un message de confirmation : `"Produit <code> ajouté."`.

---

## Comment utiliser la fonction `ajouter_produit`

### Utilisation via le script mainv2.py

Pour ajouter un produit, utilisez la commande suivante dans le terminal :

```bash
python mainv2.py Ajout <code> "<description>" <poids_unitaire> <prix> <tva> <origine>
```

### Arguments

- `<code>` : Le code unique du produit à ajouter (exemple : `"C08"`).
- `<description>` : La description du produit (exemple : `"pack de jus d'orange"`).
- `<poids_unitaire>` : Le poids ou le volume unitaire du produit (exemple : `"1.5L"`).
- `<prix>` : Le prix HT du produit (exemple : `3.5`).
- `<tva>` : Le taux de TVA applicable au produit (exemple : `10`).
- `<origine>` : Le pays d'origine du produit (exemple : `"France"`).

### Exemple

Ajout d'un nouveau produit avec le code `C08`, une description `"pack de jus d'orange"`, un poids unitaire de `1.5L`, un prix de `3.5`, une TVA de `10`, et une origine `"France"` :

```bash
python mainv2.py Ajout C08 "pack de jus d'orange" 1.5L 3.5 10 France
```

### Résultat attendu

Si l'ajout est réussi, le message suivant sera affiché dans le terminal :

```
Produit C08 ajouté.
```

Le produit sera également ajouté au fichier items.json avec les informations suivantes :

```json
"C08": {
    "desc": "pack de jus d'orange",
    "poids_unitaire": "1.5L",
    "prix": 3.5,
    "tva": 10,
    "origine": "France"
}
```

### Cas d'erreurs

1. **Code déjà existant** :
   Si le code `C08` existe déjà dans la liste des produits, le message suivant sera affiché :
   ```
   Ce code existe déjà.
   ```

2. **Prix ou TVA invalide** :
   Si le prix ou la TVA fournis ne sont pas des valeurs valides, le message suivant sera affiché :
   ```
   Prix ou TVA invalide.
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



### Explication de la fonction `modifier_produit` et comment s'en servir :

## Fonction : `modifier_produit`

### Description

La fonction `modifier_produit` permet de modifier les champs d'un produit existant dans la liste des articles disponibles. Elle vérifie si le produit existe avant d'appliquer les modifications et met à jour les informations dans le fichier JSON.

### Prototype
```python
def modifier_produit(items, code, desc=None, poids_unitaire=None, prix=None, tva=None, origine=None):
```

### Paramètres

- `items` : Le dictionnaire contenant les articles existants.
- `code` : Le code unique du produit à modifier (exemple : `"C06"`).
- `desc` : La nouvelle description du produit (facultatif, exemple : `"pack de jus d'orange amélioré"`).
- `poids_unitaire` : Le nouveau poids ou volume unitaire du produit (facultatif, exemple : `"2L"`).
- `prix` : Le nouveau prix HT du produit (facultatif, exemple : `4.0`).
- `tva` : Le nouveau taux de TVA applicable au produit (facultatif, exemple : `20`).
- `origine` : Le nouveau pays d'origine du produit (facultatif, exemple : `"Espagne"`).

### Fonctionnement

1. Vérifie si le code du produit existe dans le dictionnaire `items`.
   - Si le code n'existe pas, un message d'erreur est affiché : `"Code produit introuvable."`.
2. Si une nouvelle description (`desc`) est fournie, elle remplace l'ancienne description.
3. Si un nouveau poids unitaire (`poids_unitaire`) est fourni, il remplace l'ancien poids unitaire.
4. Si un nouveau prix (`prix`) est fourni, il est converti en nombre flottant.
   - Si la conversion échoue, un message d'erreur est affiché : `"Prix invalide, modification annulée."`.
5. Si un nouveau taux de TVA (`tva`) est fourni, il est converti en entier.
   - Si la conversion échoue, un message d'erreur est affiché : `"TVA invalide, modification annulée."`.
6. Si une nouvelle origine (`origine`) est fournie, elle remplace l'ancienne origine.
7. Le fichier items.json est mis à jour pour refléter les modifications.
8. Affiche un message de confirmation : `"Produit <code> modifié."`.

---

## Comment utiliser la fonction `modifier_produit`

### Utilisation via le script mainv2.py

Pour modifier un produit, utilisez la commande suivante dans le terminal :

```bash
python mainv2.py Modification <code> "<nouvelle_description>" <nouveau_poids_unitaire> <nouveau_prix> <nouvelle_tva> <nouvelle_origine>
```

### Arguments

- `<code>` : Le code unique du produit à modifier (exemple : `"C06"`).
- `<nouvelle_description>` : La nouvelle description du produit (facultatif, exemple : `"pack de jus d'orange amélioré"`).
- `<nouveau_poids_unitaire>` : Le nouveau poids ou volume unitaire du produit (facultatif, exemple : `"2L"`).
- `<nouveau_prix>` : Le nouveau prix HT du produit (facultatif, exemple : `4.0`).
- `<nouvelle_tva>` : Le nouveau taux de TVA applicable au produit (facultatif, exemple : `20`).
- `<nouvelle_origine>` : Le nouveau pays d'origine du produit (facultatif, exemple : `"Espagne"`).

### Exemple

1. Modification de la description et du prix d'un produit avec le code `C06` :
   ```bash
   python mainv2.py Modification C06 "pack de jus d'orange amélioré" 2L 4.0 20 Espagne
   ```

2. Modification uniquement de la description d'un produit avec le code `C06` :
   ```bash
   python mainv2.py Modification C06 "pack de jus d'orange premium"
   ```

3. Modification uniquement du prix d'un produit avec le code `C06` :
   ```bash
   python mainv2.py Modification C06 "" "" 5.0
   ```

### Résultat attendu

Si la modification est réussie, le message suivant sera affiché dans le terminal :

```
Produit C06 modifié.
```

Le produit sera également mis à jour dans le fichier items.json. Par exemple, après modification, le produit pourrait ressembler à ceci :

```json
"C06": {
    "desc": "pack de jus d'orange amélioré",
    "poids_unitaire": "2L",
    "prix": 4.0,
    "tva": 20,
    "origine": "Espagne"
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

3. **TVA invalide** :
   Si le taux de TVA fourni n'est pas un entier valide, le message suivant sera affiché :
   ```
   TVA invalide, modification annulée.
   ```


### Explication de la fonction `afficher_liste_produits` et comment s'en servir :

## Fonction : `afficher_liste_produits`

### Description

La fonction `afficher_liste_produits` permet d'afficher la liste des produits disponibles dans un format tableau détaillé. Elle inclut des informations supplémentaires comme le poids ou volume unitaire, le prix HT, le taux de TVA et l'origine du produit.

### Prototype
```python
def afficher_liste_produits(items):
```

### Paramètres

- `items` : Le dictionnaire contenant les articles existants. Chaque article est représenté par un code unique, une description, un poids ou volume unitaire, un prix HT, un taux de TVA et une origine.

### Fonctionnement

1. Affiche un en-tête contenant les colonnes suivantes :
   - **Code** : Le code unique du produit.
   - **Description** : La description du produit.
   - **Poids/vol.** : Le poids ou le volume unitaire du produit.
   - **Prix HT** : Le prix hors taxes du produit.
   - **TVA** : Le taux de TVA applicable au produit.
   - **Origine** : Le pays d'origine du produit.
2. Parcourt le dictionnaire `items` et affiche chaque produit dans un format aligné.
3. Ajoute une ligne vide à la fin pour une meilleure lisibilité.

---

## Comment utiliser la fonction `afficher_liste_produits`

### Utilisation via le script mainv2.py

Pour afficher la liste des produits, utilisez la commande suivante dans le terminal :

```bash
python mainv2.py Liste
```

### Exemple

Si vous exécutez la commande suivante :
```bash
python mainv2.py Liste
```

Et que le fichier items.json contient les produits suivants :
```json
{
    "C01": {"desc": "pack de coca", "poids_unitaire": "2kg", "prix": 5, "tva": 20, "origine": "Lituanie"},
    "C02": {"desc": "kilo de pdt", "poids_unitaire": "1kg", "prix": 1, "tva": 10, "origine": "Espagne"},
    "C03": {"desc": "pack Biscotte", "poids_unitaire": "950g", "prix": 2, "tva": 10, "origine": "France"}
}
```

Le résultat affiché dans le terminal sera :
```
Code  Description        Poids/vol.  Prix HT  TVA   Origine
---------------------------------------------------------------
C01   pack de coca        2kg         5       20 %  Lituanie
C02   kilo de pdt         1kg         1       10 %  Espagne
C03   pack Biscotte       950g        2       10 %  France
```

### Cas d'erreurs

- Si le dictionnaire `items` est vide (aucun produit disponible), la fonction affichera uniquement l'en-tête sans produits listés :
```
Code  Description        Poids/vol.  Prix HT  TVA   Origine
---------------------------------------------------------------
```
