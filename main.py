from typing import List
import datetime as dt
import sys 
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