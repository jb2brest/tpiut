import sys
from datetime import datetime
import re

# Articles avec TVA fixe à 20 %
ARTICLES = {
    "C01": {"desc": "pack de coca", "poids": "2kg", "prix": 5, "tva": 0.20},
    "C02": {"desc": "kilo de pdt", "poids": "1kg", "prix": 1, "tva": 0.20},
    "C03": {"desc": "pack Biscotte", "poids": "950g", "prix": 2, "tva": 0.20},
    "C04": {"desc": "Café soluble", "poids": "250g", "prix": 3, "tva": 0.20},
    "C05": {"desc": "Crakers", "poids": "12g", "prix": 4, "tva": 0.20},
    "C06": {"desc": "Eau", "poids": "1.5L", "prix": 6, "tva": 0.20},
    "C07": {"desc": "Pain", "poids": "250g", "prix": 1, "tva": 0.20},
}

def convertir_poids(poids_str):

    match = re.match(r"^\s*([\d.,]+)\s*([a-zA-Z]+)\s*$", poids_str.strip())
    if not match:
        return None, None  # poids invalide

    try:
        valeur = float(match.group(1).replace(",", "."))
    except ValueError:
        return None, None  # nombre invalide

    unite = match.group(2).lower()

    if unite == "kg":
        return valeur * 1000, "g"
    elif unite == "g":
        return valeur, "g"
    elif unite == "l":
        return valeur, "L"
    else:
        return valeur, unite

def formater_poids(valeur, unite):

    if unite == "g":
        if valeur >= 1000:
            return f"{valeur/1000:.2f}kg"
        else:
            return f"{valeur:.0f}g"
    elif unite == "L":
        return f"{valeur:.2f}L"
    return f"{valeur}{unite}"

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
            print(f" Format invalide pour l'article : {i}. Utilisez <code>:<quantité>.")
            continue

        # Vérifier que la quantité est bien un entier > 0
        try:
            quantite = int(quantite_str)
            if quantite <= 0:
                print(f" Quantité non valide ({quantite}) pour {code}. Elle doit être > 0.")
                continue
        except ValueError:
            print(f" Quantité '{quantite_str}' invalide pour {code}. Saisissez un nombre entier.")
            continue

        # Vérifier que le code existe
        if code not in ARTICLES:
            print(f"Article {code} inconnu, ignoré.")
            continue

        article = ARTICLES[code]

        # Conversion du poids avec vérification
        poids_valeur, unite = convertir_poids(article["poids"])
        if poids_valeur is None:
            print(f" Poids invalide pour l'article {code} ({article['poids']}). Vérifiez la base ARTICLES.")
            continue

        prix_ht = article["prix"] * quantite
        montant_tva = prix_ht * article["tva"]
        prix_ttc = prix_ht + montant_tva

        total_ht += prix_ht
        total_tva += montant_tva

        poids_total_valeur = poids_valeur * quantite
        poids_unitaire_fmt = formater_poids(poids_valeur, unite)
        poids_total_fmt = formater_poids(poids_total_valeur, unite)

        lignes_commande.append(
            f"{quantite}\t{article['desc']:<15}\t{poids_unitaire_fmt:<6}\t{poids_total_fmt:<8}\t"
            f"{article['prix']}€\t{int(article['tva']*100)}%\t{prix_ttc:.2f}€"
        )

    # Si aucune ligne valide n'a été ajoutée
    if not lignes_commande:
        return f"\n\t{magasin}\nTicket numéro : {numero_ticket}\n\nDate : {date_ticket}\n\n Aucun article valide dans la commande."

    # Construction du ticket
    ticket = [
        f"\n\t{magasin}",
        f"Ticket numéro : {numero_ticket}",
        f"\nDate : {date_ticket}",
        f"\nVous avez été servi par : {caissier}\n",
        "NB\tDescription\t\tPoids U.\tPoids total\tHT unitaire\tTVA\tTotal TTC",
        "\n".join(lignes_commande),
        "\n",
        f"\t\t\t\t\t\tTotal HT\t{total_ht:.2f}€",
        f"\t\t\t\t\t\tTotal TVA\t{total_tva:.2f}€",
        f"\t\t\t\t\t\tTotal   \t{total_ht + total_tva:.2f}€",
    ]

    return "\n".join(ticket)
ticket = generer_ticket("BUT Market", "Lisa", "C01:10|C02:abc|C03:2|C99:3|C04:0|C05:-2")
print(ticket)
# Exemple
if __name__ == "__main__":
    ticket = generer_ticket("BUT Market", "Lisa", "C01:10|C02:abc|C03:2|C99:3|C04:0|C05:-2")
    print(ticket)

    if len(sys.argv) == 4:
        magasin = sys.argv[1]
        caissier = sys.argv[2]
        commande_str = sys.argv[3]
        ticket = generer_ticket(magasin, caissier, commande_str)
        print(ticket)
