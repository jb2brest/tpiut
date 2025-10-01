# Documentation - Système de Tickets de Caisse

## Description générale

Ce programme Python génère des tickets de caisse pour un magasin. Il prend en entrée le nom du magasin, le nom du vendeur et une liste d'articles, puis affiche un ticket formaté avec les détails de la transaction.

## Prérequis

- Python 3.x
- Un fichier `num_ticket.txt` contenant un numéro de ticket initial (doit exister avant la première exécution)

## Catalogue de produits

Le programme dispose d'un catalogue de 5 produits :

| Code | Description | Prix HT |
|------|-------------|---------|
| C01 | pack de coca | 5€ |
| C02 | kilo de pdt | 1€ |
| C03 | pack Biscotte | 2€ |
| C04 | Café soluble | 3€ |
| C05 | Crackers | 4€ |

# Ajout d'un article
Pour ajouter un article il suffit d'ajouter une ligne en haut du fichier main.py dans la variable produit avec cette syntaxe :

```python
{"code_article":"C01", "description":"pack de coca","poids":"2 kg" , "prix_HT":5, "TVA":"20 %", "origine":"Lituanie" }
```

## Utilisation

### Syntaxe

```bash
python main.py <nom_du_magasin> <nom_du_vendeur> <liste_des_articles>
```

### Paramètres

1. **nom_du_magasin** : Nom du magasin (chaîne de caractères)
2. **nom_du_vendeur** : Nom du vendeur (chaîne de caractères)
3. **liste_des_articles** : Liste des articles au format `CODE:QUANTITE|CODE:QUANTITE|...`

### Exemple

```bash
python main.py "SuperMarché" "Jean Dupont" "C01:2|C03:1|C05:3"
```

Cette commande génère un ticket pour :
- 2 packs de coca
- 1 pack de biscottes
- 3 paquets de crackers

## Format du ticket généré

Le ticket affiche les informations suivantes :

```
<Nom du magasin>
Ticket numéro : <numéro auto-incrémenté>

Date : <date du jour au format JJ/MM/AA>

Vous avez été servi par : <nom du vendeur>

NB    Desc.                HT unitaire  TVA    Total   
<quantité> <description> <prix HT total> 10% <prix TTC>
...

                                   Total HT :   <montant>€
                                   Total TVA :  <montant>€
                                   Total :      <montant>€
```

## Fonctionnement technique

### Fonctions principales

#### `calcule_TVA(prix_ht) -> int`

Calcule le prix TTC à partir du prix HT en appliquant une TVA de 10%.

**Paramètres :**
- `prix_ht` : Prix hors taxes

**Retour :**
- Prix TTC (prix HT × 1.1)

#### `calcul_total(list_article:list)`

Calcule les totaux du ticket (HT, TVA et TTC).

**Paramètres :**
- `list_article` : Liste des articles du ticket

**Retour :**
- Liste contenant 3 lignes formatées : Total HT, Total TVA, Total TTC

### Gestion du numéro de ticket

Le programme utilise un fichier `num_ticket.txt` pour :
1. Lire le numéro du ticket actuel
2. Afficher ce numéro sur le ticket
3. Incrémenter et sauvegarder le nouveau numéro pour la prochaine transaction

### Traitement des articles

Pour chaque article de la commande :
1. Le code et la quantité sont extraits de la chaîne d'entrée
2. Le produit correspondant est recherché dans le catalogue
3. Le prix HT total est calculé (prix unitaire × quantité)
4. Le prix TTC est calculé avec la TVA
5. La ligne est ajoutée au ticket

## Taux de TVA

Le programme applique un taux de TVA fixe de **10%** sur tous les produits.

## Limitations et points d'attention

- Le fichier `num_ticket.txt` doit exister et contenir un nombre valide
- Tous les codes articles doivent exister dans le catalogue
- Les quantités doivent être des nombres entiers
- Le format de la liste d'articles doit être strictement respecté (`CODE:QTE|CODE:QTE`)
- Si un code article n'existe pas, le programme peut planter (pas de gestion d'erreur)

## Exemple de sortie

```
SuperMarché
Ticket numéro : 42

Date : 01/10/25

Vous avez été servi par : Jean Dupont

NB    Desc.                HT unitaire  TVA    Total   
2     pack de coca         10           10%    11.0    
1     pack Biscotte        2            10%    2.2     
3     Crackers             12           10%    13.2    


                                   Total HT :   24€
                                   Total TVA :  2.4€
                                   Total :      26.4€
```
