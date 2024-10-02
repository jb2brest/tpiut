'''
validation 1
#──────────────────────────────────────────────────────────────────────────────────────────────────────────
#─────────────────────────────────────IMPORTATION DES BIBLIOTHEQUES────────────────────────────────────────
#──────────────────────────────────────────────────────────────────────────────────────────────────────────

import sys
from datetime import datetime 

#────────────────────────────────────────CREATION DU DICTIONNAIRE──────────────────────────────────────────

# Liste des articles
articles = {
    "C01": {"description": "pack de coca", "prix": 5},
    "C02": {"description": "kilo de pdt", "prix": 1},
    "C03": {"description": "pack Biscotte", "prix": 2},
    "C04": {"description": "Café soluble", "prix": 3},
    "C05": {"description": "Crakers", "prix": 4}
}


#────────────────────────────────────────CREATION DE LA FONCTION──────────────────────────────────────────

# Nom du fichier pour stocker le numéro de ticket
fichier_ticket = 'numero_ticket.txt'

def lire_numero_ticket(fichier):
    try:
        with open(fichier, 'r') as f:
            return int(f.read().strip())
    except (FileNotFoundError, ValueError):
        return 0  # Retourne 0 si le fichier n'existe pas ou contient une valeur invalide

def ecrire_numero_ticket(fichier, numero):
    with open(fichier, 'w') as f:
        f.write(str(numero))

def calculer_ticket(nom_magasin, employe, achats):
    date = datetime.now().strftime("%d/%m/%Y")
    
    # Lire le numéro de ticket actuel et l'incrémenter
    ticket_numero = lire_numero_ticket(fichier_ticket)
    ticket_numero += 1
    ecrire_numero_ticket(fichier_ticket, ticket_numero)

    taux_tva: float = 0.10                                  #initialisation de la taxe
    total_ht: int = 0
    total_tva: int = 0
    total_ttc: int = 0

    print(nom_magasin, "\n Ticket numéro :", ticket_numero, "\n")
    print("Date :", date, "\n")
    print("Vous avez été servi par :", employe, "\n")
    print(f"{'NB':<3} {'Desc.':<20} {'HT unitaire':<15} {'TVA':<5} {'Total':<10}")
    
    for achat in achats:                                    #boucle qui permet de contabiliser tous les produits saisis
        code, quantite = achat.split(':')
        quantite = int(quantite)

        if code in articles:
            article = articles[code]
            prix_ht = article["prix"]
            total_article_ht = prix_ht * quantite
            tva = total_article_ht * taux_tva
            total_article_ttc = total_article_ht + tva

            total_ht += total_article_ht
            total_tva += tva
            total_ttc += total_article_ttc

            print(f"{quantite:<3} {article['description']:<20} {prix_ht}€"
                  f"{' ':<10} {int(taux_tva * 100)}%  {total_article_ttc:.1f}€")

    print(f"\n{'Total HT':<30} {total_ht:.1f}€")          #affichage du prix avec et sans taxe
    print(f"{'Total TVA':<30} {total_tva:.1f}€")
    print(f"{'Total':<30} {total_ttc:.1f}€")

#────────────────────────────────────────PROGRAMME PRINCIPAL──────────────────────────────────────────

if __name__ == "__main__":                      #si le nombre de paramètre est different de 4, une aide est affichée ( le nom du fichier fait parti des paramètres)
    if len(sys.argv) != 4:
        print('Utilisation : python3 main.py "Nom Magasin" "Employe" "Achats"')
        sys.exit(1)

    nom_magasin = sys.argv[1]
    employe = sys.argv[2]
    achats = sys.argv[3].split("|")

    calculer_ticket(nom_magasin, employe, achats)

'''
#validation 2 

import sys
from datetime import datetime 

# Liste des articles
articles = {
    "C01": {"description": "pack de coca", "poids_volume": "2kg", "prix": 5, "tva": 0.20, "origine": "Lituanie"},
    "C02": {"description": "kilo de pdt", "poids_volume": "1kg", "prix": 1, "tva": 0.10, "origine": "Espagne"},
    "C03": {"description": "pack Biscotte", "poids_volume": "950g", "prix": 2, "tva": 0.10, "origine": "France"},
    "C04": {"description": "Café soluble", "poids_volume": "250g", "prix": 3, "tva": 0.10, "origine": "Roumanie"},
    "C05": {"description": "Crakers", "poids_volume": "125g", "prix": 4, "tva": 0.20, "origine": "Angleterre"},
    "C06": {"description": "Eau", "poids_volume": "1,5L", "prix": 6, "tva": 0.10, "origine": "Suisse"},
    "C07": {"description": "Pain", "poids_volume": "250g", "prix": 1, "tva": 0.10, "origine": "France"},
}

# Nom du fichier pour stocker le numéro de ticket
fichier_ticket = 'numero_ticket.txt'

def lire_numero_ticket(fichier):
    try:
        with open(fichier, 'r') as f:
            return int(f.read().strip())
    except (FileNotFoundError, ValueError):
        return 0  # Retourne 0 si le fichier n'existe pas ou contient une valeur invalide

def ecrire_numero_ticket(fichier, numero):
    with open(fichier, 'w') as f:
        f.write(str(numero))

def calculer_ticket(nom_magasin, employe, achats):
    date = datetime.now().strftime("%d/%m/%Y")
    
    # Lire le numéro de ticket actuel et l'incrémenter
    ticket_numero = lire_numero_ticket(fichier_ticket)
    ticket_numero += 1
    ecrire_numero_ticket(fichier_ticket, ticket_numero)

    total_ht = 0                            #initialisation de la taxe
    total_tva = 0
    total_ttc = 0

    print(nom_magasin, "\n Ticket numéro :", ticket_numero, "\n")       
    print("Date :", date, "\n")
    print("Vous avez été servi par :", employe, "\n")
    print(f"{'NB':<3} {'Desc.':<20} {'Poids/volume unitaire':<20} {'Poids/volume total':<20} {'HT unitaire':<15} {'TVA':<5} {'Total':<10}")
    
    for achat in achats:                                                #boucle qui permet de contabiliser tous les produits saisis
        code, quantite = achat.split(':')
        quantite = int(quantite)

        if code in articles:
            article = articles[code]
            prix_ht = article["prix"]
            total_article_ht = prix_ht * quantite
            tva = total_article_ht * article["tva"]
            total_article_ttc = total_article_ht + tva
            
            total_ht += total_article_ht
            total_tva += tva
            total_ttc += total_article_ttc
            
            # Poids/volume total
            poids_volume_total = f"{quantite * float(article['poids_volume'].replace('kg', '').replace('g', '').replace('L', '').replace(',', '.')):.1f}{article['poids_volume'][-2:]}" 

            print(f"{quantite:<3} {article['description']:<20} {article['poids_volume']:<20} {poids_volume_total:<20} {prix_ht:.1f}€"
                  f"{' ':<10} {int(article['tva'] * 100)}%  {total_article_ttc:.1f}€")

    print(f"\n{'Total HT':<30} {total_ht:.1f}€")
    print(f"{'Total TVA':<30} {total_tva:.1f}€") #affichage du prix avec et sans taxe
    print(f"{'Total':<30} {total_ttc:.1f}€")

# Programme principal
if __name__ == "__main__":                                      
    if len(sys.argv) != 4:
        print('Utilisation : python3 main.py "Nom Magasin" "Employe" "Achats"')
        sys.exit(1)

    nom_magasin = sys.argv[1]               #si le nombre de paramètre est different de 4, une aide est affichée ( le nom du fichier fait parti des paramètres)
    employe = sys.argv[2]
    achats = sys.argv[3].split("|")

    calculer_ticket(nom_magasin, employe, achats)
