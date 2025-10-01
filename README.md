# tpiut
TP sur la gestion de projet niveau IUT

##Document fait par Tugdual THEPAUT et Hugo SEVESTRE


###Lancement du programme

Pour lancer le programme, il suffit de taper la commande **Python3 main.py "***Nom de Magasin***" “***Vendeur***” “***C01:10|C02:2***”**


###Comment fonctionne le programme : 

on va lui passer en paramètre la variable nom_de_magasin qui contient le nom du magasin que l'on veut afficher sur le ticket de caisse.

Le programme incrémente de 1 son numéro de ticket après chaque affichage (ce qui permet d'avoir chaque ticket avec un numéro unique).

On va afficher la date du jour qui reprends la commande *datetime.now()* importé via datetime en haut du programme

Le nom du vender/de la vendeuse va être mis dans la variable Vendeur.

on va également lui passer en paramètre l'objet qu'on veut lui acheter (code article:sa quantité|code article2:sa quantité...)

Le programme crée alors un tableau en 5 colonnes qu'il affiche. Il reprend le nombre de fois que vous avez sélectionner le produit, la description du produit (son nom), le prix hors taxe à l'uinté, le pourcentage de la TVA et pour finir le total du prix du produit (quantité * prix + quantité * prix * TVA)

Pour finir, le programme crée un tableau de 3 lignes contenant le prix total de tous les objets de votre ticket hors taxes, puis juste le prix de la TVA de la somme des produits sans le prix inital puis la combinaison des deux prix afin d'avoir le total TTC.


###Comment ajouter des produits :

vous trouverez dans le programme nommé main.py à partir de la ligne 5 (PRODUITS) la liste des produits déjà référencés. Si vous voulez ajouter des produits, vous pouvez créer une ligne supplémentaire juste en dessous de la dernière ligne en recopiant le schéma ici présent :
      "CXX": {"description": "blablabla", "prix_ht": X},
Vous pouvez ajouter votre nouveau produit en modifiant les paramètres et en faisant attention d'éviter de créer des doublons de Code d'article (très important) et de description. Vous pouvez avoir le même prix pour différents articles.
