# Documentation du Script main.py — Générateur de Ticket de Caisse

## Description

Ce script Python permet de générer un ticket de caisse à partir d'une liste d'articles achetés, en prenant en paramètre le magasin, le vendeur, les différents articles et les quantités. Le ticket est sauvegardé dans un fichier texte nommé ticket.txt.

---

## Lancement du script

### Prérequis

- Python 3 doit être installé sur votre machine.
- Placez-vous dans le dossier contenant main.py.

### Commande d'exécution

```bash
python main.py <nom_magasin> <nom_serveur> <articles>
```

**Exemple :**
```bash
python main.py "BUT Market" "Lisa" "C01:10|C02:2"
```

---

## Fonctionnement

1. **Paramètres obligatoires :**
   - `<nom_magasin>` : Nom du magasin affiché sur le ticket.
   - `<nom_serveur>` : Nom du serveur ou caissier affiché sur le ticket.
   - `<articles>` : Liste des articles achetés, au format spécifique (voir ci-dessous).

2. **Format des articles :**
   - Un article : `code:quantite` (ex : `C01:6`)
   - Plusieurs articles : séparez-les par `|` (ex : `C01:10|C02:2|C03:1`)

3. **Articles disponibles :**

   | Code | Description        | Prix unitaire (€) |
   |------|-------------------|-------------------|
   | C01  | pack de coca      | 5                 |
   | C02  | kilo de pdt       | 1                 |
   | C03  | pack Biscotte     | 2                 |
   | C04  | Café soluble      | 3                 |
   | C05  | Crakers           | 4                 |

4. **Calculs réalisés :**
   - Total HT (hors taxes)
   - TVA (10%)
   - Total TTC (toutes taxes comprises)

5. **Résultat :**
   - Un fichier ticket.txt est généré avec le ticket de caisse formaté.

---

## Ajout de produits

Pour ajouter un produit à la liste des articles disponibles :
1. Ouvrez le fichier main.py.
2. Repérez la section suivante :
   ```python
   articles = {
       "C01": {"desc": "pack de coca", "prix": 5},
       ...
   }
   ```
3. Ajoutez une nouvelle ligne avec un code unique, une description et un prix.  
   Exemple :
   ```python
   "C06": {"desc": "Jus d'orange", "prix": 3}
   ```

---

## Gestion des erreurs

- Si un code article est inconnu ou une quantité est nulle, l'article est ignoré.
- Si le format d'un article est incorrect, il est ignoré avec un message d'avertissement.

---

## Exemple de ticket généré

```
----------------------------------------
BUT Market
Ticket numéro : 1234

Date : 01/10/2025

Vous avez été servi par : Lisa

NB  Desc.                 HT unitaire  TVA  Total
10 pack de coca           5€        10%   55.00€
2 kilo de pdt             1€        10%   2.20€

                              Total HT   52€
                              Total TVA  5.2€
                              Total      57.20€
----------------------------------------
```

---

## Auteur

- Script réalisé dans le cadre d'un projet.
- Pour toute modification, reportez-vous aux commentaires dans le code source.
