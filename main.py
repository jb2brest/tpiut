#########################################################################################################
#
#          CREATION DE TICKET DE CAISSE 
#
#   EXECUTION DU CODE "Python3 'nom_du_fichier.py' '<nom_magasin>' '<nom_serveur>' '<articles>'"
# 
#
#   PARAMETRE : <nom_magasin> <nom_serveur> <articles>
#   Les 3 paramètres sont obligatoire
#
#   Pour ajouter un article : 'code_du_produit':'quantite'
#   ex : "C01:6"
#
#   Pour ajouter plusieurs articles : '|'  
#   ex : "C01:10|C02:2"   "C01:10|C02:2|C03:1"
#
#   
########################################################################################################


import sys
from datetime import datetime

# Vérification des arguments
if len(sys.argv) != 4:
    print("Usage: python3 main.py <nom_magasin> <nom_serveur> <articles>")
    print('Exemple: python3 main.py "BUT Market" "Lisa" "C01:10|C02:2"')
    sys.exit(1)

magasin = sys.argv[1]
serveur = sys.argv[2]
articles_input = sys.argv[3]

# Liste des articles disponibles
articles = {
    "C01": {"desc": "pack de coca", "prix": 5},
    "C02": {"desc": "kilo de pdt", "prix": 1},
    "C03": {"desc": "pack Biscotte", "prix": 2},
    "C04": {"desc": "Café soluble", "prix": 3},
    "C05": {"desc": "Crakers", "prix": 4}
}

# Pourcentage de la TVA 
TVA = 10

def lire_compteur():
    try:
        with open("compteur.txt", "r") as f:
            return int(f.read())
    except FileNotFoundError:
        return 0

def incrementer_compteur():
    compteur = lire_compteur() + 1
    with open("compteur.txt", "w") as f:
        f.write(str(compteur))
    return compteur

# Informations du ticket
ticket_num = lire_compteur() + 1
incrementer_compteur()

# Traitement des articles passés en argument
ticket_items = []
for article_str in articles_input.split("|"):
    try:
        code, quantite = article_str.split(":")
        code = code.upper()
        quantite  = int(quantite)
# Test des informations fournit
        if code not in articles:
            print(f"Code invalide : {code}, ignoré.")
            continue
        if quantite == 0  or quantite < 0 : 
            print(f"quantité invalide : {code}|{quantite}, ignoré.")
            continue
        item_total = articles[code]['prix'] * quantite * (1 + TVA / 100)
        ticket_items.append({
            "desc": articles[code]["desc"],
            "prix": articles[code]["prix"],
            "quantite": quantite,
            "total": item_total
        })
    except ValueError:
        print(f"Format invalide pour l'article : {article_str}, ignoré.")
        continue

# Calcul des totaux
total_ht = sum(item["prix"] * item["quantite"] for item in ticket_items)
total_tva = total_ht * TVA / 100
total_ttc = total_ht + total_tva

# Génération du contenu du ticket
ticket_lines = []
ticket_lines.append("\n" + "-"*40)
ticket_lines.append(f"{magasin}")
ticket_lines.append(f"Ticket numéro : {ticket_num}")
ticket_lines.append(f"\nDate : {datetime.now().strftime('%d/%m/%Y')}")
ticket_lines.append(f"\nVous avez été servi par : {serveur}")
ticket_lines.append("\nNB  Desc.                 HT unitaire  TVA  Total")
for i, item in enumerate(ticket_items, start=1):
    ticket_lines.append(f"{item['quantite']} {item['desc']:<20} {item['prix']}€        {TVA}%   {item['total']:.2f}€")
ticket_lines.append("\n" + " "*30 + f"Total HT   {total_ht}€")
ticket_lines.append(" "*30 + f"Total TVA  {total_tva}€")
ticket_lines.append(" "*30 + f"Total      {total_ttc:.2f}€")
ticket_lines.append("-"*40)

# Écriture dans un fichier
with open("ticket.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(ticket_lines))


