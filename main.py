import sys
from datetime import date
from re import findall

#Initialisation des produits
produit : dict = {
    "C01":["Pack de coca",5,2000,20,"Lituanie"],
    "C02":["Kilo de pdt",1,1000,10,"Espagne"],
    "C03":["Pack biscotte",2,950,10,"France"],
    "C04":["Café soluble",3,250,10,"Roumanie"],
    "C05":["Crackers",4,125,20,"Angleterre"],
    "C06":["Eau",6,1.5,10,"Suisse"],
    "C07":["Pain",1,250,10,"France"]
}

#Lecture du nombrede ticket et vidage du fichier
with open("nb_tickets.txt","r+") as file:
    nb_ticket = file.read()
    file.truncate(1000)

#Vérification des arguments
def verif():
    if len(sys.argv) != 4:
        raise Exception(SyntaxError, "Nombre d'arguments saisie invalide, arguments attendu : \"nom de la société\", \"Nom du vendeur\", \"Cn:nbproduit|Cn:nbproduit\"")

#Traitements des arguments
def traitement_donnees() -> dict:
    arg = findall("C\d{1,3}:\d{1,2}", sys.argv[3])
    liste_achat : dict = {}
    for a in arg:
        liste_achat[a.split(":")[0]] = int(a.split(":")[1])
    return liste_achat

#Mise en forme de tout les produits dans un tableau avec la TVA calculée
def calcul_somme(dict : dict) -> list:
    list = []
    for key, value in dict.items():
        if key in produit:
            total = produit[key][1]*value
            tva = produit[key][3]
            total_tva = total + total*(tva*0.01)
            if key == "C06":
                poids = str(produit[key][2]) + "L"
            else:
                poids = str(produit[key][2]) + "g"
                if int(poids[:-1]) >= 1000:
                    poids = str(int(poids[:-1])/1000) + "Kg"
            poids_total = produit[key][2]*value
            index_poids = 0
            if poids_total >= 1000:
                poids_total : float = poids_total/1000
                index_poids = 1
            list.append([produit[key],value,total,total_tva,poids,poids_total,index_poids])
    return list

#Affichage du ticket
def affichage(liste : list):
    #ticket + 1
    with open("nb_tickets.txt","w") as file:
        file.write(str(int(nb_ticket) + 1))
    #L'on récupère le nom de l'enseigne
    output : str = sys.argv[1]
    #L'on affiche le numéro ainsi que la date et le nom du serveur
    output += "\nTicket numéro : " + nb_ticket + "\n\nDate : " + date.today().strftime("%d/%m/%y") + "\n\nVous avez été servi par : " + sys.argv[2] + "\n"
    total_ht = 0
    total_tva = 0
    #Ici une boucle qui affiche les informations pour chaque produit commandé
    print(output)
    print("{:<5} {:<15} {:<23} {:<20} {:<12} {:<6} {:<15} {:<10}".format("NB","Desc","Poids/volume unitaire","Poids/volume total","HT Unitaire","TVA","Origine","Total"))
    for prod in liste:
        unite = "g"
        total_ht += prod[2]
        total_tva += prod[2]*(prod[0][3]*0.01)
        if prod[0][0] == "Eau":
            unite = "L"
        if prod[6] == 1:
            unite = "Kg"

        print("{:<5} {:<15} {:<23} {:<20} {:<12} {:<6} {:<15} {:<10}".format(str(prod[1]),str(prod[0][0]),str(prod[4]),str(prod[5])+unite,str(prod[0][1]),str(prod[0][3]),str(prod[0][4]),str(prod[3])+"€"))

    #Les grands totaux
    print("\n{:>95} {:>11} \n {:>95} {:>11} \n {:>91} {:>16}".format("Total HT",str(total_ht)+"€","Total TVA",str(total_tva)+"€","Total",str(total_ht + total_tva)+"€"))

    #fermeture du fichier du numéro de ticket
    file.close()

if __name__ == "__main__":
    verif()
    dict_data = traitement_donnees()
    somme = calcul_somme(dict_data)
    affichage(somme)