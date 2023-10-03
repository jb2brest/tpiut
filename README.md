# tpiut
TP sur la gestion de projet niveau IUT

# Récupération du Projet
git clone <project>

# Code_Article Description              
C01 "pack de coca"
C02 "kilo de pdt"
C03 "pack Biscotte"
C04 "Café soluble"
C05 "Crakers"

# Récupération du Projet
2ème étape : lancer la commande <python3 main.tf "NOM_ENTREPRISE" "NOM_CAISSIER" "C01:4|C02|2">
Dans le 3ème argument, on ajoute autant de article que l'on veut, en les séparant par des '|'. Dans chaque article, on précise le Code_Article et le nombre d'article.

# Execution du code
$ python3 main.py "Mcdo" "Lisa" "C01:10|C02:2|C04:4"
Mcdo
Ticket numéro : 1002

Date : 03/10/2023

Vous avez été servi par Lisa

NB	Desc.		      HT unitaire	TVA	 Total
10	pack de coca	5		        10%	 55.0€
2	  kit de pft	  1		        10%	 2.2€
4	  Café soluble	3		        10%	 13.2€

                     TOTAL HT          64€
                     TOTAL TVA         6.4€
                     TOTAL             70.4€
