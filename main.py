from datetime import datetime
import random

def afficher_ticket_caisse(date, nom_client, nom_magasin, pourcentage_tva, articles, somme_totale):
    """
    Génère un ticket de caisse formaté similaire à l'exemple fourni et l'enregistre dans un fichier .txt
    
    Args:
        date (str): Date du ticket (format: "DD/MM/YYYY")
        nom_client (str): Nom du client/vendeur
        nom_magasin (str): Nom du magasin
        pourcentage_tva (float): Pourcentage de la TVA (ex: 10.0 pour 10%)
        articles (list): Liste des articles sous forme de dictionnaires 
                        [{"nom": "Article", "quantite": 1, "prix_ht": 5.00}, ...]
        somme_totale (float): Somme totale TTC du ticket
    
    Returns:
        str: Le nom du fichier généré
    """
    
    # Génération d'un numéro de ticket aléatoire
    numero_ticket = random.randint(1000, 9999)
    
    # Formatage de la date pour le nom du fichier
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    nom_fichier = f"ticket_caisse_{timestamp}.txt"
    
    # Calcul des totaux
    total_ht = 0
    total_tva = 0
    
    # Création du contenu du ticket
    contenu_ticket = []
    
    # En-tête du ticket (style encadré)
    largeur = 60
    contenu_ticket.append("+" + "-" * (largeur - 2) + "+")
    contenu_ticket.append("|" + nom_magasin.center(largeur - 2) + "|")
    contenu_ticket.append("|" + f"Ticket numéro : {numero_ticket}".ljust(largeur - 2) + "|")
    contenu_ticket.append("|" + " " * (largeur - 2) + "|")
    contenu_ticket.append("|" + f"Date : {date}".ljust(largeur - 2) + "|")
    contenu_ticket.append("|" + " " * (largeur - 2) + "|")
    contenu_ticket.append("|" + f"Vous avez été servi par : {nom_client}".ljust(largeur - 2) + "|")
    contenu_ticket.append("|" + " " * (largeur - 2) + "|")
    
    # En-tête du tableau
    contenu_ticket.append("|" + f"{'NB':<3} {'Desc.':<20} {'HT unitaire':<12} {'TVA':<5} {'Total':<10}".ljust(largeur - 2) + "|")
    
    # Articles
    for i, article in enumerate(articles, 1):
        nom = article["nom"]
        quantite = article["quantite"]
        prix_ht = article["prix_ht"]
        
        # Calcul du prix TTC pour cet article
        prix_ttc = prix_ht * (1 + pourcentage_tva / 100)
        total_article_ttc = quantite * prix_ttc
        total_article_ht = quantite * prix_ht
        
        # Accumulation des totaux
        total_ht += total_article_ht
        total_tva += total_article_ttc - total_article_ht
        
        # Formatage de la ligne article
        ligne = f"{quantite:<3} {nom:<20} {prix_ht}€{'':<7} {pourcentage_tva:g}% {total_article_ttc:.1f}€"
        contenu_ticket.append("|" + ligne.ljust(largeur - 2) + "|")
    
    # Ligne vide
    contenu_ticket.append("|" + " " * (largeur - 2) + "|")
    
    # Totaux
    contenu_ticket.append("|" + f"{'Total HT':<40} {total_ht:.0f}€".ljust(largeur - 2) + "|")
    contenu_ticket.append("|" + f"{'Total TVA':<40} {total_tva:.1f}€".ljust(largeur - 2) + "|")
    contenu_ticket.append("|" + f"{'Total':<40} {somme_totale:.1f}€".ljust(largeur - 2) + "|")
    
    # Fermeture du cadre
    contenu_ticket.append("+" + "-" * (largeur - 2) + "+")
    
    # Écriture dans le fichier
    with open(nom_fichier, 'w', encoding='utf-8') as fichier:
        for ligne in contenu_ticket:
            fichier.write(ligne + '\n')
    
    print(f"Ticket de caisse généré avec succès: {nom_fichier}")
    return nom_fichier


# Exemple d'utilisation reproduisant le ticket de l'image
if __name__ == "__main__":
    # Reproduction de l'exemple du ticket BUT Market
    articles_exemple = [
        {"nom": "pack de coca", "quantite": 1, "prix_ht": 5.0},
        {"nom": "kilo de pdt", "quantite": 3, "prix_ht": 1.0},
        {"nom": "pack Biscotte", "quantite": 4, "prix_ht": 2.0}
    ]
    
    # Génération du ticket identique à l'exemple
    afficher_ticket_caisse(
        date="08/09/2023",
        nom_client="Lisa",
        nom_magasin="BUT Market",
        pourcentage_tva=10.0,
        articles=articles_exemple,
        somme_totale=17.6
    )
    
    print("\n" + "="*50)
    print("Exemple avec d'autres données :")
    print("="*50)
    
    # Autre exemple
    autres_articles = [
        {"nom": "Pain complet", "quantite": 2, "prix_ht": 1.50},
        {"nom": "Fromage de chèvre", "quantite": 1, "prix_ht": 4.20},
        {"nom": "Salade verte", "quantite": 1, "prix_ht": 1.80}
    ]
    
    afficher_ticket_caisse(
        date="01/10/2025",
        nom_client="Marie",
        nom_magasin="SuperMarché Plus",
        pourcentage_tva=20.0,
        articles=autres_articles,
        somme_totale=9.18
    )