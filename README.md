# tpiut
TP sur la gestion de projet niveau IUT

# Récupération du Projet
git clone PROJET

# Récupération du Projet
2ème étape : lancer la commande <python3 main.tf "NOM_ENTREPRISE" "NOM_CAISSIER" "C01:4|C02|2">

Dans le 3ème argument, on ajoute autant de article que l'on veut, en les séparant par des '|'.

Dans chaque article, on précise le Code_Article et le Nombre_article avec le ':'

Si je veux 6 pack de coca et 2 Crackers je ferai ceci : "C01:6|C05:2"

# Execution du code
![image info](exec2.png)

# Changer le prix produit - ajout produit - origine - poids et unité
Dans la fonction middle_ticket() que l'on peut voir ci-dessous. On a la possibilité modifier le prix correspondant.
Si vous avez besoin d'un nouveau produit, ajouter ceci : 
```py
elif code_article == "CodeArticle":
    description = "Votre description"
    origine = "Corée du Sud"
    poids_volume = 125
    unite = "g"
    prix = 100 # changer le prix, si vous le souhaiter
```

![image info](mid.png)

# Changer la TVA
![image info](tva.png)
