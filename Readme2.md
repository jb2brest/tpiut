# 🧾 Générateur de Ticket de Caisse — `main.py`

## 📌 Description
Ce script Python génère un ticket de caisse à partir d'une liste d'articles achetés. Il prend en paramètre :
- le nom du magasin
- le nom du serveur/caissier
- la liste des articles avec leurs quantités

Le ticket est sauvegardé dans un fichier texte nommé `ticket2.txt`.

---

## Lancement du Script

### Prérequis
- Python 3 doit être installé sur votre machine.
- Placez-vous dans le dossier contenant `main.py`.

### ▶Commande d'exécution
```bash
python3 main.py <nom_magasin> <nom_serveur> <articles>
```

**Exemple :**
```bash
python3 main.py "BUT Market" "Lisa" "C01:10|C02:2"
```

---

## Fonctionnement

### 1. Paramètres obligatoires
- `<nom_magasin>` : Nom du magasin affiché sur le ticket.
- `<nom_serveur>` : Nom du serveur ou caissier affiché sur le ticket.
- `<articles>` : Liste des articles achetés, au format spécifique.

### 2. Format des articles
- Un seul article : `code:quantite`  
  Exemple :
  ```text
  C01:6
  ```
- Plusieurs articles : séparez-les par `|`  
  Exemple :
  ```text
  C01:10|C02:2|C03:1
  ```

### 3. Articles disponibles

| Code | Description      | Poids   | Prix (€) | TVA (%) | Origine     |
|------|------------------|---------|----------|---------|-------------|
| C01  | pack de coca     | 2kg     | 5        | 20      | Lituanie    |
| C02  | kilo de pdt      | 1kg     | 1        | 10      | Espagne     |
| C03  | pack Biscotte    | 950g    | 2        | 10      | France      |
| C04  | Café soluble     | 250g    | 3        | 10      | Roumanie    |
| C05  | Crakers          | 125g    | 4        | 20      | Angleterre  |
| C06  | Eau              | 1.5L    | 6        | 10      | Suisse      |
| C07  | Pain             | 250g    | 1        | 10      | France      |

### 4. Calculs réalisés
- Total HT (hors taxes)
- Total TVA (selon taux de chaque produit)
- Total TTC (toutes taxes comprises)

### 5. Résultat
- Un fichier `ticket2.txt` est généré avec le ticket de caisse formaté.

---

## Ajout de Produits

Pour ajouter un produit à la liste :

1. Ouvrez le fichier `main.py`.
2. Repérez la section suivante :
```python
articles = {
    "C01": {"desc": "pack de coca", "poids": "2kg", "prix": 5, "tva": 20, "origine": "Lituanie"},
    ...
}
```
3. Ajoutez une nouvelle ligne avec un code unique, une description, un poids, un prix, un taux de TVA et une origine.

**Exemple :**
```python
"C08": {"desc": "Jus d'orange", "poids": "1L", "prix": 3, "tva": 10, "origine": "France"}
```

---

## Gestion des Erreurs

- Si un code article est inconnu ou une quantité est nulle, l'article est ignoré.
- Si le format d'un article est incorrect (`code:quantite`), il est ignoré avec un message d'avertissement.

---

## Exemple de Ticket Généré

```text
--------------------------------------------------------------------------------
BUT Market
Ticket numéro : 1234
Date : 01/10/2025
Vous avez été servi par : Lisa

NB Desc.           Poids unitaire Poids total HT unitaire TVA Total
10 pack de coca    2kg            10x2kg       5€           20% 60.0€
2  kilo de pdt     1kg            2x1kg        1€           10% 2.2€

                                                  Total HT 52€
                                                  Total TVA 5.2€
                                                  Total     57.2€
--------------------------------------------------------------------------------
```

---

## Auteur

- Script réalisé dans le cadre d’un projet pédagogique.
- Pour toute modification, reportez-vous aux commentaires dans le code source.
