from typing import List
import datetime as dt
import sys 
from tabulate import tabulate
current_date = dt.date.today()
current_date = current_date.strftime("%d/%m/%Y")



def Entete(entreprise,nom): #fonction pour la mise en place de l'entete
    titre : str =  entreprise #variable pour afficher BUT Market
    f = open('compteur.txt', 'r+') #ouvrir le fichier qui contient le conteur
    nticket = int(f.read().strip())#lire la valeur dans le fichier
    nticket  += 1 #incrémenter le compteur
    f.seek(0) #dire que l'on modifie le premier caractère
    f.write(str(nticket))#écrire la nouvelle valeur
    f.close()#fermer le fichier
    date_du_jour = current_date #variable pour afficher la date du jour
    servi = nom #variable pour afficher le nom de la personne qui à servi
    list =  [titre,nticket, date_du_jour,nom,servi] #list de toute les variables
    return list #renvoie la liste



def separation(liste_produit):
    """Fonction qui sépare les différents produits rentrés en paramètre"""
    produit_separee = liste_produit.split("|")
    return produit_separee



def creation_tableaux():
    """Cette fonction créé le tableau final d'affichage du ticket et calcul les différents totaux"""

    tableau_final = [["NB","Desc.","HT unitaire","TVA","Total"]] #tableau final, le premier element du tableau est l'entête du tableau
    total_HT = 0 #Total du ticket hors tva
    total_TVA = 0 # Total de la TVA du ticket
    total_final = 0 #Total du ticket tva inclus
    tva = "10%" #TVA modifiable (modifier aussi dans le total)


    for i in produit_separee:
        produit = i.split(":")
        if produit[0] == "C01": #on regarde si le premier produit est demandé
            nombre = produit[1]
            description = C01[0]
            prix_HT = C01[1]
            total = prix_HT*(1.1)*int(nombre)
            tableau_final.append([nombre,description,prix_HT,tva,total])


            #Calcul des totaux
            total_HT = total_HT + (prix_HT*int(nombre))
            total_TVA = total_TVA + (int(nombre) * 1.1)
            total_final = total_final + total


        elif produit[0] == "C02": #on regarde si le deuxième produit est demandé
            nombre = produit[1]
            description = C02[0]
            prix_HT = C02[1]
            total = prix_HT*(1.1)*int(nombre)
            tableau_final.append([nombre,description,prix_HT,tva,total])


            #Calcul des totaux
            total_HT = total_HT + (prix_HT*int(nombre))
            total_TVA = total_TVA + (int(nombre) * 1.1)
            total_final = total_final + total


        elif produit[0] == "C03": #on regarde si le troisème produit est demandé
            nombre = produit[1]
            description = C03[0]
            prix_HT = C03[1]
            total = prix_HT*(1.1)*int(nombre)
            tableau_final.append([nombre,description,prix_HT + "€",tva,total])

            #Calcul des totaux
            total_HT = total_HT + (prix_HT*int(nombre))
            total_TVA = total_TVA + (int(nombre) * 1.1)
            total_final = total_final + total


        elif produit[0] == "C04": #on regarde si le quatrième produit est demandé
            nombre = produit[1]
            description = C04[0]
            prix_HT = C04[1]
            total = prix_HT*(1.1)*int(nombre)
            tableau_final.append([nombre,description,prix_HT,tva,total])


            #Calcul des totaux
            total_HT = total_HT + (prix_HT*int(nombre))
            total_TVA = total_TVA + (int(nombre) * 1.1)
            total_final = total_final + total


        elif produit[0] == "C05": #on regarde si le cinquième produit est demandé
            nombre = produit[1]
            description = C05[0]
            prix_HT = C05[1]
            total = prix_HT*(1.1)*int(nombre)
            tableau_final.append([nombre,description,prix_HT,tva,total])


            #Calcul des totaux
            total_HT = total_HT + (prix_HT*int(nombre))
            total_TVA = total_TVA + (int(nombre) * 1.1)
            total_final = total_final + total

    return tableau_final,total_HT,total_TVA,total_final



def affichage():
    #On affiche le tableau des produits grâce à la bibliothèque tabulate
    print(tabulate(tableau_final, 
    tablefmt="grid"))


    #On affiche ensuite les Totaux
    print(f"                                  Total HT : {total_HT} €")
    print(f"                               Total TVA : {total_TVA} €")
    print(f"                                   Total : {total_final} €")



if __name__== "__main__" :
#--------------------------------------affichage en tête avec mise en forme---------------------------------------------------------------
    entreprise : str = sys.argv[1] #récupérer le nom de l'entreprise donner lors de l'éxécution du fichier
    nticket : int = 0 #variable pour le nombre de ticket
    nom : str = sys.argv[2]#récupérer le nom de la fonction donner lors de l'éxécution du fichier
    entete : List = Entete(entreprise,nom) # appel de la fonction de ente pour avoir les 4 premières
    nticket += 1#ajouter = 1 au ticket
    print(entete[0])
    print("Ticket numéro :", entete[1],'\n')
    print("Date :", entete[2],'\n')
    print("Vous avez été servi par :", entete[3],'\n')   

    #--------------------------------------affichage liste produit-------------------------------------------------------------- 
    """ PRODUITS """
    #On instancie les produits disponibles
    C01 = ["pack de coca", 5]
    C02 = ["kilo de pdt", 1]
    C03 = ["pack Biscotte", 2]
    C04 = ["Café soluble", 3]
    C05 = ["Crakers", 4]


    entree = sys.argv[3]#récupération des arguments
    produit_separee = separation(entree) #On commence par séparer les produits
    tableau_final,total_HT,total_TVA,total_final = creation_tableaux() #appel de la fonction création tableau
    affichage() #appel de l'affichage
