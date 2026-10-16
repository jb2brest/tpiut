# SCRIPT DE GENERATION D'UN TICKET DE CAISSE
# LE GUEN Théo & SIMON Axel - 3A2
# 16/10/2026
#

import sys                  # accès aux paramètres (sys.argv) et à sys.exit
import os                   # pour tester l'existence du fichier d'index
from datetime import date   # pour afficher la date du jour sur le ticket

# INVENTAIRE DES PRODUITS
# clé = code article, valeur = description, poids/volume unitaire et son unité,
# prix hors taxe en euros et taux de TVA propre au produit
INVENTAIRE = {
    "C01": {"description": "pack de coca", "poids_vol": 2, "unite": "kg", "prix_ht": 5.0, "tva": 0.20},
    "C02": {"description": "kilo de pdt", "poids_vol": 1, "unite": "kg", "prix_ht": 1.0, "tva": 0.10},
    "C03": {"description": "pack Biscotte", "poids_vol": 950, "unite": "g", "prix_ht": 2.0, "tva": 0.10},
    "C04": {"description": "Café soluble", "poids_vol": 250, "unite": "g", "prix_ht": 3.0, "tva": 0.10},
    "C05": {"description": "Crakers", "poids_vol": 125, "unite": "g", "prix_ht": 4.0, "tva": 0.20},
    "C06": {"description": "Eau", "poids_vol": 1.5, "unite": "L", "prix_ht": 6.0, "tva": 0.10},
    "C07": {"description": "Pain", "poids_vol": 250, "unite": "g", "prix_ht": 1.0, "tva": 0.10}
}

INDEX_FILE = "index.txt" # fichier contenant l'index du ticket
LARGEUR = 40 # largeur minimale du contenu du ticket (sans les bordures)


def erreur(message):
    # affiche un message d'erreur et quitte le script
    print("Erreur : " + message)
    # on rappelle la bonne syntaxe pour aider l'utilisateur
    print('Usage : python3 main.py "Nom Magasin" "Nom Caissier" "C01:10|C02:2"')
    # code de retour 1 = le script s'est terminé sur une erreur
    sys.exit(1)


def verifier_parametres():
    # vérifie les paramètres et renvoie (magasin, caissier, liste des articles)

    # sys.argv[0] est le nom du script, il faut donc 4 éléments au total
    if len(sys.argv) != 4:
        erreur("il faut exactement 3 paramètres.")

    # strip() retire les espaces inutiles au début et à la fin
    magasin = sys.argv[1].strip()
    caissier = sys.argv[2].strip()
    articles_texte = sys.argv[3].strip()

    # aucun des paramètres ne doit être vide
    if magasin == "":
        erreur("le nom du magasin est vide.")
    if caissier == "":
        erreur("le nom du caissier est vide.")
    if articles_texte == "":
        erreur("la liste des articles est vide.")

    # liste de tuples (code, quantité) construite à partir du 3e paramètre
    articles = []
    # les articles sont séparés par des "|"
    for element in articles_texte.split("|"):
        # chaque article doit contenir exactement un ":" entre le code et la quantité
        if element.count(":") != 1:
            erreur("article mal formé '" + element + "' (attendu CODE:QUANTITE).")
        code, quantite = element.split(":")
        # on accepte le code en minuscules (ex : "c01" -> "C01")
        code = code.strip().upper()
        quantite = quantite.strip()

        # le code doit exister dans l'inventaire
        if code not in INVENTAIRE:
            erreur("le code article '" + code + "' n'existe pas (codes disponibles : "
                   + ", ".join(INVENTAIRE) + ").")
        # la quantité doit être un entier strictement positif
        # (isdigit() refuse aussi les nombres négatifs et décimaux)
        if not quantite.isdigit() or int(quantite) <= 0:
            erreur("la quantité '" + quantite + "' de l'article " + code + " est invalide.")

        articles.append((code, int(quantite)))

    return magasin, caissier, articles


def prochain_numero_ticket():
    # lit le dernier numéro dans INDEX_FILE, l'incrémente et le sauvegarde
    numero = 0  # valeur par défaut si le fichier n'existe pas encore
    try:
        if os.path.exists(INDEX_FILE):
            with open(INDEX_FILE, "r", encoding="utf-8") as fichier:
                contenu = fichier.read().strip()
                # si le contenu est corrompu (pas un nombre), on repart de 0
                if contenu.isdigit():
                    numero = int(contenu)
        numero += 1
        # on écrase l'ancien numéro par le nouveau pour le prochain ticket
        with open(INDEX_FILE, "w", encoding="utf-8") as fichier:
            fichier.write(str(numero))
    except OSError:
        # problème d'accès au fichier (droits, disque plein, ...)
        print("Erreur : impossible de lire ou d'écrire le fichier " + INDEX_FILE + ".")
        sys.exit(1)
    return numero


def nombre(valeur):
    # formate un nombre sans zéros inutiles : 3.30 -> "3,3", 19.0 -> "19"
    # :.2f arrondit à 2 décimales, on retire les 0 puis la virgule en trop à la fin
    texte = f"{valeur:.2f}".rstrip("0").rstrip(".")
    # virgule à la place du point (format français)
    return texte.replace(".", ",")


def euros(montant):
    # formate un montant : 5.5 -> "5,5€"
    return nombre(montant) + "€"


def afficher_ticket(magasin, caissier, articles):
    # construit puis affiche le ticket de caisse complet
    numero = prochain_numero_ticket()

    # on prépare toutes les lignes avant de les afficher
    # (cela permet de calculer la largeur du cadre à la fin)
    lignes = [
        magasin,
        "Ticket numéro : " + str(numero),
        "",
        "Date : " + date.today().strftime("%d/%m/%Y"),
        "",
        "Vous avez été servi par : " + caissier,
        "",
        # en-tête du tableau : :<N aligne le texte à gauche sur N caractères
        f"{'NB':<6}{'Desc.':<19}{'Pds/vol. unitaire':<19}{'Pds/vol. total':<17}"
        f"{'HT unitaire':<14}{'TVA':<7}{'Total'}"
    ]

    # une ligne du tableau par article, en cumulant le total HT et le total TVA
    # (la TVA dépend maintenant du produit, on ne peut plus la calculer à la fin)
    total_ht = 0
    total_tva = 0
    for code, quantite in articles:
        produit = INVENTAIRE[code]
        prix_ht = produit["prix_ht"]
        tva = produit["tva"]
        ligne_ht = prix_ht * quantite
        ligne_tva = ligne_ht * tva
        total_ht += ligne_ht
        total_tva += ligne_tva
        # poids/volume : unitaire, puis multiplié par la quantité (ex : 2kg x 2 -> 4kg)
        pds_unitaire = nombre(produit["poids_vol"]) + produit["unite"]
        pds_total = nombre(produit["poids_vol"] * quantite) + produit["unite"]
        # description coupée pour ne pas casser les colonnes
        description = produit["description"][:18]
        tva_texte = str(round(tva * 100)) + "%"  # 0.20 -> "20%"
        lignes.append(f"{quantite:<6}{description:<19}{pds_unitaire:<19}{pds_total:<17}"
                      f"{euros(prix_ht):<14}{tva_texte:<7}{euros(ligne_ht + ligne_tva)}")

    total_ttc = total_ht + total_tva

    # (libellé, montant) : libellés alignés à droite pour aligner les ":",
    # montants alignés à droite pour aligner les "€"
    valeurs = [
        ("Total HT", euros(total_ht)),
        ("Total TVA", euros(total_tva)),
        ("Total", euros(total_ttc))
    ]
    larg_libelle = max(len(libelle) for libelle, _ in valeurs)
    larg_montant = max(len(montant) for _, montant in valeurs)
    totaux = [f"{libelle:>{larg_libelle}} : {montant:>{larg_montant}}" for libelle, montant in valeurs]

    # largeur ajustée au contenu le plus long (le tableau en général),
    # le ticket s'élargit si un nom (magasin, caissier) est trop long
    largeur = max([LARGEUR] + [len(l) for l in lignes + totaux])

    # ligne vide puis bloc des totaux collé à droite (rjust)
    lignes.append("")
    lignes += [t.rjust(largeur) for t in totaux]

    # affichage du cadre : bordure haute, lignes complétées par des espaces (ljust), bordure basse
    # le "+ 2" correspond aux espaces entre le texte et les "|"
    bordure = "+" + "-" * (largeur + 2) + "+"
    print(bordure)
    for l in lignes:
        print("| " + l.ljust(largeur) + " |")
    print(bordure)


# point d'entrée : ce code n'est exécuté que si on lance le fichier directement
# (et pas s'il est importé depuis un autre script)
if __name__ == "__main__":
    magasin, caissier, articles = verifier_parametres()
    afficher_ticket(magasin, caissier, articles)
