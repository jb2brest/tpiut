# Sytème d'édition de ticket - TP Python
---

## Présentation
Ce projet consiste à réaliser un **système d'édition de ticket de caisse** en langage Python.   

Ce TP a pour but d'apprendre :
* La gestion de données.
* L'organisation de projet, de tâches.
* La gestion de besoin client (Demande de modification entre de Lot).
  
---
## Fonctionnalités
**LOT 1**
* Liste de produit simple (code, nom, prix HT)
* Calcul **Total HT, TVA, Total TTC**.
* Affichage de ticket (colonnes articles et nombre d'article, quantité, prix unitaire, prix HT)
* Documentation explicative avec plan des tests
  
**LOT 2 (fonctionnalité suplémentaire)**
* Affichage du poids à l'unité par article 
* Affichage du poids total par article

---
# Structure du projet
```
├── main.py        # Script Lot 1
├── readme.md      # Documentation
```
---
## Installation

### 1. Cloner le projet
```
git clone https://github.com/jb2brest/tpiut.git
cd tpiut
git checkout 2025-Lannion-GA2-SOHIER-GIRAUD
```

### 2. Logiciel requis
* Python 3.8 minimum

---
## Utilisation
**LOT 1**
```
python3 main.py "But Market" "Lisa" "C01:2|C02:1|C03:3"
```
**LOT 2**
```
python3 main.py "BUT Market", "Lisa", "C01:10|C02:abc|C03:2|C99:3|C04:0|C05:-2"
```
**Exemple de sorti**
**LOT 1**
```

	BUT Market
Ticket numéro : 2200

Date : 30/09/2025

Vous avez été servi par : Lisa

NB	Desc.		HT unitaire	TVA	Total
10	pack de coca   	5€	10%	55.00€
2	kilo de pdt    	1€	10%	2.20€


				Total HT	52.00€
				Total TVA	5.20€
				Total   	57.20€
```

**LOT 2**
```
 Quantité 'abc' invalide pour C02. Saisissez un nombre entier.
Article C99 inconnu, ignoré.
 Quantité non valide (0) pour C04. Elle doit être > 0.
 Quantité non valide (-2) pour C05. Elle doit être > 0.

	BUT Market
Ticket numéro : 2200

Date : 30/09/2025

Vous avez été servi par : Lisa

NB	Description		Poids U.	Poids total	HT unitaire	TVA	Total TTC
10	pack de coca   	2.00kg	20.00kg 	5€	20%	60.00€
2	pack Biscotte  	950g  	1.90kg  	2€	20%	4.80€


						Total HT	54.00€
						Total TVA	10.80€
						Total   	64.80€
```
---
## Tests

| Objectif                       | Commande                                      | Résultat attendu                                      |                                                          |
| ------------------------------ | --------------------------------------------- | ----------------------------------------------------- | -------------------------------------------------------- |
|**LOT 1**|||
| Bon fonctionnement du ticket         | `python3 main.py "But Market" "Lisa" "C01:10{pipe}C02:2"` | Le code nous renvoie le ticket de caisse dans le bon format sans erreur |
| Code d'article en dehors de la base de donnée | `python3 main.py "But Market" "Lisa" "C012:10{pipe}C02:2"`| Code de l'article inconnu, article ignoré |
| Tester le fonctionnement avec une mauvaise quantité| `python3 main.py "But Market" "Lisa" "C01:{pipe}C02:"` | Renvoie un message : "La quantité n'est pas au bon format"|
| Changement de nom caissière et magasin | `python3 main.py "But Market3" "Lisa3" "C01:10{pipe}C02:2"`| Les modifications sont bien effectuée
**LOT 2**
| Verification de l'affichage du poids à l'unité et au totale |`python3 main.py "BUT Market", "Lisa", "C01:10{pipe}C02:abc{pipe}C03:2{pipe}C99:3{pipe}C04:0{pipe}C05:-2"`| L'affichage des 2 options doit être fonctionelle |

##  Livraison
**LOT1**
   * Développement + commit
   * Livraison → `git tag 3A2-lot1 && git push origin 3A2-lot1`
**LOT 2**
   * Livraison  → `git tag 3A2-lot2 && git push origin 3A2-lot2`
---

##  Binôme

* **Tristan Giraud**
* **Maël Sohier**

Groupe : **3A2 – Lannion 2025**
