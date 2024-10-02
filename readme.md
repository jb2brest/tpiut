<!-- 
Groupe 3A1
BOEZ Lucas
CHICHEPORTICHE Axel

TP Cycle De Vie D'Un Projet

La documentation permettre de comprendre comment utiliser notre produit (lancement, fonctionnement, ajout de produits,...)

lot 3 -->

L'objectif du programme main.py est la réalisation d'un programme d'un systeme d'édition de ticket de caisse.


Pour permettre la comprhension de notre documentation, nous allons utiliser l'exemple d'une commande d'exécution du programme suivant :

python3 .\main.py "But Maket" "Lisa" "C01:10|C02:2" 
(si il y a une erreur "Python est introuvable. ExÚcutez sans argument pour procÚder Ó l" utiliser py à la place de python3)

Le programme prends en compte 3 variables en entrée.

La première est le nom du supermarché, ici `"BUT Market"`. La deuxième est le nom du vendeur `"Lisa"` et pour la troisième, on rentre les `"items"` que l'on veut ajouter ainsi que la quantité. Pour la troisième variable, on reprend les items dans le tableau ci dessous :

Pour pouvoir exécuter le programme, vous devez au préalable posséder un logiciel d'éditeur de code comme Vscode, Thonny, Spider, ...
Dans notre cas nous allons détailler la façon de faire sur VS Code.

Après avoir lancé l'application, pour que se soit plus simple, vous pouvez ouvrir le dossier dans lequel ce trouve les fichiers téléchargés avec l'onglet `"File"` en haut à gauche puis `"Open folder"` et choisir le dossier.

Maintenant que le dossier est ouvert, vous devez vous déplacer dans le fichier `"main.py"`. A partir de là, vous pouvez ouvrir un terminal où vous pourrez exécuter le programme.

Pour cela, il vous suffit simplement de cliquer sur `"Terminal` puis `"New Terminal"`.
Ensuite, vous pouvez commencer à tester le code. Pour pouvoir le faire, vous devez saisir dans le terminal les commandes suivantes :


Ne pas oublier de vérifier d'être bien placé dans le dossier ou ce trouve le programme avant de l'éxécuter à l'aide du chemin afficher dans le terminal.


py3.\main.py   "But Maket" "Lisa" "C01:10|C02:2" 

Le résultat qui doit être renvoyé est le suivant :

Résultat:

But Maket
Ticket numéro : 16 

Date : 01/10/2024

Vous avez été servi par : Lisa


 NB Desc.         HT unitaire  TVA  Total 
 10  pack de coca  5            10% 55.0  
 2   kilo de pdt   1            10%  2.2   

Total HT : 52 €
Total TVA : 13.2 €
Total : 57.2 €









