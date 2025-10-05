# tpiut
TP sur la gestion de projet niveau IUT


## Description

Ce programme permet de générer un ticket de caisse en ligne de commande.  
Vous pouvez créer un ticket en entrant le nom du magasin, le nom du vendeur et la liste des articles achetés avec leurs quantités.  
Le ticket est affiché au format classique dans la console.


### Création d'un ticket

Lancez le programme en ligne de commande, en respectant la syntaxe suivante :

```bash
python3 main.py "Nom Magasin" "Vendeur" "C01:QTE|C02:QTE|..."
```

### Liste des produits disponibles

| Code | Description      | Poids/Volume | Prix HT | TVA   |
|------|------------------|--------------|---------|-------|
| C01  | pack de coca     | 2kg          | 5€      | 20 %  |
| C02  | kilo de pdt      | 1kg          | 1€      | 10 %  |
| C03  | pack Biscotte    | 950g         | 2€      | 10 %  |
| C04  | Café soluble     | 250g         | 3€      | 10 %  |
| C05  | Crakers          | 125g         | 4€      | 20 %  |
| C06  | Eau              | 1.5L         | 6€      | 10 %  |
| C07  | Pain             | 250g         | 1€      | 10 %  |


### Règles de saisie

- **Nom du magasin** et **vendeur** : uniquement des lettres et espaces (pas de chiffres, ni de caractères spéciaux).
- **Articles** : chaque article doit avoir un code valide (voir tableau ci-dessus) et une quantité entière strictement positive.
- **Format obligatoire** : `C01:2|C03:1` (pas de caractères spéciaux, de lettres dans les quantités, ni d’espaces inutiles).
- **En cas d’erreur** : le programme affiche un message d’erreur, la syntaxe attendue, un exemple, et la liste des produits disponibles.


### Comment fonctionne le programme : 

on va lui passer en paramètre la variable nom_de_magasin qui contient le nom du magasin que l'on veut afficher sur le ticket de caisse.

Le programme incrémente de 1 son numéro de ticket après chaque affichage (ce qui permet d'avoir chaque ticket avec un numéro unique).

On va afficher la date du jour qui reprends la commande *datetime.now()* importé via datetime en haut du programme

Le nom du vender/de la vendeuse va être mis dans la variable Vendeur.

on va également lui passer en paramètre l'objet qu'on veut lui acheter (code article:sa quantité|code article2:sa quantité...)

Le programme crée alors un tableau en 5 colonnes qu'il affiche. Il reprend le nombre de fois que vous avez sélectionner le produit, la description du produit (son nom), le prix hors taxe à l'uinté, le pourcentage de la TVA et pour finir le total du prix du produit (quantité * prix + quantité * prix * TVA)

Pour finir, le programme crée un tableau de 3 lignes contenant le prix total de tous les objets de votre ticket hors taxes, puis juste le prix de la TVA de la somme des produits sans le prix inital puis la combinaison des deux prix afin d'avoir le total TTC.


### Exemple de ticket généré

```
Leclerc
Ticket numéro : 2201

Date : 01/10/2025

Vous avez été servi par : José

NB  Desc.           Poids/U  Poids total HT unit. TVA   Total
4   pack de coca    2kg      8.00kg      5€     20%  24.00€
1   Crakers         125g     125g        4€     20%  4.80€

Total HT                           24€
Total TVA                          4.80€
Total                              28.80€
```


### Comment ajouter des produits :

vous trouverez dans le programme nommé main.py à partir de la ligne 5 (PRODUITS) la liste des produits déjà référencés. Si vous voulez ajouter des produits, vous pouvez créer une ligne supplémentaire juste en dessous de la dernière ligne en recopiant le schéma ici présent :
      "CXX": {"description": "blablabla", "prix_ht": X},
Vous pouvez ajouter votre nouveau produit en modifiant les paramètres et en faisant attention d'éviter de créer des doublons de Code d'article (très important) et de description. Vous pouvez avoir le même prix pour différents articles.


### Modifier le taux de TVA

Changez la valeur de la clé `"tva"` pour chaque produit dans `PRODUITS`
par exemple `"tva": 0.20` pour 20%, `"tva": 0.10` pour 10%.



## Auteur

Projet réalisé par Hugo SEVESTRE et Tugdual THEPAUT
