import sys
from datetime import date
from re import findall

produit : dict = {
    "C01":["Pack de coca",5],
    "C02":["Kilo de pdt",1],
    "C03":["Pack biscotte",2],
    "C04":["Café soluble",3],
    "C05":["Crackers",4]
}

with open("nb_tickets.txt","r+") as file:
    nb_ticket = file.read()
    file.truncate(1000)

def verif():
    if len(sys.argv) != 4:
        raise Exception(SyntaxError, "Nombre d'arguments saisie invalide, arguments attendu : \"nom de la société\", \"Nom du vendeur\", \"Cn:nbproduit|Cn:nbproduit\"")

def traitement_donnees() -> dict:
    arg = findall("C\d{1,3}:\d{1,2}", sys.argv[3])
    liste_achat : dict = {}
    for a in arg:
        liste_achat[a.split(":")[0]] = int(a.split(":")[1])
    return liste_achat

def calcul_somme(dict : dict) -> list:
    list = []
    for key, value in dict.items():
        if key in produit:
            total = produit[key][1]*value
            total_tva = total + total*0.1
            list.append([produit[key],value,total,total_tva])
    return list

def affichage(liste : list):
    with open("nb_tickets.txt","w") as file:
        file.write(str(int(nb_ticket) + 1))
    output : str = sys.argv[1]
    output += "\nTicket numéro : " + nb_ticket + "\n\nDate : " + date.today().strftime("%d/%m/%y") + "\n\nVous avez été servi par : " + sys.argv[2] + "\n\nNB\tDesc\t\tHT Unitaire\tTVA\tTotal\n"
    total_ht = 0
    for prod in liste:
        total_ht += prod[2]
        output += str(prod[1]) + "\t" + prod[0][0] + "\t" + str(prod[0][1]) + "\t\t10%" + "\t" + str(prod[3]) + "€\n"
    output += "\n\t\t\t\tTotal HT\t" + str(total_ht)
    output += "\n\t\t\t\tTotal TVA\t" + str(total_ht*0.1)
    output += "\n\t\t\t\tTotal\t\t" + str(total_ht + total_ht*0.1)

    file.close()
    print(output)

if __name__ == "__main__":
    verif()
    dict_data = traitement_donnees()
    somme = calcul_somme(dict_data)
    affichage(somme)