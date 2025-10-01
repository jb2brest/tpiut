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

# Articles disponibles avec poids, TVA et origine
articles = {
    "C01": {"desc": "pack de coca", "poids": "2kg", "prix": 5, "tva": 20, "origine": "Lituanie"},
    "C02": {"desc": "kilo de pdt", "poids": "1kg", "prix": 1, "tva": 10, "origine": "Espagne"},
    "C03": {"desc": "pack Biscotte", "poids": "950g", "prix": 2, "tva": 10, "origine": "France"},
    "C04": {"desc": "Café soluble", "poids": "250g", "prix": 3, "tva": 10, "origine": "Roumanie"},
    "C05": {"desc": "Crakers", "poids": "125g", "prix": 4, "tva": 20, "origine": "Angleterre"},
    "C06": {"desc": "Eau", "poids": "1.5L", "prix": 6, "tva": 10, "origine": "Suisse"},
    "C07": {"desc": "Pain", "poids": "250g", "prix": 1, "tva": 10, "origine": "France"}
}

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

ticket_num = lire_compteur() + 1
incrementer_compteur()

ticket_items = []
for article_str in articles_input.split("|"):
    try:
        code, quantite = article_str.split(":")
        code = code.upper()
        quantite = int(quantite)

        if code not in articles:
            print(f"Code invalide : {code}, ignoré.")
            continue
        if quantite <= 0:
            print(f"Quantité invalide : {code}|{quantite}, ignoré.")
            continue

        produit = articles[code]
        prix_ht = produit["prix"]
        tva = produit["tva"]

        total_ht_item = prix_ht * quantite
        total_tva_item = total_ht_item * tva / 100
        total_ttc_item = total_ht_item + total_tva_item
        pt = quantite * float(produit["poids"][:-2])  
        ticket_items.append({
            "desc": produit["desc"],
            "poids_unitaire": produit["poids"],
            "poids_total": pt,
            "prix": prix_ht,
            "quantite": quantite,
            "tva": tva,
            "total_ht": total_ht_item,
            "total": total_ttc_item
        })
    except ValueError:
        print(f"Format invalide pour l'article : {article_str}, ignoré.")
        continue

# Totaux
total_ht = sum(item["total_ht"] for item in ticket_items)
total_tva = sum(item["total"] - item["total_ht"] for item in ticket_items)
total_ttc = total_ht + total_tva

# Génération du ticket
ticket_lines = []
ticket_lines.append("\n" + "-"*80)
ticket_lines.append(f"\n{magasin}")
ticket_lines.append(f"Ticket numéro : {ticket_num}")
ticket_lines.append(f"\nDate : {datetime.now().strftime('%d/%m/%Y')}")
ticket_lines.append(f"\nVous avez été servi par : {serveur}")
ticket_lines.append("\nNB  Desc.              Poids unitaire  Poids total  HT unitaire  TVA   Total")

for item in ticket_items:
    ticket_lines.append(f"{item['quantite']}   {item['desc']:<15}    {item['poids_unitaire']:<10}           {item['poids_total']:<10}      {item['prix']}€  {item['tva']}%   {item['total']:.1f}€")

ticket_lines.append("\n" + " "*60 + f"Total HT   {total_ht}€")
ticket_lines.append(" "*60 + f"Total TVA  {total_tva:.1f}€")
ticket_lines.append(" "*60 + f"Total      {total_ttc:.1f}€")
ticket_lines.append("\n" + "-"*80)


# Sauvegarde fichier
with open("ticket2.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(ticket_lines))
