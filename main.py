import sys
from datetime import datetime


# Obtenir la date sous le format "jour/mois/annee"
def get_date(today):
    date_format = today.strftime("%d/%m/%Y")
    return date_format


# On récupère le numéro du ticket actuel
def get_ticket():
    try:
        with open('numero_ticket.txt', 'r') as file:
            numero_ticket = int(file.read().strip())
            return numero_ticket
    except FileNotFoundError:
        # Si le fichier n'existe pas, on retourne 0 par défault
        return 0


# On incrémente le ticket de 1
def increment_ticket():
    numero_ticket_suivant = numero_ticket + 1
    with open('numero_ticket.txt', 'w') as file:
        file.write(str(numero_ticket_suivant))


# On affiche le haut du ticket
def top_header_ticket(e, n_c, t):
    print(f"{e}")
    print(f"Ticket numéro : {t}\n")
    print(f"Date : {date}\n")
    print(f"Vous avez été servi par {n_c}\n")


# On récupère le 3ème argument, donc les produits avec le code d'article et la quantité asssociée
def get_products(products):
    # Initialiser un dictionnaire pour stocker les codes d'articles et les quantités
    articles_quantites = {}

    # Le séparateur des produits est '|'
    separation = products.split('|')

    # chaque produit, on récupère le code article et la quantité associée
    for s in separation:

        # Divisier "code:quantité" en utilisant les '|'
        parts = s.split(':')

        if (len(parts)) == 2:
            code_article = parts[0]
            quantite = int(parts[1])

            articles_quantites[code_article] = quantite
    return articles_quantites


# On récupère la TVA du Pays
def get_TVA_by_country(pays):
    if pays in ["Lituanie", "Angleterre"]:
        tva = 1.2
        tva_affichage = "20%"
    else:
        tva = 1.1
        tva_affichage = "10%"
    return tva, tva_affichage


# On récupère le poids du produit avec sa bonne unité
def get_poids(poids_article, unite):
    if unite == "g":
        if poids_article >= 1000:
            poids_article = poids_article / 1000
            unite = "kg"
    return poids_article, unite


# On affiche les produits, au milieu du ticket
def middle_ticket(article_quantite, total_HT, total_TVA):
    # On parcourt les différents articles, et on en déduit le prix et la description de celui-ci
    for code_article, quantite in article_quantite.items():
        description = ""
        if code_article == "C01":
            description = "pack de coca"
            prix = 5
            poids_volume = 2
            unite = "kg"
            origine = "Lituanie"
        elif code_article == "C02":
            description = "kit de pft"
            prix = 1
            poids_volume = 1
            unite = "kg"
            origine = "Espagne"
        elif code_article == "C03":
            description = "pack Biscotte"
            prix = 2
            poids_volume = 950
            unite = "g"
            origine = "France"
        elif code_article == "C04":
            description = "Café soluble"
            prix = 3
            poids_volume = 250
            unite = "g"
            origine = "Roumanie"
        elif code_article == "C05":
            description = "Crackers"
            prix = 4
            poids_volume = 125
            unite = "g"
            origine = "Angleterre"
        elif code_article == "C06":
            description = "Eau"
            prix = 6
            poids_volume = 1.5
            unite = "L"
            origine = "Suisse"
        elif code_article == "C07":
            description = "Pain"
            prix = 1
            poids_volume = 250
            unite = "g"
            origine = "France"

        tva, tva_affichage = get_TVA_by_country(origine)

        # calcul prix avec et sans TVA de l'article
        prix_article_avec_TVA = prix * quantite * tva
        prix_article_sans_TVA = prix * quantite
        poids_total_article = poids_volume * quantite
        new_poids_article, new_unite = get_poids(poids_total_article, unite)

        # calcul du coût total de la TVA de l'article
        TVA = prix_article_avec_TVA - prix_article_sans_TVA
        total_TVA += TVA

        # calcul du coût total sans TVA de l'article
        total_HT += prix_article_sans_TVA

        print(f"{quantite}\t{description}\t{poids_volume}{unite}\t\t\t{round(new_poids_article, 2)}{new_unite}\t\t{round(prix, 2)}\t\t{tva_affichage}\t{round(prix_article_avec_TVA, 2)}€")
    return total_HT, total_TVA


# On affiche les infos de bas de ticket (TOTAL HT / TOTAL TVA / TOTAL)
def footer_ticket(total_HT, total_TVA):
    print(f"\n                     TOTAL HT          {round(total_HT, 2)}€")
    print(f"                     TOTAL TVA         {round(total_TVA, 2)}€")
    print(f"                     TOTAL             {round(total_HT + total_TVA, 2)}€")


if __name__ == "__main__":
    date = get_date(datetime.today())

    nom_entreprise = sys.argv[1]
    nom_caissiere = sys.argv[2]
    produits = sys.argv[3]

    numero_ticket = get_ticket()

    increment_ticket()

    total_HT = 0
    total_TVA = 0

    top_header_ticket(nom_entreprise, nom_caissiere, numero_ticket)

    print("NB\tDesc.\t\tpoids/volume unitaire\tpoids/volume total\HT unitaire\tTVA\tTotal")

    # python3 main.py “But Maket” “Lisa” “C01:10|C02:2|C03:5”

    article_quantite = get_products(produits)

    total_HT, total_TVA = middle_ticket(article_quantite, total_HT, total_TVA)

    footer_ticket(total_HT, total_TVA)
