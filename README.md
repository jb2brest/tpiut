**<h1>Mode opératoire</h1>**

**<h2>Exécution du programme</h2>**

1 - Lancer Visual studio code sur le poste de travail.

2 - Aller en haut à droite dans l'onglet [ file > Open File > Sélectionner le programme "code_ticket"]

3 - Aller dans le répertoire où vous avez enregistré le programme puis sélectionné le.

4 - Une fois ouvrer, il faut sélectionner l'onglet terminal en-haut > New Terminal

5 - Pour exécuter le script dans le terminal la commande suivante : 

``` python /<chemin ver le répertoires dans le quel le programme se trouve>/code_ticket.py <Nom_du_ticket> <Nom de la personne> <"ID du produit : quantité ,ID du produit : quantité>```

---------------------------------------------------------------

**<h2>Fonctionnement du produit</h2>**

1 - mettre les fichiers csv dans le même répertoire que le code

2 - Fonction recup_csv : permet de récupérer le contenu d'un fichier sous la forme string (chaîne de caractère). La fonction transforme cette chaîne en liste, en fonction de la localisation des virgules dans le tableau csv. Renvoie une liste de liste avec chacun des éléments du fichier csv.

3 - Fonctione recup_elem : La fonction permet de récupérer les éléments de la liste qui nous intéresse, en comparant l'id du produit demandé et celui présent dans la liste.

4 - Fonction calcul_tva : La fonction permet de calculer le prix des produits selon la TVA et la quantité du produit. Elle permet également de mettre à jour les valeurs totales qui nécessite de prendre en compte tous les produits.

5 - Fonction calcul_totaux : La fonction permet de récupérer les différentes valeurs calculées dans la fonction précédente.

6 - Fonction ticket : La fonction réalise l'affichage des informations calculées à l'aide des autres fonctions. Elle calcul également la date.

---------------------------------------------------------------

**pour l'éventuels ajouts de produits, il faut les ajoutés aux documents CSV**
