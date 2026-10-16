import json
import os
import sys
from datetime import datetime

FICHIER_CATALOGUE = "catalogue.json"

CATALOGUE_DEFAUT = {
    "C01": {"nom": "pack de coca", "prix_ht": 5.0, "tva": 10},
    "C02": {"nom": "kilo de pdt", "prix_ht": 1.0, "tva": 10},
    "C03": {"nom": "pack Biscotte", "prix_ht": 2.0, "tva": 10},
    "C04": {"nom": "Café soluble", "prix_ht": 3.0, "tva": 10},
    "C05": {"nom": "Crakers", "prix_ht": 4.0, "tva": 10},
}


def sauvegarder_catalogue(catalogue):
    with open(FICHIER_CATALOGUE, "w", encoding="utf-8") as f:
        json.dump(catalogue, f, indent=4, ensure_ascii=False)


def charger_catalogue():
    """Charge le catalogue depuis le JSON, ou le crée avec les valeurs par défaut."""
    if os.path.exists(FICHIER_CATALOGUE):
        with open(FICHIER_CATALOGUE, "r", encoding="utf-8") as f:
            return json.load(f)
    sauvegarder_catalogue(CATALOGUE_DEFAUT)
    return dict(CATALOGUE_DEFAUT)


CATALOGUE = charger_catalogue()


def ajouter_article_catalogue(code, nom, prix_ht, tva=10):
    """Ajoute un produit et le sauvegarde de façon permanente."""
    if code in CATALOGUE:
        print(f"Erreur : le code {code} existe déjà.")
        sys.exit(1)
    CATALOGUE[code] = {"nom": nom, "prix_ht": float(prix_ht), "tva": tva}
    sauvegarder_catalogue(CATALOGUE)


def main():
    if len(sys.argv) < 4:
        print("Erreur : arguments manquants.")
        print('Utilisation : python main.py "Magasin" "Caissier" "C01:1|C02:3" ["CODE:NOM:PRIX:TVA"]')
        sys.exit(1)

    magasin = sys.argv[1]
    caissier = sys.argv[2]
    commande = sys.argv[3]

    # Ajout optionnel d'un produit (4e argument) : "C06:Jus d'orange:3.5:10"
    if len(sys.argv) >= 5:
        try:
            code, nom, prix, tva = sys.argv[4].split(":", 3)
            ajouter_article_catalogue(code, nom, prix, int(tva))
        except ValueError:
            print('Erreur : format du produit invalide. Attendu : "CODE:NOM:PRIX:TVA"')
            sys.exit(1)

    date_du_jour = datetime.now().strftime("%d/%m/%Y")

    print(f"{magasin}")
    print("Ticket numéro : 2200")
    print(f"Date : {date_du_jour}\n")
    print(f"Vous avez été servi par : {caissier}\n")

    print(f"{'NB':<4} {'Desc.':<15} {'HT unitaire':<12} {'TVA':<6} {'Total':<6}")

    total_ht_global = 0.0
    total_tva_global = 0.0

    for item in commande.split("|"):
        if ":" not in item:
            continue

        code, qte_str = item.split(":", 1)
        try:
            qte = int(qte_str)
        except ValueError:
            print(f"Ligne ignorée (quantité invalide) : {item}")
            continue

        if code not in CATALOGUE:
            print(f"Ligne ignorée (code inconnu) : {code}")
            continue

        article = CATALOGUE[code]
        nom = article["nom"]
        prix_ht = article["prix_ht"]
        taux_tva = article["tva"]

        ligne_ht = prix_ht * qte
        ligne_tva = ligne_ht * (taux_tva / 100)
        ligne_ttc = ligne_ht + ligne_tva

        total_ht_global += ligne_ht
        total_tva_global += ligne_tva

        print(
            f"{qte:<4} {nom:<15} {f'{prix_ht:.2f}€':<12} "
            f"{f'{taux_tva}%':<6} {ligne_ttc:.2f}€"
        )

    total_ttc_global = total_ht_global + total_tva_global

    print("\n" + " " * 20 + f"Total HT        {total_ht_global:.2f}€")
    print(" " * 20 + f"Total TVA       {total_tva_global:.2f}€")
    print(" " * 20 + f"Total           {total_ttc_global:.2f}€")


if __name__ == "__main__":
    main()
