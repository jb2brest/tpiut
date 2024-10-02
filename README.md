# Documentation

## Table des matières

## Gestion des items


### Ajouter un item

Pour ajouter un item, il faut executer la commande suivante :

```console
python3 main.py -a -c "Code article" -d "Description" -p "Prix"
```

* `-a` : Permet d'ajouter un item
* `-c` : Code de l'article
* `-d` : Description de l'article
* `-p` : Prix de l'article

Celui-ci sera ajouté à la base de données. (Fichier `items.json`)

Exemple:

```console
# Ajout d'un item qui n'existe pas encore
python3 main.py -a -c "C01" -d "pack de coca" -p 5

Added item: C01 - pack de coca - 5

# Ajout d'un item qui existe déjà
python3 main.py -a -c "C01" -d "pack de coca" -p 5

Item C01 already exists
```

### Supprimer un item

Pour supprimer un item, il faut executer la commande suivante :

```console
python3 main.py -d -c "Code article"
```

* `-d` : Permet de supprimer un item
* `-c` : Code de l'article

Celui-ci sera supprimé de la base de données. (Fichier `items.json`)

Exemple:

```console
# Suppression d'un item qui existe
python3 main.py -r -c "C01"

Removed item: C01

# Suppression d'un item qui n'existe pas
python3 main.py -r -c "C01"

Item C01 not found
```

### Lister les items

Pour lister les items, il faut executer la commande suivante :

```console
python3 main.py -l
```

Exemple:

```console
python3 main.py -l

Code article    | Description                    | Price HT   | TVA:
C02             | kilo de pdt                    | 1 euros     | 10 %
C01             | pack de coca                   | 5.0 euros   | 10 %
C03             | pack Biscotte                  | 2.0 euros   | 10 %
C04             | Café soluble                   | 3.0 euros   | 10 %
C05             | Crackers                       | 4.0 euros   | 10 %
```
## Création d'un ticket

Pour créé un nouveau ticket, il faut executer la commande suivante :
```console
main.py -t -n "nom_caissier" -m "nom_magasin" -i "id_produit1:quantité|id_produit2:quantité|..."
```

* `-t` : Permet de créé un ticket
* `-n` : Permet d'indiqué le caissier qui à servis le client
* `-m` : Permet d'indiqué le magasin où l'achat à été éffectuer
* `-i` : Permet d'indiqué les produits acheté et leur quantités

Exemple:

```console
main.py -t -n "Alexis" -m "IUT Lannion" -i "C01:2|C04:4"
IUT Lannion
Ticket numéro :19

Date : 02/10/2024 10:18:51

Vous avez été servi par : Alexis

NB      Desc.                   HT unitaire     TVA     Total
2       pack de coca            5.0 €           10%     12.0€
4       Café soluble            3.0 €           10%     14.4€

                                                Total HT : 22.0
                                                Total TVA : 4.4
                                                Total : 26.4
```
