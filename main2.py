"""
Ce programme généer une ticket de caisse en fonction des arguments passés en ligne de commande.

Exemple d'exécution en ligne de commande :
    python3 main.py "But Market" "Lisa" "C01:2|C02:1|C03:3"
"""

import sys
from datetime import datetime

liste_produits = {
    "C01": {"nom": "pack de coca", "poids": "2kg", "prix_ht": 5.0, "tva": 0.20, "origine": "Lituanie"},
    "C02": {"nom": "kilo de pdt", "poids": "1kg", "prix_ht": 1.0, "tva": 0.10, "origine": "Espagne"},
    "C03": {"nom": "pack Biscotte", "poids": "950g", "prix_ht": 2.0, "tva": 0.10, "origine": "France"},
    "C04": {"nom": "Café soluble", "poids": "250g", "prix_ht": 3.0, "tva": 0.10, "origine": "Roumanie"},
    "C05": {"nom": "Crakers", "poids": "125g", "prix_ht": 4.0, "tva": 0.20, "origine": "Angleterre"},
    "C06": {"nom": "Eau", "poids": "1,5L", "prix_ht": 6.0, "tva": 0.10, "origine": "Suisse"},
    "C07": {"nom": "Pain", "poids": "250g", "prix_ht": 1.0, "tva": 0.10, "origine": "France"},
}




#fonction pour actualiser le numéro de ticket dans un fichier txt:
def get_num_ticket():
    try:
        with open("numero_ticket.txt", "r") as f:
            numero_ticket = int(f.read())
    except FileNotFoundError:#si on ne trouve pas le fichier le numéro est 0
            numero_ticket = 0
    
    numero_ticket += 1

    with open("numero_ticket.txt", "w") as f:
        f.write(str(numero_ticket))

    ticket_final:str = f"Numéro de ticket :{numero_ticket}"
    return ticket_final

def generer_ticket(magasin: str, numero_ticket:str, vendeur: str, items: str) -> str:
    """
    Génère un ticket de caisse sous le format demandé en cours
    """
    lignes_ticket = []
    total_ht = 0
    total_tva = 0
    numero_ticket = get_num_ticket()


    # --- En-tête ---

    lignes_ticket.append(f"{magasin}")
    lignes_ticket.append(f"{numero_ticket}")
    lignes_ticket.append("")
    lignes_ticket.append(f"Date : {datetime.now().strftime('%d/%m/%Y')}")
    lignes_ticket.append("")
    lignes_ticket.append(f"Vous avez été servi par : {vendeur:<25}")
    lignes_ticket.append("-" * 40)
    lignes_ticket.append(f"{'NB':<3} {'Desc.':<15} {'Poids/vol. unit.':<12} {'Poids/vol. total':<20} {'HT unitaire':>5} {'TVA':>10} {'Total':>8}")
    lignes_ticket.append("-" * 40)

    # --- Produits ---
    for item in items.split("|"):
        try:
            code, quantite = item.split(":")
            quantite = int(quantite)
        except ValueError:
            print(f"!!!!!!!!!!IL Y A UNE ERREUR POUR L'ARTICLE CODE : {code}, IL FAUT METTRE UN ENTIER POUR LA QUANTITE!!!!!!!!!!!!!")
            sys.exit(1) # ignore entrée invalide

        produit = liste_produits.get(code)
        if produit:
            pu = produit["prix_ht"]
            taux_tva = produit["tva"]
            montant_ht = pu * quantite
            montant_tva = montant_ht * taux_tva
            montant_ttc = montant_ht + montant_tva

            total_ht += montant_ht
            total_tva += montant_tva
            # Poids total
            poids_unit = produit["poids"]
            poids_total = calculer_poids_total(poids_unit, quantite)

            lignes_ticket.append(f"{quantite:<3} {produit['nom']:<15} {poids_unit:<10} {poids_total:<14} {pu:>4.0f}€ {int(taux_tva*100):>2}% {montant_ttc:>7.1f}€")

    # --- Totaux ---
    total_ttc = total_ht + total_tva
    lignes_ticket.append("")
    lignes_ticket.append(f"{'Total HT':<20}{total_ht:.1f}€")
    lignes_ticket.append(f"{'Total TVA':<20}{total_tva:.1f}€")
    lignes_ticket.append(f"{'Total':<20}{total_ttc:.1f}€")

    return "\n".join(lignes_ticket)

def calculer_poids_total(poids_unit: str, quantite: int) -> str:
    """
    Calcule le poids/volume total.
    Ex: "1kg" x 3 = "3kg"
    """
    try:
        # Séparer valeur et unité (ex:"200g", "20kg", "1,5L")
        valeur = poids_unit[:-2].replace(",", ".")  # permet d'enlever l'unité
        unite = poids_unit[-2:]
        total = float(valeur) * quantite
        # permet de remettre au bon format
        if unite == "kg":
            return f"{int(total)}kg" if total.is_integer() else f"{total:.1f}kg"
        elif unite == "g":
            return f"{int(total)}g" if total.is_integer() else f"{total:.1f}g"
        elif unite == "L":
            return f"{total:.1f}L"
    except Exception:
        return poids_unit  # retourne le poids unitaire si non calculable

    return poids_unit


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python3 main.py <Magasin> <Vendeur> <Items ex: C01:2|C02:1>")
        sys.exit(1)

    magasin = sys.argv[1]
    numero_ticket = get_num_ticket
    vendeur = sys.argv[2]
    items = sys.argv[3]
    ticket = generer_ticket(magasin, numero_ticket, vendeur, items)
    print(ticket)
