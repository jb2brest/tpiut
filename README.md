# Générateur de Tickets de Caisse (Projet Python)

Projet développé dans le cadre du module IUT. Ce programme en ligne de commande permet de générer un ticket de caisse formaté à partir d'un catalogue d'articles et d'une commande passée en argument.

## Structure du projet

- `main.py` : script principal qui génère et affiche le ticket de caisse
- `test.py` : script de test unitaire simple pour vérifier le catalogue et les calculs de TVA
- `README.md` : documentation du projet

## Catalogue des articles

Le catalogue contient 5 articles prédéfinis avec une TVA fixée à 10 % :

| Code | Description    | Prix HT | TVA |
|------|----------------|---------|-----|
| C01  | Pack de coca   | 5.0 €   | 10% |
| C02  | Kilo de pdt    | 1.0 €   | 10% |
| C03  | Pack Biscotte  | 2.0 €   | 10% |
| C04  | Café soluble   | 3.0 €   | 10% |
| C05  | Crakers        | 4.0 €   | 10% |

## Utilisation

### 1. Générer un ticket (`main.py`)

Le script prend 3 arguments en ligne de commande :

1. Nom du magasin
2. Nom du caissier
3. Contenu de la commande au format `CODE:QUANTITÉ|CODE:QUANTITÉ`

Exemple de commande :

```bash
python main.py "Mon Magasin" "Hugo" "C01:2|C02:3|C03:1"
```

Exemple de résultat dans la console :

```text
Mon Magasin
Ticket numéro : 2200
Date : 16/10/2026

Vous avez été servi par : Hugo

NB   Desc.           HT unitaire  TVA    Total 
2    pack de coca    5€           10%    11€   
3    kilo de pdt     1€           10%    3€    
1    pack Biscotte   2€           10%    2€    

                    Total HT        15€
                    Total TVA       1.5€
                    Total           16€
```

### 2. Lancer les tests (`test.py`)

Pour vérifier la validité des prix et la justesse des calculs du programme :

```bash
python test.py
```

Si tout fonctionne correctement, le terminal affichera :

```text
TEST RÉUSSI : Le catalogue et les calculs fonctionnent parfaitement !
```
