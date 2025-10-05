import os
import sys
from datetime import datetime

PRODUITS = {
    "C01": {"description": "pack de coca", "poids": "2kg",   "prix_ht": 5, "tva": 0.20},
    "C02": {"description": "kilo de pdt",  "poids": "1kg",   "prix_ht": 1, "tva": 0.10},
    "C03": {"description": "pack Biscotte","poids": "950g",  "prix_ht": 2, "tva": 0.10},
    "C04": {"description": "Café soluble", "poids": "250g",  "prix_ht": 3, "tva": 0.10},
    "C05": {"description": "Crakers",      "poids": "125g",  "prix_ht": 4, "tva": 0.20},
    "C06": {"description": "Eau",          "poids": "1.5L",  "prix_ht": 6, "tva": 0.10},
    "C07": {"description": "Pain",         "poids": "250g",  "prix_ht": 1, "tva": 0.10}
}
FICHIER_NUMERO = "numero_ticket.txt"

def afficher_produits():
    print("\nListe des produits disponibles :")
    print(f"{'Code':<5}{'Description':<15}{'Poids/Vol.':<10}{'Prix HT':<8}{'TVA':<6}")
    for code, info in PRODUITS.items():
        tva_txt = f"{int(info['tva']*100)} %"
        print(f"{code:<5}{info['description']:<15}{info['poids']:<10}{info['prix_ht']:<8}{tva_txt:<6}")
    print()

def afficher_erreur_utilisation(message=""):
    print("Erreur :", message)
    print('Utilisation : python3 main.py "Nom Magasin" "Vendeur" "C01:QTE|C02:QTE|..."')
    print('Exemple : python3 main.py "Leclerc" "José" "C01:4|C05:1"')
    afficher_produits()
    sys.exit(1)

def lire_numero_ticket():
    if os.path.exists(FICHIER_NUMERO):
        with open(FICHIER_NUMERO, "r", encoding="utf-8") as f:
            numero = f.read().strip()
            if numero.isdigit():
                nouveau_numero = int(numero) + 1
            else:
                nouveau_numero = 2200
    else:
        nouveau_numero = 2200
    with open(FICHIER_NUMERO, "w", encoding="utf-8") as f:
        f.write(str(nouveau_numero))
    return nouveau_numero

def est_nom_valide(nom):
    return nom.replace(" ", "").isalpha()

def calcul_poids_total(qte, poids_unitaire):
    """Retourne la chaîne exprimant le poids/volume total (par concaténation naïve)."""
    # Extraction valeur et unité (ex: 2kg, 950g, 1.5L)
    import re
    m = re.match(r"([\d\.]+)([a-zA-Z]+)", poids_unitaire)
    if not m:
        return "N/A"
    valeur, unite = m.groups()
    try:
        total = float(valeur) * qte
        # Si l'unité est g ou ml et dépasse 1000, convertir en kg ou L
        if unite == "g" and total >= 1000:
            total_aff = f"{total/1000:.2f}kg"
        elif unite == "ml" and total >= 1000:
            total_aff = f"{total/1000:.2f}L"
        else:
            total_aff = f"{total:g}{unite}"
        # Pour kg/L garder une décimale précise
        if unite in ("kg", "L"):
            total_aff = f"{total:.2f}{unite}"
        return total_aff
    except Exception:
        return "N/A"

def parse_commandes(chaine_commandes):
    liste_commandes = []
    if chaine_commandes.strip() == "":
        afficher_erreur_utilisation("Aucun article n'a été renseigné.")
    for couple in chaine_commandes.split('|'):
        if not couple:
            continue
        if ':' not in couple:
            afficher_erreur_utilisation(
                f"L'article '{couple}' n'est pas au format code:quantité."
            )
        code, quantite = couple.split(':', 1)
        if code not in PRODUITS:
            afficher_erreur_utilisation(f"Le code article '{code}' n'existe pas.")
        if not quantite.isdigit():
            afficher_erreur_utilisation(
                f"La quantité '{quantite}' pour l'article '{code}' n'est pas un nombre entier positif."
            )
        quantite_int = int(quantite)
        if quantite_int <= 0:
            afficher_erreur_utilisation(
                f"La quantité '{quantite}' pour l'article '{code}' doit être supérieure à 0."
            )
        prod = PRODUITS[code]
        poids_total = calcul_poids_total(quantite_int, prod["poids"])
        liste_commandes.append({
            "code": code,
            "description": prod["description"],
            "poids_unitaire": prod["poids"],
            "poids_total": poids_total,
            "prix_ht": prod["prix_ht"],
            "tva": prod["tva"],
            "quantite": quantite_int
        })
    return liste_commandes

def calculer_totaux(commandes):
    total_ht = sum(a["prix_ht"] * a["quantite"] for a in commandes)
    total_tva = sum(a["prix_ht"] * a["quantite"] * a["tva"] for a in commandes)
    total = total_ht + total_tva
    return int(total_ht), round(total_tva, 2), round(total, 2)

def generer_ticket_affichage(ticket):
    lignes = []
    lignes.append(f"{ticket['magasin']}")
    lignes.append(f"Ticket numéro : {ticket['numero_ticket']}")
    lignes.append("")
    lignes.append(f"Date : {ticket['date']}")
    lignes.append("")
    lignes.append(f"Vous avez été servi par : {ticket['vendeur']}")
    lignes.append("")
    lignes.append(f"{'NB':<3} {'Desc.':<15} {'Poids/U':<9}{'Poids total':<12}{'HT unit.':<9}{'TVA':<6}{'Total TTC'}")
    for a in ticket['articles']:
        montant_ht = a["prix_ht"] * a["quantite"]
        montant_tva = montant_ht * a["tva"]
        montant_total = montant_ht + montant_tva
        lignes.append(f"{a['quantite']:<3} {a['description']:<15} {a['poids_unitaire']:<9}{a['poids_total']:<12}{a['prix_ht']}€{'':<2}      {int(a['tva']*100)}%  {montant_total:.2f}€")
    lignes.append("")
    lignes.append(f"{'Total HT':<34}{ticket['total_ht']}€")
    lignes.append(f"{'Total TVA':<34}{ticket['total_tva']:.2f}€")
    lignes.append(f"{'Total':<34}{ticket['total']:.2f}€")
    return '\n'.join(lignes)

def creer_ticket_par_arguments():
    if len(sys.argv) != 4:
        afficher_erreur_utilisation("Le nombre d'arguments n'est pas correct.")
    nom_magasin = sys.argv[1]
    vendeur = sys.argv[2]
    chaine_commandes = sys.argv[3]
    if not est_nom_valide(nom_magasin):
        afficher_erreur_utilisation("Le nom du magasin doit uniquement contenir des lettres (pas de chiffre ou caractère spécial).")
    if not est_nom_valide(vendeur):
        afficher_erreur_utilisation("Le nom du vendeur doit uniquement contenir des lettres (pas de chiffre ou caractère spécial).")
    articles = parse_commandes(chaine_commandes)
    numero_ticket = lire_numero_ticket()
    date_du_jour = datetime.now().strftime("%d/%m/%Y")
    total_ht, total_tva, total = calculer_totaux(articles)
    ticket = {
        "magasin": nom_magasin,
        "numero_ticket": numero_ticket,
        "date": date_du_jour,
        "vendeur": vendeur,
        "articles": articles,
        "total_ht": total_ht,
        "total_tva": total_tva,
        "total": total
    }
    print("\n" + generer_ticket_affichage(ticket) + "\n")

if __name__ == "__main__":
    if len(sys.argv) == 4:
        creer_ticket_par_arguments()
    else:
        print('Utilisation : python3 main.py "Nom Magasin" "Vendeur" "C01:QTE|C02:QTE|..."')
        print('Exemple : python3 main.py "Leclerc" "José" "C01:4|C05:1"')
        afficher_produits()