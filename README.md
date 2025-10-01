# R5.04 - Cycle de vie d'un projet informatique - TP  
### Réalisé par : Gurvan MURY & Elian SALOU  

---

## Projet : Système de Ticket de Caisse  

Ce projet a pour objectif de développer un système de gestion simple permettant :  
- La génération de tickets de caisse pour un magasin.  
- L’ajout, la suppression et la modification des articles.  
- Une utilisation rapide en ligne de commande.  

---

## Tableau des articles de base

| Code article | Description      | Prix HT unitaire (€) |
|--------------|------------------|-----------------------|
| **C01**      | Pack de Coca     | 5.0                   |
| **C02**      | Kilo de PDT      | 1.0                   |
| **C03**      | Pack Biscotte    | 2.0                   |
| **C04**      | Café soluble     | 3.0                   |
| **C05**      | Crackers         | 4.0                   |

---

## Exécution du programme

Commande générale :  

```bash
python3 main.py "[Magasin]" "[Caissier]" "[code article 1]:[quantité]|[code article 2]:[quantité]|..."
```

Vous pouvez ajouter autant d’articles que nécessaire, en les séparant par **`|`**.  

---

##  Modes disponibles

### 1️ Mode Caisse (génération de ticket)
```bash
python3 main.py "But Market" "Lisa" "C01:10|C02:2"
```

### 2️ Mode Ajout (ajouter un article)
```bash
python3 main.py ajout "C06" "Eau minérale" "1.5"
```

### 3️ Mode Suppression (supprimer un article)
```bash
python3 main.py suppression "C06"
```

### 4 Mode Modification (modifier un article)
```bash
python3 main.py modification "C01" "Coca-Cola 2L" "6"
```

---

## Articles disponibles (exemple)

```
--- ARTICLES DISPONIBLES ---
C01: Coca-Cola 2L - 6.0€
C02: Kilo de PDT   - 1.0€
C03: Pack Biscotte - 2.0€
C04: Café soluble  - 3.0€
C05: Crackers      - 4.0€
-----------------------------
```

---

## Exemple d’ajout de produit

```bash
python3 main.py ajout "C06" "Eau minérale" "1.5"
```

Résultat attendu :  
```
Article 'C06' ajouté avec succès :
   Eau minérale - 1.5€
```

Puis à l’achat :  
```bash
python3 main.py "But Market" "Lisa" "C06:1"
```

```
Bienvenue dans notre supermarché But Market !

==================================================
But Market
Ticket numéro : 67
Date : 01/10/2025
Caissier : Lisa

NB  Desc.           HT unitaire  TVA   Total 
1   Eau minérale    1.5€         10%   1.65€  

                               Total HT   1.5€
                               Total TVA  0.15€
                               Total      1.65€
==================================================
```

---

## Résultat attendu (exemple complet)

Commande :  
```bash
python3 main.py "But Market" "Lisa" "C01:10|C02:2"
```

Résultat :  
```
Bienvenue dans notre supermarché But Market !

==================================================
But Market
Ticket numéro : 66
Date : 01/10/2025
Caissier : Lisa

NB  Desc.           HT unitaire  TVA   Total 
10  Coca-Cola 2L    6.0€         10%   60.0€ 
2   Kilo de PDT     1.0€         10%   2.0€  

                               Total HT   62.0€
                               Total TVA  6.2€
                               Total      68.2€
==================================================
```



