# Programme génération de ticket de caisse
# Baptiste JEGO | Maxime DENAIS
# 3A2
# 16/10/2026
import sys
import os
from datetime import datetime

# --- Catalogue d'articles mis à jour ---
CATALOGUE = {
    "C01": {"description": "pack de coca", "poids_vol": 2, "unite": "kg", "prix_ht": 5.0, "tva": 0.20},
    "C02": {"description": "kilo de pdt", "poids_vol": 1, "unite": "kg", "prix_ht": 1.0, "tva": 0.10},
    "C03": {"description": "pack Biscotte", "poids_vol": 950, "unite": "g", "prix_ht": 2.0, "tva": 0.10},
    "C04": {"description": "Café soluble", "poids_vol": 250, "unite": "g", "prix_ht": 3.0, "tva": 0.10},
    "C05": {"description": "Crakers", "poids_vol": 125, "unite": "g", "prix_ht": 4.0, "tva": 0.20},
    "C06": {"description": "Eau", "poids_vol": 1.5, "unite": "L", "prix_ht": 6.0, "tva": 0.10},
    "C07": {"description": "Pain", "poids_vol": 250, "unite": "g", "prix_ht": 1.0, "tva": 0.10}
}

FICHIER_COMPTEUR = "compteur_ticket.txt"


def obtenir_numero_ticket():
    numero = 2199
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
    return f"{montant:g}".replace(".", ",") + "€"


def formater_tva(taux):
    return f"{int(taux * 100)}%"


def calculer_affichage_poids(qte, poids_vol, unite):
    total_num = qte * poids_vol
    if unite == "g" and total_num >= 1000:
        total_num = total_num / 1000
        unite_affiche = "kg"
    else:
        unite_affiche = unite
        
    total_str = f"{total_num:g}".replace(".", ",")
    return f"{total_str}{unite_affiche}"


def lire_achats(chaine_achats):
    lignes_ticket = []
    total_ht_global = 0.0
    total_tva_global = 0.0

    if not chaine_achats.strip():
        print("Erreur : aucun achat n'a été indiqué.")
        sys.exit(1)

    lignes_achats = chaine_achats.split("|")

    for numero_ligne, ligne in enumerate(lignes_achats, start=1):
        ligne = ligne.strip()
        if not ligne:
            continue

        if ligne.count(":") != 1:
            print(f"Erreur : format incorrect pour '{ligne}'. Utilisez CODE:QUANTITE.")
            sys.exit(1)

        code, qte_str = ligne.split(":", 1)
        code = code.strip().upper()
        qte_str = qte_str.strip()

        if code not in CATALOGUE:
            print(f"Erreur : le code article '{code}' n'existe pas.")
            sys.exit(1)

        try:
            qte = float(qte_str.replace(",", "."))
            if qte <= 0:
                raise ValueError
        except ValueError:
            print(f"Erreur : la quantité pour {code} doit être un nombre positif (ex: 1 ou 1.5).")
            sys.exit(1)

        article = CATALOGUE[code]
        
        prix_unitaire_ht = article["prix_ht"]
        taux_tva = article["tva"]
        
        total_ligne_ht = prix_unitaire_ht * qte
        montant_tva_ligne = total_ligne_ht * taux_tva
        total_ligne_ttc = total_ligne_ht + montant_tva_ligne

        total_ht_global += total_ligne_ht
        total_tva_global += montant_tva_ligne

        pds_vol_unitaire_str = f"{str(article['poids_vol']).replace('.', ',')}{article['unite']}"
        pds_vol_total_str = calculer_affichage_poids(qte, article["poids_vol"], article["unite"])

        lignes_ticket.append({
            "qte": qte,
            "desc": article["description"],
            "pds_vol_uni": pds_vol_unitaire_str,
            "pds_vol_tot": pds_vol_total_str,
            "pu_ht": prix_unitaire_ht,
            "taux_tva": taux_tva,
            "total_ttc": total_ligne_ttc
        })

    return lignes_ticket, total_ht_global, total_tva_global


def main():
    if len(sys.argv) != 4:
        print('Erreur. Usage : python3 main.py "Nom Magasin" "Nom Caissier" "C01:1|C02:1.5"')
        sys.exit(1)

    nom_magasin = sys.argv[1].strip()
    nom_caissier = sys.argv[2].strip()
    chaine_achats = sys.argv[3]

    if not nom_magasin or not nom_caissier:
        print("Erreur : le nom du magasin et du caissier ne peuvent pas être vides.")
        sys.exit(1)

    lignes_ticket, total_ht_global, total_tva_global = lire_achats(chaine_achats)
    total_ttc_global = total_ht_global + total_tva_global

    numero_ticket = obtenir_numero_ticket()
    date_jour = datetime.now().strftime("%d/%m/%Y")

    contenu_ticket = [
        nom_magasin,
        f"Ticket numéro : {numero_ticket}",
        "",
        f"Date : {date_jour}",
        "",
        f"Vous avez été servi par : {nom_caissier}",
        "",
        f"{'NB':<5} {'Desc.':<18} {'Pds/vol. unitaire':<18} {'Pds/vol. total':<16} {'HT unitaire':<13} {'TVA':<6} {'Total'}"
    ]

    for art in lignes_ticket:
        qte_affichee = f"{art['qte']:g}".replace(".", ",")
        
        pu_str = formater_prix(art["pu_ht"])
        total_str = formater_prix(art["total_ttc"])
        tva_str = formater_tva(art["taux_tva"])
        
        contenu_ticket.append(
            f"{qte_affichee:<5} {art['desc']:<18} {art['pds_vol_uni']:<18} {art['pds_vol_tot']:<16} "
            f"{pu_str:<13} {tva_str:<6} {total_str}"
        )

    contenu_ticket.append("")

    lignes_totaux = [
        f"Total HT : {formater_prix(total_ht_global)}",
        f"Total TVA : {formater_prix(total_tva_global)}",
        f"Total : {formater_prix(total_ttc_global)}"
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
