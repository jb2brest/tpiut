"""
Ce programme généer une ticket de caisse en fonction des arguments passés en ligne de commande.

Exemple d'exécution en ligne de commande :
    python3 main.py "But Market" "Lisa" "C01:2|C02:1|C03:3"
"""

import sys
from datetime import datetime

PRODUITS = {
    "C01": {"nom": "Coca Cola", "prix_ht": 5.00},
    "C02": {"nom": "kilo de pdt", "prix_ht": 1.00},
    "C03": {"nom": "pack Biscotte", "prix_ht": 2.00},
    "C04": {"nom": "Café soluble", "prix_ht": 3.00},
    "C05": {"nom": "Crackers", "prix_ht": 4.00},    
}

TAUX_TVA = 0.10  # TVA de 10%


def generer_ticket(magasin: str, vendeur: str, items: str) -> str:
    """
    Génère un ticket de caisse sous le format demandé en cours
    """
    lignes_ticket = []
    total_ht = 0

    # --- En-tête ---

    lignes_ticket.append(f"{magasin:^40}")
    lignes_ticket.append(f"Vendeur : {vendeur:<25} {datetime.now().strftime('%d/%m/%Y %H:%M')}")
    lignes_ticket.append("-" * 40)
    lignes_ticket.append(f"{'Article':<20}{'Qté':>5}{'PU HT':>7}{'Total HT':>8}")
    lignes_ticket.append("-" * 40)

    # --- Produits ---
    for item in items.split("|"):
        try:
            code, quantite = item.split(":")
            quantite = int(quantite)
        except ValueError:
            continue  # ignore entrée invalide

        produit = PRODUITS.get(code)
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
    vendeur = sys.argv[2]
    items = sys.argv[3]

    ticket = generer_ticket(magasin, vendeur, items)
    print(ticket)
