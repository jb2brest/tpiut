from datetime import datetime
import csv
import sys
import random
import re

num_ticket=random.randint(1,9999)
nom="moi"

"""Tri des arguments"""
nom_ticket = str(sys.argv[1])
nom_utilisateur = str(sys.argv[2])
liste=sys.argv[3].split("|")
liste2=[]
for i in range(len(liste)):
    liste2+=[liste[i].split(":")]


def recup_csv(nom_csv):
    """
    Le nom du fichier est en paramètre et est ouvert.
    On demande la séparation des éléments à l'apparition de chaque ','. 
    On créer donc une liste pour chaque ligne du CSV.
    On renvoie les données sous la forme de liste.
    """
    fichier = open(nom_csv,"r")
    cr = csv.reader(fichier,delimiter=",")
    texte2=[]
    for ligne in cr:
        texte = str(len(ligne)) + ":"
        for i in range(len(ligne)):
            texte = texte + "|"+ ligne[i]+"|"
        texte2+=[texte.split("|")]
    return(texte2)

def recup_elem(csv,liste2):
    """
    En paramètre se trouve le fichier CSV sous la forme de liste de liste et 
    """
    global liste3
    liste3=[]
    for i in range(len(liste2)):
        for j in range(len(csv)):
            if liste2[i][0] == csv[j][1]:
                liste3+=[csv[j]]
    return liste3

valeur_tva=0
ht_unitaire_glob=0
total_glob=0
def calcul_tva(ht_unitaire,nb,tva):
    """
    Les paramètres sont la quantité et le prix du produit demandés.
    On globalise les calculs des totaux.
    """
    global valeur_tva
    global ht_unitaire_glob
    global total_glob
    total=ht_unitaire*(1.0+int(tva))*int(nb)
    valeur_tva+=total-(ht_unitaire*int(nb))
    ht_unitaire_glob+=ht_unitaire*int(nb)
    total_glob+=total
    return total

def calcul_totaux():
    """
    Organiser et envoyer les totaux calculer dans le calcul TVA
    """
    return [valeur_tva,ht_unitaire_glob,total_glob]

    
def ticket():
    """
    Affichage du ticket.
    Calcule de la date.
    """
    print(nom_ticket)
    print(f"Ticket numero : {num_ticket}\n")
    date_val=datetime.now()
    date_ac = '%s/%s/%s' % (date_val.day, date_val.month, date_val.year)
    print(f"Date : {date_ac}\n")
    print(f"Vous avez été servi par : {nom_utilisateur}\n")
    print(f"NB	Desc.		Pds/vol. unitaire	Pds/vol. total	Orig.	HT unitaire	TVA	Total")
    for i in range(len(liste3)):
        nb=liste2[i][1]
        nom=liste3[i][3]
        vol_uni=liste3[i][5]
        chiffres = re.findall(r'\d+', vol_uni)
        vol_tot=int(chiffres[0])*int(nb)
        origine=liste3[i][11]
        prix=liste3[i][7]
        tva=liste3[i][9]
        print(f"{nb}	{nom}		{vol_uni}		{vol_tot}		{origine}		{prix}€	10%	{calcul_tva(int(prix),int(nb),tva)}€")
    
    print(f"Total HT : {calcul_totaux()[1]}")
    print(f"Total TVA : {calcul_totaux()[0]}")
    print(f"Total : {calcul_totaux()[2]}")

if __name__ == "__main__":
    csv=recup_csv("bdd2.csv")
    recup_elem(csv,liste2)
    ticket()