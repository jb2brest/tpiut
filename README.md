Générateur de Ticket de Caisse

Ce projet est un simple générateur de ticket de caisse écrit en Python. Il permet de générer un ticket de caisse contenant des informations sur les articles achetés, y compris leur description, quantité, poids/volume unitaire et total, prix HT, TVA, et le total à payer.
Prérequis

    Python 3.x installé sur votre machine.
    Le fichier numero_ticket.txt doit exister dans le même répertoire que le script pour suivre le numéro de ticket. S'il n'existe pas, un numéro de ticket par défaut de 2200 sera utilisé, et un nouveau fichier sera créé.

Installation

    Clonez ou téléchargez ce projet.

    Assurez-vous d'avoir Python 3 installé en exécutant la commande suivante dans votre terminal :

```bash
    python --version
```
Placez-vous dans le répertoire contenant le script avec la commande :

```bash

    cd chemin/vers/le/repertoire
```
Usage

Le script prend trois paramètres principaux :

    Nom du magasin : le nom de votre magasin.
    Nom du caissier : la personne qui vous a servi.
    Liste des articles : une chaîne de caractères décrivant les articles achetés sous la forme code_article:quantité, séparée par des barres verticales | pour plusieurs articles.

Exemple de commande pour générer un ticket :

```bash

python ton_script.py "BUT Market" "Lisa" "C01:1|C02:3|C03:4"
```
Explication :

    BUT Market : le nom du magasin.
    Lisa : le nom de la personne qui vous a servi.
    "C01:1|C02:3|C03:4" : la chaîne de caractères représentant les articles achetés, où :
        C01:1 signifie que vous avez acheté 1 pack de coca.
        C02:3 signifie que vous avez acheté 3 kilos de pommes de terre.
        C03:4 signifie que vous avez acheté 4 packs de biscottes.

Résultat :

Le programme générera un ticket de caisse avec tous les détails comme ci-dessous :

BUT Market
Ticket numéro : 2200

Date : 01/10/2048

Vous avez été servi par : Lisa

NB   Desc.            Poids/volume unitaire Poids/volume total   HT unitaire   TVA    Total
1    pack de coca      2kg                   2kg                 5            20.00%  6.00 €
3    kilo de pdt       1kg                   3kg                 1            10.00%  3.30 €
4    pack Biscotte     950g                  3.8kg               2            10.00%  8.80 €

Total HT                                      16.00 €
Total TVA                                     2.10 €
Total                                         18.10 €

Gestion des erreurs

Le script gère plusieurs erreurs possibles, dont :

    Paramètres manquants : Si vous ne fournissez pas tous les paramètres, un message d'erreur s'affichera pour indiquer le format correct à utiliser.
    Code d'article incorrect : Si un code d'article n'existe pas, un message d'erreur spécifique sera affiché.
    Quantité incorrecte : Si la quantité n'est pas un entier positif, une erreur sera signalée.

Exemple d'erreur :

```bash

python ton_script.py "BUT Market" "Lisa" "C01:-3|C02:3"
```
Cela renverra l'erreur suivante :

rust

Erreur : La quantité pour l'article C01 doit être un entier positif.

Fonctionnalités supplémentaires

    Suivi du numéro de ticket : Le script génère un ticket avec un numéro unique. Le numéro de ticket est incrémenté automatiquement et sauvegardé dans le fichier numero_ticket.txt après chaque génération de ticket.
    Calcul automatique des poids et volumes : Le script gère aussi bien les kilogrammes (kg) que les litres (L) et les grammes (g), et calcule automatiquement le poids ou volume total en fonction de la quantité.
