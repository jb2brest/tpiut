# Ticket de caisse

Script Python qui génère un ticket de caisse dans le terminal à partir d'une liste d'articles préenregistrés.

## Prérequis

- Python 3.x (aucune dépendance externe)

## Utilisation

### Lancement

```bash
python3 main.py "BUT Market" "Lisa" "C01:1|C02:3|C03:4"
```

Les arguments sont, dans l'ordre :

1. le nom du magasin ;
2. le nom du vendeur ;
3. la liste des articles, au format `code:quantité`, séparés par `|`.

### Exemple de résultat

```
┌────────────────────────────────────────────────────────────────────────────────┐
│ BUT Market                                                                     │
│ Ticket numéro : 1000                                                           │
│                                                                                │
│ Date : 16/10/2026                                                              │
│                                                                                │
│ Vous avez été servi par : Lisa                                                 │
│                                                                                │
│ NB  Desc.             Pds/vol. unit.  Pds/vol. total  HT unitaire TVA    Total │
│ 1   Pack de coca      2kg             2kg             5€          20%       6€ │
│ 3   Kilo de pdt       1kg             3kg             1€          10%     3,3€ │
│ 4   Pack de biscotte  950g            3,8kg           2€          10%     8,8€ │
│                                                                                │
│                                                           Total HT         16€ │
│                                                           Total TVA       2,1€ │
│                                                           Total          18,1€ │
└────────────────────────────────────────────────────────────────────────────────┘
```

### Ajouter un article

Les articles sont stockés dans le dictionnaire `dic_article` de `main.py`. Pour en ajouter un, ajoutez une ligne :

```python
"C07": {"description": "Pain", "Poids ou volume unitaire" : "250g" ,"prix HT unitaire": 1, "tva": 0.10},
```

- `description` : nom ou description du produit
- `prix HT unitaire` : prix hors taxe en euros
- `tva` : taux sous forme décimale (`0.10` = 10 %)
- `Poids ou volume unitaire` : poid ou volume du produit pour un seul article