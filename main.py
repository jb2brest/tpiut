import sys
from datetime import datetime

# Catalogue officiel du projet (Code: Nom, Prix HT, TVA en %)
CATALOGUE = {
    "C01": {"nom": "pack de coca", "prix_ht": 5.0, "tva": 10},
    "C02": {"nom": "kilo de pdt", "prix_ht": 1.0, "tva": 10},
    "C03": {"nom": "pack Biscotte", "prix_ht": 2.0, "tva": 10},
    "C04": {"nom": "Café soluble", "prix_ht": 3.0, "tva": 10},
    "C05": {"nom": "Crakers", "prix_ht": 4.0, "tva": 10},
}

def main():
    # Vérification des arguments (magasin, caissier, commande)
    if len(sys.argv) < 4:
        print("Erreur : arguments manquants.")
        print('Utilisation : python main.py "Magasin" "Caissier" "C01:1|C02:3"')
        sys.exit(1)

    magasin = sys.argv[1]
    caissier = sys.argv[2]
    commande = sys.argv[3]

    # Récupération de la date actuelle au format JJ/MM/AAAA
    date_du_jour = datetime.now().strftime("%d/%m/%Y")

    # En-tête du ticket
    print(f"{magasin}")
    print("Ticket numéro : 2200")
    print(f"Date : {date_du_jour}\n")
    print(f"Vous avez été servi par : {caissier}\n")

    # En-tête du tableau des articles
    print(f"{'NB':<4} {'Desc.':<15} {'HT unitaire':<12} {'TVA':<6} {'Total':<6}")

    total_ht_global = 0.0
    total_tva_global = 0.0

    # Découpage de la commande (ex: "C01:1|C02:3")
    items = commande.split("|")
    for item in items:
        if ":" in item:
            code, qte_str = item.split(":")
            qte = int(qte_str)

            if code in CATALOGUE:
                article = CATALOGUE[code]
                nom = article["nom"]
                prix_ht = article["prix_ht"]
                taux_tva = article["tva"]

                # Calculs par ligne
                ligne_ht = prix_ht * qte
                ligne_tva = ligne_ht * (taux_tva / 100)
                ligne_ttc = ligne_ht + ligne_tva

                # Cumul global
                total_ht_global += ligne_ht
                total_tva_global += ligne_tva

                # Affichage de la ligne du ticket
                print(f"{qte:<4} {nom:<15} {int(prix_ht)}€{'':<10} {taux_tva}%{'':<3} {int(ligne_ttc)}€")

    # Totaux finaux
    total_ttc_global = total_ht_global + total_tva_global

    print("\n" + " " * 20 + f"Total HT        {int(total_ht_global)}€")
    print(" " * 20 + f"Total TVA       {total_tva_global}€")
    print(" " * 20 + f"Total           {int(total_ttc_global)}€")

if __name__ == "__main__":
    main()