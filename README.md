# Documentation

## Table des matières

* [Gestion des items](#gestion-des-items)
  * [Ajouter un item](#ajouter-un-item)
  * [Supprimer un item](#supprimer-un-item)
  * [Lister les items](#lister-les-items)
* [Création d'un ticket](#création-dun-ticket)

## Gestion des items

### Ajouter un item

Pour ajouter un item, il faut executer la commande suivante :

```console
python3 main.py -a -c "Code article" -d "description" -p prix -w poids -u unité -tva tva
```

* `-a`  : Permet d'ajouter un item
* `-c`  : Code de l'article
* `-d`  : Description de l'article
* `-p`  : Prix de l'article
* `-w`  : Poid de l'article
* `-u`  : Unité de mesure du poid(Kg, L, etc...)
* `-tva`: La valeur de la tva en pourcentage

Celui-ci sera ajouté à la base de données. (Fichier `items.json`)

Exemple:

```console
# Ajout d'un item qui n'existe pas encore
python3 main.py -a -c "C01" -d "pack de coca" -p 5 -w 2 -u Kg -tva 20

Added item: C01 - pack de coca - 5

# Ajout d'un item qui existe déjà
python3 main.py -a -c "C01" -d "pack de coca" -p 5 -w 2 -u Kg -tva 20

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

Code article    | Description                    | Price HT   | TVA:  | Weight:
C02             | kilo de pdt                    | 1 euros    | 10 %  | 1 kg
C01             | pack de coca                   | 5.0 euros  | 20 %  | 2 kg
C03             | pack Biscotte                  | 2.0 euros  | 10 %  | 0.95 kg
C04             | Café soluble                   | 3.0 euros  | 10 %  | 0.25 kg
C05             | Crackers                       | 4.0 euros  | 20 %  | 0.125 kg
C07             | Pain                           | 1 euros    | 10 %  | 0.250 Kg
C06             | Eau                            | 6 euros    | 10 %  | 1.5 L
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

IUT Lannion
Ticket numéro :50

Date : 02/10/2024 11:28:20

Vous avez été servi par : Alexis

NB      Desc.                   Poid unitaire   Poid total  Prix HT unitaire    TVA     Total
2       pack de coca            2kg             4.0kg       5.0 €               20%     12.0€
4       kilo de pdt             1kg             4.0kg       1 €                 10%     4.4€
12      pack Biscotte           0.95kg          11.4kg      2.0 €               10%     26.4€
1       Café soluble            0.25kg          0.25kg      3.0 €               10%     3.3€
12      Crackers                0.125kg         1.5kg       4.0 €               20%     57.6€
42      Eau                     1.5L            63.0L       6 €                 10%     277.2€
2       Pain                    0.250Kg         0.5Kg       1 €                 10%     2.2€

                                                                                 Total HT : 343.0
                                                                                 Total TVA : 40.1
                                                                                 Total :     383.1
```
