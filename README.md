# TP IUT 
TP sur la gestion de projet niveau IUT

AUBINAIS Nathan - VIEIRA MIRANDA Lucas 
3B1 - 01/10/25


## Projet Ticket de caisse 

### 1. Objectif du programme

Ce programme simule un système de ticket de caisse.
L’utilisateur fournit en ligne de commande :

le nom du magasin

le nom du personnel

une commande au format C01:10|C02:2

Le programme affiche un ticket de caisse formaté dans une fenêtre Tkinter, avec le détail des achats, les totaux HT, TVA et TTC.

### 2. Structure du code
   
#### a) Imports nécessaires

```Python
import sys
from datetime import datetime
import tkinter as tk
```

sys : pour lire les arguments passés en ligne de commande.

datetime : pour générer la date du jour.

tkinter : pour créer une interface graphique et afficher le ticket.

#### b) Articles disponibles

```Python
articles = [
    {"Code": "C01", "Description": "Pack de coca", "Prix": 5},
    {"Code": "C02", "Description": "Kilo de pdt", "Prix": 1},
    {"Code": "C03", "Description": "Pack de Biscotte", "Prix": 2},
    {"Code": "C04", "Description": "Café soluble", "Prix": 3},
    {"Code": "C05", "Description": "Crakers", "Prix": 4},
]
```

Chaque article est représenté par un dictionnaire avec :

Code → identifiant unique (C01, C02, …)

Description → nom de l’article

Prix → prix unitaire HT

#### c) Variables globales

```Python
TVA = 0.1        # 10% de TVA
Total_TVA = 0.0
Total_HT = 0.0
Total_articles = 0.0
Total_final = 0.0
num_ticket = 2200  # numéro initial du ticket
```

#### d) Fonction Date()

```Pyhton
def Date() -> str:
    date = datetime.now()
    return date.strftime("%d/%m/%Y")
```
Retourne la date du jour au format JJ/MM/AAAA

#### e) Fonction recuperer_infos_ticket

```Python
def recuperer_infos_ticket(nom_mag, personnel, commande, articles_disponibles):
    catalogue = {art["Code"]: art for art in articles_disponibles}
    articles_ticket = []

    for item in commande.split('|'):
        code, quant = item.split(':')
        quant = int(quant)
        if code in catalogue:
            art = catalogue[code]
            articles_ticket.append({
                "Desc": art["Description"],
                "Prix": art["Prix"],
                "TVA": TVA,
                "Quantite": quant
            })
        else:
            print(f"Attention : code {code} non trouvé dans le catalogue.")

    return {
        "nom_mag": nom_mag,
        "personnel": personnel,
        "articles": articles_ticket
    }
```
Cette fonction :

Transforme la commande en dictionnaire.

Associe chaque code à son article correspondant.

Crée une liste d’articles commandés avec description, prix, TVA et quantité.

#### f) Fonction Ticket_caisse

Cette fonction affiche un ticket formaté dans une fenêtre Tkinter.

Exemple d’affichage :

```Text
Mon Supermarché
Ticket numéro : 2201

Date : 01/10/2025

Vous avez été servi par : Nathan

NB  Desc.               HT unitaire  TVA   Total
10  Pack de coca        5€           10%   55.0€
 2  Kilo de pdt         1€           10%    2.2€

Total HT        52.0€
Total TVA        5.2€
Total            57.2€
```

Elle calcule automatiquement :

le total HT

le montant de la TVA

le total TTC

#### g) Bloc principal (if __name__ == "__main__":)

Vérifie que l’utilisateur a bien entré 3 arguments.

Incrémente le numéro du ticket.

Vérifie que le prénom ne contient pas de chiffres.

Vérifie que la commande est bien au bon format (Cxx:Nombre).

Appelle recuperer_infos_ticket puis Ticket_caisse.

#### 3. Utilisation
Lancer le programme

Dans le terminal :

```Python
python3 main.py "Mon Supermarché" "Nathan" "C01:10|C02:2"
```

Résultat attendu

Une fenêtre Tkinter s’ouvre avec le ticket de caisse détaillé.

### 4. Points forts

Gestion des erreurs si l’utilisateur oublie les paramètres.

Vérification du format des commandes.

Interface graphique lisible via Tkinter.

Totaux HT, TVA et TTC bien calculés.

### 5. Améliorations possibles

Sauvegarder le ticket en PDF ou TXT.

Ajouter un système de remise ou promotion.

Gérer plusieurs taux de TVA selon les articles.

Enregistrer l’historique des tickets dans un fichier.
