#!/usr/bin/env python3

import sys
from datetime import datetime

# Catalogue des produits
PRODUITS = {
    "C01": {"nom": "Coca Cola", "prix_ht": 5.00},
    "C02": {"nom": "kilo de pdt", "prix_ht": 1.00},
    "C03": {"nom": "pack Biscotte", "prix_ht": 2.00},
    "C04": {"nom": "Café soluble", "prix_ht": 3.00},
    "C05": {"nom": "Crackers", "prix_ht": 4.00},    
}

TAUX_TVA = 0.10 

def generer_ticket(magasin: str, vendeur: str, items: str) -> str:
    lignes_ticket = []
    total_ht = 0

    #En-tête
    lignes_ticket.append("=" * 40)
    lignes_ticket.append(f"{magasin:^40}")
    
    # récupère la date et l'heure du ticket
    date_heure = datetime.now().strftime('%d/%m/%Y %H:%M')
    #aligne le vendeur à gauche et on met la date au bout
    lignes_ticket.append(f"Vendeur : {vendeur:<25} {date_heure}")
    
    lignes_ticket.append("-" * 40)
    # Noms des colonnes 
    lignes_ticket.append(f"{'Article':<20}{'Qté':>5}{'PU HT':>7}{'Total HT':>8}")
    lignes_ticket.append("-" * 40)

    # Boucle sur les articles achetés
    # découpage articles envoyés dans le terminal (ex: "C01:10|C02:13")
    for item in items.split("|"):
        try:
            code, quantite = item.split(":")
            quantite = int(quantite)
        except ValueError:
            # Si y'a une erreur de frappe, on passe au suivant sans crasher
            continue 

        produit = PRODUITS.get(code)
        if produit:
            pu = produit["prix_ht"]
            prix_total = pu * quantite
            total_ht += prix_total # cumule le prix 
            
            # On ajoute la ligne du produit avec les alignements
            # Le '.2f' sert à toujours afficher 2 chiffres après la virgule (ex: 5.00)
            lignes_ticket.append(f"{produit['nom']:<20}{quantite:>5}{pu:>7.2f}{prix_total:>8.2f}")

    #Calcul des totaux 
    tva = total_ht * TAUX_TVA
    total_ttc = total_ht + tva

    # Bas du ticket 
    lignes_ticket.append("-" * 40)
    lignes_ticket.append(f"{'Total HT':<30}{total_ht:>8.2f} €")
    lignes_ticket.append(f"{'TVA (10%)':<30}{tva:>8.2f} €")
    lignes_ticket.append(f"{'Total TTC':<30}{total_ttc:>8.2f} €")
    
    lignes_ticket.append("=" * 40)
    lignes_ticket.append("Merci de votre visite et à bientôt !".center(40))
    lignes_ticket.append("=" * 40)

    # colle toutes les lignes ensemble avec des sauts de ligne (\n)
    return "\n".join(lignes_ticket)

if __name__ == "__main__":
    #vérification, si l'utilisateur oublie des infos
    if len(sys.argv) < 4:
        print('Utilisation : python3 main.py "Nom Magasin" "Nom Vendeur" "C01:10|C02:13"')
        sys.exit(1)

    magasin = sys.argv[1]
    vendeur = sys.argv[2]
    items = sys.argv[3]

    # On appelle notre fonction et on affiche le résultat dans la console
    ticket = generer_ticket(magasin, vendeur, items)
    print(ticket)