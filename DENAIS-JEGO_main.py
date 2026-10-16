# Programme génération de ticket de caisse
# Maxime DENAIS | Baptiste JEGO
# 3A2
# 16/10/2026
import sys
import os
from datetime import datetime

# --- TÂCHE 1 : Catalogue d'articles ---
CATALOGUE = {
    "C01": {"description": "pack de coca", "prix_ht": 5.0},
    "C02": {"description": "kilo de pdt", "prix_ht": 1.0},
    "C03": {"description": "pack Biscotte", "prix_ht": 2.0},
    "C04": {"description": "Café soluble", "prix_ht": 3.0},
    "C05": {"description": "Crakers", "prix_ht": 4.0}
}

FICHIER_COMPTEUR = "compteur_ticket.txt"
TAUX_TVA = 0.10  # 10% de TVA


def obtenir_numero_ticket():
    """Gère le compteur persistant du numéro de ticket."""
    numero = 1

    if os.path.exists(FICHIER_COMPTEUR):
        try:
            with open(FICHIER_COMPTEUR, "r", encoding="utf-8") as fichier:
                contenu = fichier.read().strip()
                if contenu.isdigit():
                    numero = int(contenu)
        except OSError:
            print("Erreur : impossible de lire le compteur des tickets.")
            sys.exit(1)

    nouveau_numero = numero + 1

    try:
        with open(FICHIER_COMPTEUR, "w", encoding="utf-8") as fichier:
            fichier.write(str(nouveau_numero))
    except OSError:
        print("Erreur : impossible d'enregistrer le numéro du ticket.")
        sys.exit(1)

    return nouveau_numero


def formater_prix(montant):
    """Formate un montant avec une virgule et le symbole €."""
    return f"{montant:.2f}".replace(".", ",") + " €"


def lire_achats(chaine_achats):
    """Vérifie les codes articles et les quantités avant de calculer le ticket."""
    lignes_ticket = []
    total_ht_global = 0.0

    if not chaine_achats.strip():
        print("Erreur : aucun achat n'a été indiqué.")
        sys.exit(1)

    lignes_achats = chaine_achats.split("|")

    for numero_ligne, ligne in enumerate(lignes_achats, start=1):
        ligne = ligne.strip()

        if not ligne:
            print(f"Erreur : achat vide à la position {numero_ligne}.")
            sys.exit(1)

        if ligne.count(":") != 1:
            print(
                f"Erreur : format incorrect pour '{ligne}'. "
                "Utilisez CODE:QUANTITE, par exemple C01:2."
            )
            sys.exit(1)

        code, qte_str = ligne.split(":", 1)
        code = code.strip().upper()
        qte_str = qte_str.strip()

        if code not in CATALOGUE:
            print(
                f"Erreur : le code article '{code}' n'existe pas. "
                f"Codes disponibles : {', '.join(CATALOGUE.keys())}."
            )
            sys.exit(1)

        # La quantité doit être un nombre entier strictement positif.
        if not qte_str.isdigit():
            print(
                f"Erreur : la quantité '{qte_str}' pour l'article {code} "
                "doit être un nombre entier positif."
            )
            sys.exit(1)

        qte = int(qte_str)

        if qte <= 0:
            print(f"Erreur : la quantité pour l'article {code} doit être supérieure à zéro.")
            sys.exit(1)

        article = CATALOGUE[code]
        desc = article["description"]
        prix_unitaire_ht = article["prix_ht"]

        total_ligne_ht = prix_unitaire_ht * qte
        total_ligne_ttc = total_ligne_ht * (1 + TAUX_TVA)
        total_ht_global += total_ligne_ht

        lignes_ticket.append({
            "qte": qte,
            "desc": desc,
            "pu_ht": prix_unitaire_ht,
            "total_ttc": total_ligne_ttc
        })

    return lignes_ticket, total_ht_global


def main():
    # --- TÂCHE 2 : Vérification des arguments de la ligne de commande ---
    if len(sys.argv) != 4:
        print(
            'Erreur. Usage attendu : '
            'python3 main.py "Nom Magasin" "Nom Caissier" "C01:1|C02:2"'
        )
        sys.exit(1)

    nom_magasin = sys.argv[1].strip()
    nom_caissier = sys.argv[2].strip()
    chaine_achats = sys.argv[3]

    if not nom_magasin:
        print("Erreur : le nom du magasin ne peut pas être vide.")
        sys.exit(1)

    if not nom_caissier:
        print("Erreur : le nom du caissier ne peut pas être vide.")
        sys.exit(1)

    # --- TÂCHE 3 : Validation des achats et calculs financiers ---
    lignes_ticket, total_ht_global = lire_achats(chaine_achats)

    total_tva_global = total_ht_global * TAUX_TVA
    total_ttc_global = total_ht_global + total_tva_global

    # --- TÂCHE 4 : Affichage du ticket ---
    numero_ticket = obtenir_numero_ticket()
    date_jour = datetime.now().strftime("%d/%m/%Y")

    contenu_ticket = [
        nom_magasin,
        f"Ticket numéro : {numero_ticket}",
        f"Date : {date_jour}",
        f"Vous avez été servi par : {nom_caissier}",
        "",
        f"{'NB':<4} {'Desc.':<20} {'HT unitaire':<12} {'TVA':<5} {'Total TTC'}"
    ]

    for article in lignes_ticket:
        pu_str = formater_prix(article["pu_ht"])
        total_str = formater_prix(article["total_ttc"])
        contenu_ticket.append(
            f"{article['qte']:<4} {article['desc']:<20} "
            f"{pu_str:<12} {'10%':<5} {total_str}"
        )

    contenu_ticket.append("")

    # Les trois totaux sont alignés à droite du ticket.
    lignes_totaux = [
        f"Total HT : {formater_prix(total_ht_global)}",
        f"Total TVA : {formater_prix(total_tva_global)}",
        f"Total TTC : {formater_prix(total_ttc_global)}"
    ]

    largeur = max(
        max(len(ligne) for ligne in contenu_ticket),
        max(len(ligne) for ligne in lignes_totaux)
    ) + 4

    contenu_ticket.extend(ligne.rjust(largeur - 4) for ligne in lignes_totaux)

    print("+" + "-" * (largeur - 2) + "+")
    for ligne in contenu_ticket:
        print("| " + ligne.ljust(largeur - 4) + " |")
    print("+" + "-" * (largeur - 2) + "+")


if __name__ == "__main__":
    main()
