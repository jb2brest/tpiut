# Projet Ticket de Caisse – HARROUD & CHAPPÉ

## Description
Ce projet consiste à développer un programme Python qui génère un **ticket de caisse** à partir d’une liste d’articles saisis en ligne de commande.  
Le ticket affiche le magasin, le numéro de ticket, la date, le nom du serveur, la liste des produits achetés ainsi que les **totaux HT, TVA et TTC**.  

---

## Auteurs
- Naël Harroud  
- Nathan Chappé  
-  R&T 3A1  
- 01/10/2025  

---

## Prérequis
- Python 3.x installé  
- Fichier `numTiquet.txt` initialisé avec un nombre de départ (ex. `2200`) pour gérer l’incrément du numéro de ticket.  

---

## Lancement du programme

### Commande générale
```bash
python3 HARROUD_CHAPPE_V1.py "NomMagasin" "NomServeur" "ListeProduits"
```

### Format de la liste de produits

Chaque produit est représenté par un code et une quantité : Cxx:nb

Plusieurs produits peuvent être passés en paramètre séparés par |.

Exemple :

```bash
python3 HARROUD_CHAPPE_V1.py "But Market" "Lisa" "C01:2|C02:3"
```

## Fonctionnement du programme
1. Générer un ticket de caisse

Le ticket est généré automatiquement lors de l’exécution du programme avec les paramètres valides.
Il affiche : le magasin, le numéro de ticket, la date, le serveur, les articles achetés et les totaux.

2. Ajouter un produit

Pour ajouter un nouvel article dans la base du programme, il faut modifier la liste liste_produit dans le fichier HARROUD_CHAPPE_V1.py.
Exemple :

```bash
["C06"], ["Chocolat"], [6]
```

3. Supprimer un produit

Pour supprimer un article, il suffit d’effacer sa ligne correspondante dans la liste liste_produit.

4. Annuler un ticket

Si vous lancez le programme avec un code d’article invalide, le ticket ne sera pas généré et un message d’erreur sera affiché.

Si vous souhaitez "annuler" un ticket déjà généré, il suffit de ne pas conserver la sortie (puisque le ticket est uniquement affiché dans la console).

Pour rétablir le compteur, il est possible de modifier manuellement le fichier numTiquet.txt.

5. Fermer le programme

Le programme se termine automatiquement après avoir généré le ticket (ou après avoir affiché une erreur).
Aucune action supplémentaire n’est requise.

## Articles disponibles

| Code | Description   | Prix HT unitaire |
| ---- | ------------- | ---------------- |
| C01  | Pack de coca  | 5 €              |
| C02  | Kilo de pdt   | 1 €              |
| C03  | Pack Biscotte | 2 €              |
| C04  | Café soluble  | 3 €              |
| C05  | Crackers      | 4 €              |

## Tests réalisés

Ticket simple → entrée C01:1 → ticket correct.

Ticket avec plusieurs produits → entrée C01:2|C02:3 → totaux conformes.

Code invalide → entrée Z99:1 → message d’erreur affiché.

Validation des calculs → contrôles manuels des montants HT/TVA/TTC.

## Notes

Le fichier numTiquet.txt est utilisé pour mémoriser le dernier numéro de ticket et l’incrémenter à chaque exécution.

Le taux de TVA est fixé à 10% pour tous les articles.

Le code vérifie la validité des entrées (format et codes produits).