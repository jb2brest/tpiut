# SCRIPT DE GENERATION D'UN TICKET DE CAISSE
# LE GUEN Théo & SIMON Axel - 3A2
# 16/10/2026
#

import sys                  # accès aux paramètres (sys.argv) et à sys.exit
import os                   # pour tester l'existence du fichier d'index
from datetime import date   # pour afficher la date du jour sur le ticket

# INVENTAIRE DES PRODUITS
# clé = code article, valeur = description et prix hors taxe en euros
INVENTAIRE = {
    "C01": {"description": "pack de coca", "prix_ht": 5.0},
    "C02": {"description": "kilo de pdt", "prix_ht": 1.0},
    "C03": {"description": "pack Biscotte", "prix_ht": 2.0},
    "C04": {"description": "Café soluble", "prix_ht": 3.0},
    "C05": {"description": "Crakers", "prix_ht": 4.0}
}

INDEX_FILE = "index.txt" # fichier contenant l'index du ticket
TVA = 0.10 # une TVA de 10%
LARGEUR = 54 # largeur du contenu du ticket (sans les bordures)


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


def euros(montant):
    # formate un montant : 5.5 -> "5,50 €"
    # :.2f garde 2 décimales, puis on remplace le point par une virgule (format français)
    return f"{montant:.2f}".replace(".", ",") + " €"


def afficher_ticket(magasin, caissier, articles):
    # construit puis affiche le ticket de caisse complet
    numero = prochain_numero_ticket()

    # on prépare toutes les lignes avant de les afficher
    # (cela permet de calculer la largeur du cadre à la fin)
    lignes = [
        magasin,
        "Ticket numéro : " + str(numero),
        "Date : " + date.today().strftime("%d/%m/%Y"),
        "Vous avez été servi par : " + caissier,
        "",
        # en-tête du tableau : :<N aligne le texte à gauche sur N caractères
        f"{'NB':<5}{'Desc.':<21}{'HT unitaire':<13}{'TVA':<6}{'Total TTC':<9}"
    ]

    # une ligne du tableau par article, en cumulant le total HT
    total_ht = 0
    for code, quantite in articles:
        produit = INVENTAIRE[code]
        prix_ht = produit["prix_ht"]
        # total de la ligne TTC = prix HT x quantité x (1 + TVA)
        total_ligne_ttc = prix_ht * quantite * (1 + TVA)
        total_ht += prix_ht * quantite
        # la description est coupée à 20 caractères pour ne pas casser les colonnes
        description = produit["description"][:20]
        tva_texte = str(int(TVA * 100)) + "%"  # 0.10 -> "10%"
        lignes.append(f"{quantite:<5}{description:<21}{euros(prix_ht):<13}{tva_texte:<6}{euros(total_ligne_ttc):<9}")

    # calcul des totaux à partir du total HT
    total_tva = total_ht * TVA
    total_ttc = total_ht + total_tva

    totaux = [
        "Total HT : " + euros(total_ht),
        "Total TVA : " + euros(total_tva),
        "Total TTC : " + euros(total_ttc)
    ]

    # le ticket s'élargit si un nom (magasin, caissier) est trop long
    largeur = max([LARGEUR] + [len(l) for l in lignes + totaux])

    # ligne vide puis totaux alignés à droite (rjust)
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
