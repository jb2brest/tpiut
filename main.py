import sys
from datetime import datetime

# Dictionnaire des articles disponibles
ARTICLES = {
    "CO1": {"desc": "pack de coca", "prix": 5, "tva": 0.1},
    "CO2": {"desc": "kilo de pdt", "prix": 1, "tva": 0.1},
    "CO3": {"desc": "pack Biscotte", "prix": 2, "tva": 0.1},
    "CO4": {"desc": "Café soluble", "prix": 3, "tva": 0.1},
    "CO5": {"desc": "Crakers", "prix": 4, "tva": 0.1},
}

def generer_ticket(magasin, caissier, commande_str):
    numero_ticket = 2200
    date_ticket = datetime.now().strftime("%d/%m/%Y")

    lignes_commande = []
    total_ht = 0
    total_tva = 0

    # Découper la commande en paires code:quantité
    items = commande_str.split("|")
    for i in items:
        try:
            code, quantite_str = i.split(":")
        except ValueError:
            print(f"⚠️ Format invalide pour l'article : {i}. Utilisez <code>:<quantité>.")
            continue

        # Vérifier que la quantité est bien un entier
        try:
            quantite = int(quantite_str)
            if quantite <= 0:
                print(f"Quantité non valide ({quantite}) pour {code}. Elle doit être > 0.")
                continue
        except ValueError:
            print(f"Quantité '{quantite_str}' invalide pour {code}. Saisissez un nombre entier.")
            continue
        if code not in ARTICLES:
            print(f"Article {code} inconnu, ignoré.")
            continue

        article = ARTICLES[code]
        prix_ht = article["prix"] * quantite
        montant_tva = prix_ht * article["tva"]
        prix_ttc = prix_ht + montant_tva

        total_ht += prix_ht
        total_tva += montant_tva

        lignes_commande.append(
            f"{quantite}\t{article['desc']:<15}\t{article['prix']}€\t"
            f"{int(article['tva']*100)}%\t{prix_ttc:.2f}€"
        )

    # Construction du ticket
    ticket = [
        f"\n\t{magasin}",
        f"Ticket numéro : {numero_ticket}",
        f"\nDate : {date_ticket}",
        f"\nVous avez été servi par : {caissier}\n",
        "NB\tDesc.\t\tHT unitaire\tTVA\tTotal",
        "\n".join(lignes_commande),
        "\n",
        f"\t\t\t\tTotal HT\t{total_ht:.2f}€",
        f"\t\t\t\tTotal TVA\t{total_tva:.2f}€",
        f"\t\t\t\tTotal   \t{total_ht + total_tva:.2f}€",
    ]

    return "\n".join(ticket)


ticket = generer_ticket("BUT Market", "Lisa", "CO1:a|CO2:2")
print(ticket)

