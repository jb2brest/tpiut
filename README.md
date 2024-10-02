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

Example:

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

Example:

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

Example:

```console
python3 main.py -l

Code article    | Description                    | Price HT   | TVA:
C02             | kilo de pdt                    | 1 euros     | 10 %
C01             | pack de coca                   | 5.0 euros   | 10 %
C03             | pack Biscotte                  | 2.0 euros   | 10 %
C04             | Café soluble                   | 3.0 euros   | 10 %
C05             | Crackers                       | 4.0 euros   | 10 % 
```
