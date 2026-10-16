# Système d'édition de ticket de caisse

Projet IUT : gestion de projet. Binôme : Maël LE GALLO, Markan Le Galliot.

## Lancement

```bash
python3 main.py "<magasin>" "<vendeur>" "<CODE:QUANTITE|CODE:QUANTITE|...>"
```

Exemple :

```bash
python3 main.py "BUT Market" "Lisa" "C01:1|C02:3|C03:4"
```

Résultat :

```
BUT Market
Ticket numéro : 2200

Date : 16/10/2026

Vous avez été servi par : Lisa

NB    Desc.               HT unitaire   TVA    Total
1     pack de coca        5€            10%    5,5€
3     kilo de pdt         1€            10%    3,3€
4     pack Biscotte       2€            10%    8,8€

                                 Total HT      16€
                                 Total TVA     1,6€
                                 Total         17,6€
```

## Fonctionnement

1. Le panier `"C01:1|C02:3"` est découpé : les articles sont séparés par `|`, et le code est séparé de la quantité par `:`.
2. Chaque code est cherché dans le catalogue `produits.csv`.
3. Pour chaque ligne : `Total = prix HT × quantité × (1 + TVA)`.
4. Les totaux HT, TVA et TTC sont calculés en bas du ticket.
5. Le numéro de ticket commence à 2200 et augmente de 1 à chaque ticket. Il est enregistré dans `compteur.txt`. Supprimer ce fichier fait repartir le compteur à 2200.
6. La date affichée est celle du jour.

Les montants sont calculés en `Decimal` pour éviter les erreurs d'arrondi.

## Ajouter ou modifier un produit

Ajouter une ligne dans `produits.csv` (séparateur `;`) :

```
code;description;prix_ht;tva
C06;Jus d'orange;2.5;5.5
```

- `prix_ht` : prix unitaire hors taxe (point ou virgule acceptés)
- `tva` : taux en pourcentage (10 = 10 %)

Le code n'a pas besoin d'être modifié.

## Erreurs gérées

| Cas | Message |
|-----|---------|
| Mauvais nombre d'arguments | Affiche l'aide d'utilisation |
| Code article inconnu (`C99:1`) | `Erreur : Code article inconnu : C99` |
| Quantité non numérique, nulle ou négative | `Erreur : Quantité invalide...` |
| Format sans `:` | `Erreur : Format invalide...` |

Quand le ticket est en erreur, aucun numéro de ticket n'est consommé.

## Tests

```bash
python3 -m unittest -v
```

## Fichiers

| Fichier | Rôle |
|---------|------|
| `main.py` | Programme principal |
| `produits.csv` | Catalogue des articles |
| `compteur.txt` | Dernier numéro de ticket (créé automatiquement) |
| `test_main.py` | Tests unitaires |
