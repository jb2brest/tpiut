#!/usr/bin/python3

# TICKETO - Logiciel d'édition de tickets de caisse
# Antoine GUERY & Thomas LE FLOC'H

from sys import argv
from datetime import datetime

# python3 main.py "Pipi market" "Thomas" "C01:2|C03:6"

compteur_num_ticket = 0
with open("compteur.txt", mode="r", encoding="utf-8") as f:
    compteur_num_ticket = int(f.read().strip())
    
compteur_num_ticket += 1

with open("compteur.txt", mode="w", encoding="utf-8") as f:
    f.write(str(compteur_num_ticket))

ARTICLES:dict = {"C01": ("Pack de coca", 5.00),
            "C02": ("Kg patate", 1.00),
            "C03": ("Pack biscotte", 2.00),
            "C04": ("Café soluble", 3.00),
            "C05": ("Crackers", 4.00)
}
horodatage = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

sortie:str = ""
grand_total_ht:int = 0

# Récupération arguments
args:list = argv[1:]
magasin:str = args[0]
caissier:str = args[1]
produits:str = args[2]

sortie += f"{magasin}\n"
sortie += f"Ticket numéro {compteur_num_ticket}\n\n"
sortie += f"Date et heure : {horodatage}\n\n"
sortie += f"Vous avez été servi par {caissier}\n"
sortie += f"ARTICLES\n"
sortie += f"Qté    Desc.            HT Unitaire    TVA    Total\n"

# Parsing des produits
produit_qte:str = produits.split("|")
for produit in produit_qte:
    infos_achat = produit.split(":")
    code_achete = infos_achat[0]
    qte_achetee = int(infos_achat[1])
    desc_produit = "NONE"
    prix_unitaire = 0
    tot_produit = 0
    try:
        desc_produit = ARTICLES[code_achete][0]
        prix_unitaire = ARTICLES[code_achete][1]
        tot_produit = prix_unitaire * int(qte_achetee)
    except KeyError:
        print(f"ERREUR: Êtes-vous sûr que le code {code_achete} est référencé ?")
    except Exception as e:
        print(f"ERREUR {e}: Demandez à Claude.")

    grand_total_ht += tot_produit
    sortie += f"{qte_achetee}      {desc_produit}     {prix_unitaire}€           10%    {tot_produit*qte_achetee*1.1}€\n"

sortie += f"                                              Total HT {grand_total_ht:.2f}€\n"
sortie += f"                                              TVA 10%\n"
sortie += f"                                              Total TTC {grand_total_ht * 1.1:.2f}€\n"


print(sortie)
