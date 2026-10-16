# Ticket de caisse

Script Python qui génère un ticket de caisse dans le terminal à partir d'une liste d'articles préenregistrés.

## Prérequis

- Python 3.x (aucune dépendance externe)

## Utilisation

### Lancement

```bash
python3 main.py "Magasin" "Vendeur" "C01:10|C02:2"
```

Les arguments sont, dans l'ordre :

1. le nom du magasin ;
2. le nom du vendeur ;
3. la liste des articles, au format `code:quantité`, séparés par `|`.

### Exemple de résultat

```
┌──────────────────────────────────────────────────┐
│ Magasin                                          │
│ Ticket numéro : 1000                             │
│                                                  │
│ Date : 16/10/2026                                │
│                                                  │
│ Vous avez été servi par : Vendeur                │
│                                                  │
│ NB  Desc.             HT unitaire  TVA     Total │
│ 10  Pack de coca      5€           10%       55€ │
│ 2   Kilo de pdt       1€           10%      2,2€ │
│                                                  │
│                             Total HT         52€ │
│                             Total TVA       5,2€ │
│                             Total          57,2€ │
└──────────────────────────────────────────────────┘
```

### Ajouter un article

Les articles sont stockés dans le dictionnaire `dic_article` de `main.py`. Pour en ajouter un, ajoutez une ligne :

```python
"C03": {"description": "Nom de l'article", "prix HT unitaire": 12.50, "tva": 0.10},
```

- `prix HT unitaire` : prix hors taxe en euros
- `tva` : taux sous forme décimale (`0.10` = 10 %)