import sys,datetime,os

def database(prod : str)-> list :
    """
    base de donnée, permet de retourner la liste des infos d'un produit 
    Param : 
    prod -> référence d'un produit (ex : C01)
    """
    base = {'C01':['Pack de Coca',5],
                'C02':['Kilo de pdt',1],
                'C03':['Pack de Biscottes',2],
                'C04':['Café Soluble',3],
                'C05':['Crackers',4]
                }
    li_return = [prod]
    for item in base[prod] :
        li_return.append(item)

    return li_return


def produits()-> dict:
    """
    lecture du 3ème arguments (produits) et retourne un dictionnaire : {produit : [desc, qte, prix_ht ,total_ht]}
    """
    li_prod = sys.argv[3].split('|')
    dico_produits = {}
    for item in li_prod :
        prod = item.split(':')
        dico_produits[prod[0]]=[f'{database(prod[0])[1]}',f'{prod[1]}',f'{database(prod[0])[2]}',f'{database(prod[0])[2]*int(prod[1])}']
    return dico_produits

def lire_txt()-> str:
    """
    Fonction qui permet de lire la valeur d'un fichier texte contenant le numéro de ticket actuel
    """
    fichier = open('nb_ticket.txt','r')
    nb = fichier.read()
    fichier.close()
    return nb

def modif_txt():
    """
    Fonction qui permet d'ajouter 1 au fichier contenant le numéro de ticket actuel
    """
    val_fic = int(lire_txt())
    fichier = open('nb_ticket.txt','w+')
    fichier.write(f'{val_fic+1}')
    fichier.close()


def Ticket_caisse():
    """
    Fonction de mise en forme du ticket
    """
    nom_mag = sys.argv[1]    #Nom du magasin -> lecture argument 1
    hote = sys.argv[2]       #Nom de l'hôte de caisse -> lecture argument 2
    date = datetime.date.today()

    #Date
    modif_txt()
    nb_ticket=lire_txt()

    #Produits 
    dico_produits = produits()

    #Print entete du ticket
    print(f"\n{nom_mag}\nTicket numéro : {nb_ticket}\n\nDate : {date}\nVous avez été servi par : {hote}\n")

    #Print produits 
    print(f"{'NB':<3} {'Desc':<20} {'HT unitaire':<15} {'TVA':<5} {'Total':<10}")
    for item in dico_produits :
        print(f"{dico_produits[item][1]:<3} {dico_produits[item][0]:<20} {dico_produits[item][2]:<15} {'10%':<5} {round(float(dico_produits[item][3])*1.1,2):<10}")
    print("\n")

        
    

if __name__ == "__main__" :
    #Programme principal
    Ticket_caisse()

