"""
Ce programme généer une ticket de caisse en fonction des arguments passés en ligne de commande.

Exemple d'exécution en ligne de commande :
    python3 main.py "But Market" "Lisa" "C01:2|C02:1|C03:3"
"""

import sys
from datetime import datetime

liste_produits = {
    "C01": {"nom": "Coca Cola", "prix_ht": 5.00},
    "C02": {"nom": "kilo de pdt", "prix_ht": 1.00},
    "C03": {"nom": "pack Biscotte", "prix_ht": 2.00},
    "C04": {"nom": "Café soluble", "prix_ht": 3.00},
    "C05": {"nom": "Crackers", "prix_ht": 4.00},    
}


TAUX_TVA = 0.10  # TVA de 10%


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
    numero_ticket = get_num_ticket()


    # --- En-tête ---

    lignes_ticket.append(f"{magasin}")
    lignes_ticket.append(f"{numero_ticket}")
    lignes_ticket.append("")
    lignes_ticket.append(f"Date : {datetime.now().strftime('%d/%m/%Y')}")
    lignes_ticket.append("")
    lignes_ticket.append(f"Vous avez été servi par : {vendeur:<25}")
    lignes_ticket.append("-" * 40)
    lignes_ticket.append(f"{'Article':<20}{'Qté':>5}{'PU HT':>7}{'Total HT':>8}")
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
            prix_total = pu * quantite
            total_ht += prix_total
            lignes_ticket.append(
                f"{produit['nom']:<20}{quantite:>5}{pu:>7.2f}{prix_total:>8.2f}"
            )

    # --- Totaux ---
    tva = total_ht * TAUX_TVA
    total_ttc = total_ht + tva

    lignes_ticket.append("-" * 40)
    lignes_ticket.append(f"{'Total HT':<30}{total_ht:>9.2f} €")
    lignes_ticket.append(f"TVA ({int(TAUX_TVA*100)}%)".ljust(30) + f"{tva:>9.2f} €")
    lignes_ticket.append(f"{'Total TTC':<30}{total_ttc:>9.2f} €")

    return "\n".join(lignes_ticket)


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
