# Auteur : Titouan PLANSON-JEULLAIN // Léo Dumont--Bauer
# Groupe : 3A1
# Date : 16/10/2026
# Description : Programme pour générer un ticket de caisse - version 2

# Importation des modules
import os
import sys
from datetime import datetime

# Catalogue : dictionnaire de dictionnaires, une entrée par article
dic_article: dict = {
    "C01": {"description": "Pack de coca",     "Poids ou volume unitaire" : "2kg"  ,"prix HT unitaire": 5, "tva": 0.20},
    "C02": {"description": "Kilo de pdt",      "Poids ou volume unitaire" : "1kg"  ,"prix HT unitaire": 1, "tva": 0.10},
    "C03": {"description": "Pack de biscotte", "Poids ou volume unitaire" : "950g" ,"prix HT unitaire": 2, "tva": 0.10},
    "C04": {"description": "Café soluble",     "Poids ou volume unitaire" : "250g" ,"prix HT unitaire": 3, "tva": 0.10},
    "C05": {"description": "Crackers",         "Poids ou volume unitaire" : "125g" ,"prix HT unitaire": 4, "tva": 0.20},
    "C06": {"description": "Eau",              "Poids ou volume unitaire" : "1,5L" ,"prix HT unitaire": 6, "tva": 0.10},
    "C07": {"description": "Pain",             "Poids ou volume unitaire" : "250g" ,"prix HT unitaire": 1, "tva": 0.10},
}


def lire_arguments():
    # On attend 3 arguments en plus (sys.argv[0] est le nom du script)
    if len(sys.argv) != 4:
        print('Usage : python3 main.py "Magasin" "Vendeur" "C01:10|C02:2"')
        sys.exit(1)

    magasin = sys.argv[1]
    vendeur = sys.argv[2]
    commande = sys.argv[3]

    articles = []
    # Les articles sont séparés par "|"
    for element in commande.split("|"):
        # Vérification du format CODE:QUANTITE
        if element.count(":") != 1:
            print(f"Erreur : '{element}' n'est pas au format CODE:QUANTITE (ex : C01:2)")
            sys.exit(1)

        code, quantite = element.split(":")
        code = code.strip().upper()
        quantite = quantite.strip()

        # Vérification que l'article existe dans le catalogue
        if code not in dic_article:
            print(f"Erreur : l'article {code} n'existe pas dans le catalogue")
            sys.exit(1)

        # Vérification que la quantité est un nombre entier positif
        if not quantite.isdigit() or int(quantite) == 0:
            print(f"Erreur : la quantité '{quantite}' pour {code} doit être un nombre entier positif")
            sys.exit(1)

        articles.append((code, int(quantite)))

    return magasin, vendeur, articles


def generer_numero_et_date():
    # Numéro de ticket incrémental, sauvegardé dans ticket.txt (départ : 1000)
    fichier = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ticket.txt")
    numero = 1000

    if os.path.exists(fichier):
        with open(fichier, "r", encoding="utf-8") as f:
            contenu = f.read().strip()
        if contenu.isdigit():
            numero = int(contenu)

    with open(fichier, "w", encoding="utf-8") as f:
        f.write(str(numero + 1))

    date = datetime.now().strftime("%d/%m/%Y")
    return str(numero), date


# Fonction pour séparer la valeur et l'unité (ex : "1,5L" -> 1.5 et "L")
def separer_poids_volume(texte: str) -> tuple:
    # On récupère les chiffres (et la virgule) au début du texte
    nombre = ""
    for caractere in texte:
        if caractere.isdigit() or caractere in ",.":
            nombre += caractere
        else:
            break
    # Le reste du texte correspond à l'unité
    unite = texte[len(nombre):].strip()
    return float(nombre.replace(",", ".")), unite


# Fonction pour calculer le poids ou volume total d'une ligne (ex : "950g" x 4 -> "3,8kg")
def calcul_poids_volume_total(poids_unitaire: str, quantite: int) -> str:
    valeur, unite = separer_poids_volume(poids_unitaire)
    total = valeur * quantite

    # Au-delà de 1000g on passe en kg
    if unite == "g" and total >= 1000:
        total = total / 1000
        unite = "kg"

    # On enlève les zéros inutiles puis on remplace le point par une virgule
    texte = f"{total:.3f}".rstrip("0").rstrip(".")
    return texte.replace(".", ",") + unite


# Fonction pour calculer les montants
def calcul_montant(articles: list) -> tuple:
    # Initialisation des variables
    lignes = []
    total_ht = 0
    total_tva = 0

    for code, quantite in articles:
        if code in dic_article:
            article = dic_article[code]
            montant_ht = article["prix HT unitaire"] * quantite
            montant_tva = montant_ht * article["tva"]

            # On garde le détail de la ligne pour l'affichage du ticket
            lignes.append({
                "quantite": quantite,
                "description": article["description"],
                "poids_unitaire": article["Poids ou volume unitaire"],
                "poids_total": calcul_poids_volume_total(article["Poids ou volume unitaire"], quantite),
                "prix_ht": article["prix HT unitaire"],
                "tva": article["tva"],
                "total_ttc": round(montant_ht + montant_tva, 2),
            })

            total_ht += montant_ht
            total_tva += montant_tva

    total_ttc = total_ht + total_tva
    return lignes, round(total_ht, 2), round(total_tva, 2), round(total_ttc, 2)


# Fonction pour formater un montant comme sur l'exemple (ex : 5,5€ ou 16€)
def formater_prix(montant: float) -> str:
    # On enlève les zéros inutiles puis on remplace le point par une virgule
    texte = f"{montant:.2f}".rstrip("0").rstrip(".")
    return texte.replace(".", ",") + "€"


# Fonction pour afficher le ticket dans le terminal
def afficher_ticket(magasin, vendeur, numero, date, lignes, total_ht, total_tva, total_ttc):
    # Largeur du cadre (élargie pour les colonnes poids/volume)
    largeur = 78

    # Construction des lignes du ticket
    contenu = []
    contenu.append(magasin)
    contenu.append(f"Ticket numéro : {numero}")
    contenu.append("")
    contenu.append(f"Date : {date}")
    contenu.append("")
    contenu.append(f"Vous avez été servi par : {vendeur}")
    contenu.append("")

    # En-tête du tableau
    contenu.append(
        f"{'NB':<4}{'Desc.':<18}{'Pds/vol. unit.':<16}{'Pds/vol. total':<16}"
        f"{'HT unitaire':<12}{'TVA':<5}{'Total':>7}"
    )

    # Une ligne par article (description coupée si trop longue pour garder l'alignement)
    for ligne in lignes:
        tva = f"{round(ligne['tva'] * 100)}%"
        contenu.append(
            f"{ligne['quantite']:<4}"
            f"{ligne['description'][:17]:<18}"
            f"{ligne['poids_unitaire']:<16}"
            f"{ligne['poids_total']:<16}"
            f"{formater_prix(ligne['prix_ht']):<12}"
            f"{tva:<5}"
            f"{formater_prix(ligne['total_ttc']):>7}"
        )
    contenu.append("")

    # Totaux alignés à droite
    contenu.append(" " * (largeur - 20) + f"{'Total HT':<12}{formater_prix(total_ht):>8}")
    contenu.append(" " * (largeur - 20) + f"{'Total TVA':<12}{formater_prix(total_tva):>8}")
    contenu.append(" " * (largeur - 20) + f"{'Total':<12}{formater_prix(total_ttc):>8}")

    # Affichage avec un cadre autour, comme sur le modèle
    print("┌" + "─" * (largeur + 2) + "┐")
    for texte in contenu:
        print("│ " + texte.ljust(largeur) + " │")
    print("└" + "─" * (largeur + 2) + "┘")


# Point d'entrée du programme
if __name__ == "__main__":
    magasin, vendeur, articles = lire_arguments()
    numero, date = generer_numero_et_date()
    lignes, total_ht, total_tva, total_ttc = calcul_montant(articles)

    # Affichage du ticket
    afficher_ticket(magasin, vendeur, numero, date, lignes, total_ht, total_tva, total_ttc)