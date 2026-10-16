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

# Code : (Description, Prix HT, Taux de TVA en %, Poids/volume unitaire, Unité)
# Unité : "g" pour un poids (en grammes), "ml" pour un volume (en millilitres)
ARTICLES:dict = {"C01": ("Pack de coca", 5.00, 20, 2000, "ml"),
            "C02": ("Kg patate", 1.00, 10, 1000, "g"),
            "C03": ("Pack biscotte", 2.00, 10, 950, "g"),
            "C04": ("Café soluble", 3.00, 10, 200, "g"),
            "C05": ("Crackers", 4.00, 10, 250, "g")
}
horodatage = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

# Convertit une quantité en g ou ml vers un affichage lisible (kg, L)
def formater_quantite(valeur:float, unite:str) -> str:
    if valeur >= 1000:
        unite_grande = "kg" if unite == "g" else "L"
        return f"{valeur / 1000:g}{unite_grande}"
    return f"{valeur:g}{unite}"

# Mise en forme du ticket : < aligne à gauche, > aligne à droite, le nombre est la largeur de la colonne
# Colonnes : NB, Desc., Poids/volume unitaire, Poids/volume total, HT unitaire, TVA, Total
FORMAT_LIGNE:str = "{:<4}{:<16}{:>23}{:>20}{:>13}{:>6}{:>10}\n"
FORMAT_TOTAL:str = " " * 70 + "{:<12}{:>10}\n"

sortie:str = ""
grand_total_ht:int = 0
grand_total_tva:float = 0

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
sortie += FORMAT_LIGNE.format("NB", "Desc.", "Poids/volume unitaire", "Poids/volume total", "HT unitaire", "TVA", "Total")

# Parsing des produits
produit_qte:str = produits.split("|")
for produit in produit_qte:
    infos_achat = produit.split(":")
    code_achete = infos_achat[0]
    qte_achetee = 0
    try:
        qte_achetee = int(infos_achat[1])
    except ValueError:
        sortie += f"{infos_achat[1]} ERREUR: il faut taper une quantité entière !\n"
    desc_produit = "NONE"
    prix_unitaire = 0
    taux_tva = 0
    poids_volume_unitaire = 0
    unite = "g"
    tot_produit = 0
    try:
        desc_produit = ARTICLES[code_achete][0]
        prix_unitaire = ARTICLES[code_achete][1]
        taux_tva = ARTICLES[code_achete][2]
        poids_volume_unitaire = ARTICLES[code_achete][3]
        unite = ARTICLES[code_achete][4]
        tot_produit = prix_unitaire * int(qte_achetee)
    except KeyError:
        sortie += f"ERREUR: Êtes-vous sûr que le code {code_achete} est référencé ?\n"
    except Exception as e:
        sortie += f"ERREUR {e}: Demandez à Claude.\n"

    tva_produit = tot_produit * taux_tva / 100
    grand_total_ht += tot_produit
    grand_total_tva += tva_produit
    poids_volume_total = poids_volume_unitaire * qte_achetee
    sortie += FORMAT_LIGNE.format(qte_achetee,
                                  desc_produit,
                                  formater_quantite(poids_volume_unitaire, unite),
                                  formater_quantite(poids_volume_total, unite),
                                  f"{prix_unitaire}€",
                                  f"{taux_tva}%",
                                  f"{tot_produit + tva_produit:.2f}€")

sortie += FORMAT_TOTAL.format("Total HT", f"{grand_total_ht:.2f}€")
sortie += FORMAT_TOTAL.format("Total TVA", f"{grand_total_tva:.2f}€")
sortie += FORMAT_TOTAL.format("Total TTC", f"{grand_total_ht + grand_total_tva:.2f}€")


print(sortie)