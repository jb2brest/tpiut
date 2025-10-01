import os
import sys
from datetime import datetime

PRODUITS = {
    "C01": {"description": "pack de coca", "prix_ht": 5},
    "C02": {"description": "kilo de pdt", "prix_ht": 1},
    "C03": {"description": "pack Biscotte", "prix_ht": 2},
    "C04": {"description": "Café soluble", "prix_ht": 3},
    "C05": {"description": "Crakers", "prix_ht": 4}
}
TAUX_TVA = 0.10
FICHIER_NUMERO = "numero_ticket.txt"

def afficher_produits():
    print("\nListe des produits disponibles :")
    print(f"{'Code':<5}{'Description':<20}{'Prix HT'}")
    for code, info in PRODUITS.items():
        print(f"{code:<5}{info['description']:<20}{info['prix_ht']}€")
    print()

def afficher_erreur_utilisation(message=""):
    print("Erreur :", message)
    print('Utilisation : python3 main.py "Nom Magasin" "Vendeur" "C01:QTE|C02:QTE|..."')
    print('Exemple : python3 main.py "Leclerc" "José" "C01:4|C05:1"')
    afficher_produits()
    sys.exit(1)

def lire_numero_ticket():
    """Lit le dernier numéro de ticket utilisé et l’incrémente."""
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
    # Le nom ne doit contenir que des lettres (et espaces/accents éventuellement)
    return nom.replace(" ", "").isalpha()

def parse_commandes(chaine_commandes):
    """Transforme la chaîne des articles en liste de commandes structurée avec vérification stricte."""
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
            afficher_erreur_utilisation(
                f"Le code article '{code}' n'existe pas."
            )
        # Vérifie que quantité est un entier positif, sans caractère spécial ou lettre
        if not quantite.isdigit():
            afficher_erreur_utilisation(
                f"La quantité '{quantite}' pour l'article '{code}' n'est pas un nombre entier positif."
            )
        quantite_int = int(quantite)
        if quantite_int <= 0:
            afficher_erreur_utilisation(
                f"La quantité '{quantite}' pour l'article '{code}' doit être supérieure à 0."
            )
        liste_commandes.append({
            "code": code,
            "description": PRODUITS[code]["description"],
            "prix_ht": PRODUITS[code]["prix_ht"],
            "quantite": quantite_int
        })
    return liste_commandes

def calculer_totaux(commandes):
    """Calcule les totaux HT, TVA et TTC pour un ticket."""
    total_ht = sum(a["prix_ht"] * a["quantite"] for a in commandes)
    total_tva = total_ht * TAUX_TVA
    total = total_ht + total_tva
    return int(total_ht), round(total_tva, 2), round(total, 2)

def generer_ticket_affichage(ticket):
    """Affiche le ticket au format demandé."""
    lignes = []
    lignes.append(f"{ticket['magasin']}")
    lignes.append(f"Ticket numéro : {ticket['numero_ticket']}")
    lignes.append("")
    lignes.append(f"Date : {ticket['date']}")
    lignes.append("")
    lignes.append(f"Vous avez été servi par : {ticket['vendeur']}")
    lignes.append("")
    lignes.append(f"{'NB':<3} {'Desc.':<15} {'HT unitaire':<10} {'TVA':<5} {'Total'}")
    for a in ticket['articles']:
        montant_ht = a["prix_ht"] * a["quantite"]
        montant_tva = montant_ht * TAUX_TVA
        montant_total = montant_ht + montant_tva
        lignes.append(f"{a['quantite']:<3} {a['description']:<15} {a['prix_ht']}€{'':<3} 10%  {montant_total:.1f}€")
    lignes.append("")
    lignes.append(f"{'Total HT':<17}{ticket['total_ht']}€")
    lignes.append(f"{'Total TVA':<17}{ticket['total_tva']:.1f}€")
    lignes.append(f"{'Total':<17}{ticket['total']:.1f}€")
    return '\n'.join(lignes)

def creer_ticket_par_arguments():
    if len(sys.argv) != 4:
        afficher_erreur_utilisation("Le nombre d'arguments n'est pas correct.")
    nom_magasin = sys.argv[1]
    vendeur = sys.argv[2]
    chaine_commandes = sys.argv[3]

    # Vérification des noms
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