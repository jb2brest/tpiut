#Ticket de caisse

import sys
import datetime

numero:int = 1
date = datetime.date.today()
date = date.strftime("%d-%m-%Y") #Affiche la date comme ça "jour-mois-année"
input:str = sys.argv[1:] #Prend les arguments qu'il y a après qu'on lance le programme
Articles:dict = {}


def ajout_article(code:str,description:str,poids_unitaire:int, volume:str, prixHT:int, TVA:int, origine:str)-> list:
    Articles[code]=[description,poids_unitaire, volume, prixHT, TVA, origine]

def string_To_liste_of_tuple(value:str)->list:
   retoure:list=[]
   commande=value.split("|")
   for val in commande:
      code_quantite=val.split(":")
      code=code_quantite[0]
      quantite=int(code_quantite[1])
      retoure.append((code, quantite))
   return retoure



def affiche_tableau(list_value:tuple)->None:
    # Affiche les informations concernant le tableau
    print("NB\t", end=" ")
    print("Desc.\t\t", end=" ")
    print("Pds/vol.unitaire\t", end=" ")
    print("Pds/vol.total\t", end=" ")
    print("Orig\t", end=" ")
    print("HT unitaire\t", end=" ")
    print("TVA	Total")

    montant_prix_total  : float = 0
    montant_TVA_total   : float = 0
    montant_prix_TVA    : float = 0

    # Pour chaque article selectionné
    for value in list_value:

        # Si cette article existe dans le dictionnaire article
       if value[0] in list(Articles):
          
          produit_nombre         = value[1]
          produit_description    = Articles[value[0]][0]
          produit_volume         = Articles[value[0]][2]
          produit_poids          = Articles[value[0]][1]
          produit_poids_Total    = produit_poids*produit_nombre
          produit_origine        = Articles[value[0]][5]
          produit_prix_unitaire  = Articles[value[0]][3]
          produit_TVA            = Articles[value[0]][4]
          produit_prix_total     = produit_prix_unitaire*produit_nombre
          produit_prix_total_TVA = produit_prix_unitaire*produit_nombre*(produit_TVA/100+1)

          # Affiche le nombre d'article
          print(f"{produit_nombre}\t", end=" ")
          # Affiche la déscription de l'article
          print(f"{produit_description}\t\t", end=" ")
          # Affiche le volume et poids       
          print(f"{produit_poids}{produit_volume}\t\t\t", end=" ")
          # Affiche le volume et poids total
          print(f"{produit_poids_Total}{produit_volume}\t", end=" ")
          # Affiche l'origine
          print(f"{produit_origine}\t\t", end=" ")
          # Affiche le prix unitaire
          print(f"{produit_prix_unitaire}€\t", end=" ")
          # Affiche le montant de la TVA
          print(f"{produit_TVA}%\t", end=" ")
          # Affiche le prix total après TVA
          print(f"{produit_prix_total_TVA:.2f}€")

          montant_prix_total += produit_prix_total
          montant_TVA_total  += produit_prix_total_TVA-produit_prix_total
          montant_prix_TVA   += produit_prix_total_TVA
          

    # Affiche le montant total de la commande
    print()
    decalage="\t\t\t\t\t\t\t\t\t\t"
    print(f"{decalage}Total HT\t{montant_prix_total:.2f}€")
    print(f"{decalage}Total TVA\t{montant_TVA_total:.2f}€")
    print(f"{decalage}Total\t\t{montant_prix_TVA:.2f}€")


# Initialise le dictionaire Article
ajout_article("C01","pack de coca",2,"kg",5,20,"Lituanie")
ajout_article("C02","kilo de pdt",1,"kg",1,10,"Espagne")
ajout_article("C03","pack Biscotte",950,"g",2,10,"France")
ajout_article("C04","Café soluble",250,"g",3,10,"Roumanie")
ajout_article("C05","Crakers",125,"g",4,20,"Angleterre")
ajout_article("C06","Eau\t",1.5,"L",6,10,"Suisse")
ajout_article("C07","Pain\t",250,"g",1,10,"France")

if not input :
 print("Exemple:")
 print("Python3 main.py “But Maket” “Lisa” “C01:10|C02:2”")
 sys.exit(1)

print(input[0])
print("Ticket numéro :",numero,"\n")
print("Date :",date,"\n")
print("Vous avez été servi par :",input[1],"\n") #Affiche le nom sans les crochets

try:
    affiche_tableau(string_To_liste_of_tuple(input[2]))
except ValueError:
   print("ERREUR: L'affichage du tableau n'à pas pu être réalisé")
   print("        La valeur selectionné doit etre le code du produit suivi d'un chiffre pour la quantité !!")
   print("        EXEMPLE: C01:10|C02:4")
except:
   print("Il y à eu une erreur lors de l'affichage")
