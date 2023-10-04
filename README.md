# tpiut
TP sur la gestion de projet niveau IUT

# Description

Ce programme permet de générer un ticket de caisse.
Il effectue les calculs de prix en fonction des variables attribuées.


# Comment utiliser le programme?

Voici comment utiliser 

```
python3 ticket.py <"nom du magasin"> <"Nom du vendeur/se"> <"n°série A:nbr_articles A | n°série B:nbr_articles B">
```

Voici un exemple d'utilisation :

```
Python3 main.py “But Market” “Lisa” “C01:10|C02:2”
```

qui affiche en sortie :

![resultat](images\resultat.png)


# Comment est initialisée la base de données

|Code article|Description|Prix HT unitaire | TVA |
| :--------: | :-------:  | :------------: | :--: |
|    C01     |pack de coca  | 5 | 10% |
|    C02     |kilo de pdt   | 1 | 10% |
|    C03     |pack Biscotte | 2 | 10%|
|    C04     |Café soluble  | 3 |10% |
|    C05     |Crakers       | 4 | 10% |

# Comment modifier la base de données

Afin de modifier la base de donnée, il vous faudra ouvrir le fichier main.py
à la 5ème ligne vous trouverez "produit".
Ajoutez en dessous de cette ligne le produit que vous souhaitez en respectant la nomenclature tel que :

```
"Code d'article":[Description du produit, prix du produit],
```
ATTENTION A NE PAS OUBLIER LA VIRGULE