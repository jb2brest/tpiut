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

| Code article | Description   | Poids ou volume unitaire | Prix HT unitaire (€) | TVA   | Origine     |
|--------------|---------------|--------------------------|-----------------------|-------|-------------|
| C01          | Pack de coca  | 2kg                      | 5                     | 20 %  | Lituanie    |
| C02          | Kilo de pdt   | 1kg                      | 1                     | 10 %  | Espagne     |
| C03          | Pack Biscotte | 950g                     | 2                     | 10 %  | France      |
| C04          | Café soluble  | 250g                     | 3                     | 10 %  | Roumanie    |
| C05          | Crackers      | 125g                     | 4                     | 20 %  | Angleterre  |
| C06          | Eau           | 1.5L                     | 6                     | 10 %  | Suisse      |
| C07          | Pain          | 250g                     | 1                     | 10 %  | France      |
---

## Exécution du programme

Commande générale :  

```bash
python3 main.py "[Magasin]" "[Caissier]" "[code article 1]:[quantité]|[code article 2]:[quantité]|..."
```

Vous pouvez ajouter autant d’articles que nécessaire, en les séparant par **`|`**.  

### Exemple (génération de ticket)
```bash
python3 main.py "But Market" "Lisa" "C01:10|C02:2"
```

---

## Articles disponibles (exemple)

```
--- ARTICLES DISPONIBLES ---
C01: pack de coca (2kg) - 5€ - TVA 20%
C02: kilo de pdt (1kg) - 1€ - TVA 10%
C03: pack Biscotte (950g) - 2€ - TVA 10%
C04: Café soluble (250g) - 3€ - TVA 10%
C05: Crakers (125g) - 4€ - TVA 20%
C06: Eau (1.5L) - 6€ - TVA 10%
C07: Pain (250g) - 1€ - TVA 10%
-----------------------------
```

---


## Résultat attendu (exemple complet)

Commande :  
```bash
python3 main.py "But Market" "Lisa" "C01:10|C02:2|C07:4"
```

Résultat :  
```
Bienvenue dans notre supermarché But Market !

================================================================================
But Market
Ticket numéro : 92

Date : 01/10/2025

Vous avez été servi par : Lisa

NB  Desc.           Poids/volume  Poids/volume  HT unitaire TVA  Total HT
                    unitaire      total                                
10  pack de coca    2kg           20.0kg        5€          20%  50.0€ 
2   kilo de pdt     1kg           2.0kg         1€          10%  2.0€  
4   Pain            250g          1000.0g       1€          10%  4.0€  

                                                                   Total HT    56€
                                                                   Total TVA   10.6€
                                                                   Total       66.6€
================================================================================
```



