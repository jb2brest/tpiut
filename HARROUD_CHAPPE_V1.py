# Programme génération de tiquet de caisse
# Naël Harroud ; Nathan Chappé
# R&T 3A1
# 01/10/2025

import sys
import datetime
import re


# Initialisation de la base de données des produits et de l'expression regex.
liste_produit : list = [[["C01"],["C02"],["C03"],["C04"],["C05"]],[["pack de coca"],["kilo de pdt"],["pack Biscotte"],["Café soluble"],["Crackers"]],[[5],[1],[2],[3],[4]]]
patterne = re.compile(r"^C0\d:\d+$")


# Fonction verif_variable vient vérifier le bon respect des formats des variables.
def verif_variable(nomMagasin,nomServeur,produit) :
    retour = True
    try :
        nomMagasin = str(nomMagasin)
    except Exception:
        print("Format du nom du magasin non conforme")
        retour = False
    try :
        nomServeur = str(nomServeur)
    except Exception :
        print("Format du nom du serveur non conforme")
        retour = False
    try :
        produit = str(produit)
        produit = produit.split("|")
        for prod in produit :
            if bool(patterne.match(prod)) == False :
                raise Exception
    except Exception:
        print("Format des produits non conforme (Ex : C01:10)")
        retour = False
    return retour

# Fonction calclu_prixTVA : Calcul le total TTC à partir du total HT.
def calcul_prixTVA(prix) :
    return float(prix) * 1.10

# Fonction calcul_TotalTVA: Somme de la TVA de chaque produit. 
def calcul_TotalTVA(produit : str):
    total = 0
    produit = produit.split("|")
    for prod in produit :
        nb = int(prod.split(":")[1])
        identifiant : int = int(prod.split(":")[0].split("C0")[1]) - 1
        total = total + liste_produit[2][identifiant][0]*0.1*nb
    return total

# Fonction calcul_TotalHt: Total des prix HT 
def calcul_TotalHt(produit) :
    total = 0
    produit = produit.split("|")
    for prod in produit :
        nb = int(prod.split(":")[1])
        identifiant : int = int(prod.split(":")[0].split("C0")[1]) - 1
        total = total + liste_produit[2][identifiant][0]*nb
    return total


# Fonction generer_tab: Genère un tableau de 5 colonnes (Nb,Desc.,HT Unitaire,TVA,Total) de chaque produit
def generer_tab(produit : str) :
        produit = produit.split("|")
        print("NB\tDesc.\t        HT Unitaire\tTVA\tTotal")
        for prod in produit :
            nb = int(prod.split(":")[1])
            identifiant : int = int(prod.split(":")[0].split("C0")[1]) - 1
            desc = liste_produit[1][identifiant][0]
            prixHt = liste_produit[2][identifiant][0]
            Total = calcul_prixTVA(prixHt * nb)
            print(f"{nb}\t{desc}\t{prixHt}\t        10%\t{Total}")

# Fonction numTicket: La fonction lit le fichier numTiquet.txt afin de récuperer le nouveau numéro de Tiquet. 
def numTicket() :
    with open("numTiquet.txt", "r", encoding="utf-8" ) as f :
        num = f.read()
    return num

# Fonction incrTiquet: La fonction écrit dans le fichier numTiquet.txt le prochain numéro de Tiquet.
def incrTiquet(num : int) :
    with open("numTiquet.txt", "w", encoding="utf-8" ) as f :
        f.write(f"{int(num)+1}")



# Fonction génerer_tiquet: Génère le tiquet de caisse final.
def générer_tiquet(nomMagasin : str , nomServeur : str, produit : list) :
    print(str(nomMagasin))
    num = numTicket()
    print(f"Ticket numéro : {num}\n")
    incrTiquet(num)
    print(f"Date : {datetime.date.today()} \n")
    print(f"Vous avez été servi par : {str(nomServeur)} \n")
    generer_tab(produit)
    totalHT = calcul_TotalHt(produit)
    totalTVA = calcul_TotalTVA(produit)
    prixTotal = calcul_prixTVA(totalHT)
    print("\n")
    print(f"\t\t       Total HT   {totalHT}")
    print(f"\t\t       Total TVA  {totalTVA}")
    print(f"\t\t       Total      {prixTotal}")


# Vérification du nombre de variable passé en paramètre si OUI -> génère un tiquet.
if len(sys.argv) > 3 :
    nomMagasin : str = sys.argv[1]
    nomServeur : str = sys.argv[2]
    produits : str = sys.argv[3]
    if verif_variable(nomMagasin,nomServeur,produits) :
            générer_tiquet(nomMagasin,nomServeur,produits)
else :
        print("Aucun ou pas assez de paramètre(s). Fin du programme")