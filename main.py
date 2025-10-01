# =============================================================================
# SYSTÈME DE GESTION DE TICKETS DE CAISSE
# =============================================================================
# Auteur: [Votre nom]
# Date: 1 octobre 2025
# Usage: python main.py "Nom_Magasin" "Nom_Client" "C01:10|C02:2"
# =============================================================================

from datetime import datetime
import random
import sys

# Variables globales
stockage = []
code_counter = 1

# =============================================================================
# FONCTIONS DE GESTION DU STOCKAGE
# =============================================================================

def stockage_list():
    """Initialise la liste de stockage"""
    global stockage, code_counter
    stockage = []
    code_counter = 1

def stockage_ajouter_produit(description: str, prix_ht_unitaire: float):
    """Ajoute un produit dans le stockage"""
    global stockage, code_counter
    product = {
        "code_produit": code_counter,
        "description": description,
        "prix_ht_unitaire": prix_ht_unitaire
    }
    stockage.append(product)
    code_counter += 1

def afficher_stockage():
    """Affiche la liste des produits en stockage"""
    if not stockage:
        print("Le stockage est vide.")
    else:
        print("Liste des produits en stockage :")
        for produit in stockage:
            print(f"Code produit: {produit['code_produit']}, Description: {produit['description']}, Prix HT unitaire: {produit['prix_ht_unitaire']} €")


# =============================================================================
# FONCTIONS DE CONVERSION ET TRAITEMENT DES DONNÉES
# =============================================================================
# FONCTIONS DE CONVERSION ET TRAITEMENT
# =============================================================================

def convertir_stockage_vers_articles(codes_produits_et_quantites):
    """Convertit les produits du stockage au format attendu par afficher_ticket_caisse"""
    articles = []
    
    for item in codes_produits_et_quantites:
        code_produit = item["code_produit"]
        quantite = item["quantite"]
        
        # Rechercher le produit dans le stockage
        produit_trouve = None
        for produit in stockage:
            if produit["code_produit"] == code_produit:
                produit_trouve = produit
                break
        
        if produit_trouve:
            article = {
                "nom": produit_trouve["description"],
                "quantite": quantite,
                "prix_ht": produit_trouve["prix_ht_unitaire"]
            }
            articles.append(article)
        else:
            print(f"Attention: Produit avec le code {code_produit} non trouvé dans le stockage")
    
    return articles


def generer_ticket_depuis_stockage(date, nom_client, nom_magasin, pourcentage_tva, codes_produits_et_quantites):
    """Génère un ticket de caisse à partir des produits en stockage"""
    # Convertir les codes produits en articles
    articles = convertir_stockage_vers_articles(codes_produits_et_quantites)
    
    # Calculer la somme totale TTC
    somme_totale = 0
    for article in articles:
        prix_ttc = article["prix_ht"] * (1 + pourcentage_tva / 100)
        somme_totale += article["quantite"] * prix_ttc
    
    # Générer le ticket
    return afficher_ticket_caisse(date, nom_client, nom_magasin, pourcentage_tva, articles, somme_totale)


# =============================================================================
# FONCTIONS DE VALIDATION
# =============================================================================

def valider_nom_magasin(nom_magasin):
    """Valide le nom du magasin"""
    if not nom_magasin or nom_magasin.strip() == "":
        return False, "❌ ERREUR: Le nom du magasin ne peut pas être vide."
    if len(nom_magasin.strip()) < 2:
        return False, "❌ ERREUR: Le nom du magasin doit contenir au moins 2 caractères."
    if len(nom_magasin.strip()) > 50:
        return False, "❌ ERREUR: Le nom du magasin ne peut pas dépasser 50 caractères."
    return True, ""

def valider_nom_client(nom_client):
    """Valide le nom du client/vendeur"""
    if not nom_client or nom_client.strip() == "":
        return False, "❌ ERREUR: Le nom du client/vendeur ne peut pas être vide."
    if len(nom_client.strip()) < 2:
        return False, "❌ ERREUR: Le nom du client/vendeur doit contenir au moins 2 caractères."
    if len(nom_client.strip()) > 30:
        return False, "❌ ERREUR: Le nom du client/vendeur ne peut pas dépasser 30 caractères."
    
    import re
    if not re.match(r"^[a-zA-ZÀ-ÿ\s\-']+$", nom_client.strip()):
        return False, "❌ ERREUR: Le nom du client/vendeur ne peut contenir que des lettres, espaces, tirets et apostrophes."
    return True, ""
    if len(nom_client.strip()) > 30:
        return False, "❌ ERREUR: Le nom du client/vendeur ne peut pas dépasser 30 caractères."
    
    # Importer le module regex pour la validation des caractères
    import re
    # Vérifier que le nom ne contient que des lettres, espaces, tirets et apostrophes
    # Pattern regex: lettres (a-z, A-Z), caractères accentués (À-ÿ), espaces (\s), tirets (-) et apostrophes (')
    if not re.match(r"^[a-zA-ZÀ-ÿ\s\-']+$", nom_client.strip()):
        return False, "❌ ERREUR: Le nom du client/vendeur ne peut contenir que des lettres, espaces, tirets et apostrophes."
    
    # Si toutes les validations passent, retourner True
    return True, ""


def valider_format_commande(commande):
    """
    Valide le format d'une commande individuelle selon le pattern C[numéro]:[quantité].
    Effectue une validation complète du format, des types et des valeurs limites.
    
    Args:
        commande (str): Commande à valider (ex: "C01:10")
    
    Returns:
        tuple: (bool, str, int, int) - (True si valide, message d'erreur, code_produit, quantité)
    """
    # Importer le module regex pour la validation du format
    import re
    
    # Vérifier le format général avec une expression régulière
    # Pattern: C suivi d'un ou plusieurs chiffres, puis :, puis un ou plusieurs chiffres
    if not re.match(r"^C\d+:\d+$", commande.strip()):
        return False, f"❌ ERREUR: Format de commande invalide '{commande}'. Format attendu: C[numéro]:[quantité] (ex: C01:10)", 0, 0
    
    try:
        # Séparer le code produit et la quantité en utilisant ':' comme délimiteur
        if ":" not in commande:
            return False, f"❌ ERREUR: Commande '{commande}' doit contenir ':' pour séparer le code produit et la quantité.", 0, 0
        
        code_part, quantite_str = commande.strip().split(":")
        
        # Valider que le code produit commence bien par 'C'
        if not code_part.startswith("C"):
            return False, f"❌ ERREUR: Le code produit '{code_part}' doit commencer par 'C'.", 0, 0
        
        # Extraire et valider le numéro du produit (enlever le 'C' et convertir en entier)
        try:
            code_produit = int(code_part[1:])  # Enlever le 'C' et convertir
            # Vérifier que le numéro est positif
            if code_produit <= 0:
                return False, f"❌ ERREUR: Le numéro de produit '{code_part[1:]}' doit être un nombre positif.", 0, 0
        except ValueError:
            return False, f"❌ ERREUR: Le numéro de produit '{code_part[1:]}' doit être un nombre entier.", 0, 0
        
        # Valider la quantité
        try:
            quantite = int(quantite_str)
            # Vérifier que la quantité est positive
            if quantite <= 0:
                return False, f"❌ ERREUR: La quantité '{quantite_str}' doit être un nombre positif.", 0, 0
            # Vérifier que la quantité ne dépasse pas la limite maximale
            if quantite > 999:
                return False, f"❌ ERREUR: La quantité '{quantite_str}' ne peut pas dépasser 999.", 0, 0
        except ValueError:
            return False, f"❌ ERREUR: La quantité '{quantite_str}' doit être un nombre entier.", 0, 0
        
        # Si toutes les validations passent, retourner les valeurs extraites
        return True, "", code_produit, quantite
        
    except Exception as e:
        # Capturer toute erreur inattendue lors du traitement
        return False, f"❌ ERREUR: Erreur lors de l'analyse de la commande '{commande}': {str(e)}", 0, 0


def parser_commandes(commandes_str):
    """
    Parse une chaîne de commandes au format "C01:10|C02:2" avec validation complète.
    Effectue une validation exhaustive de chaque commande et vérifie l'existence des produits.
    
    Args:
        commandes_str (str): Chaîne contenant les commandes séparées par |
    
    Returns:
        tuple: (list, list) - (Liste de dictionnaires avec code_produit et quantité, Liste des erreurs)
    """
    # Initialiser les listes de résultats
    codes_et_quantites = []  # Commandes valides
    erreurs = []             # Messages d'erreur
    
    # Vérifier que la chaîne d'entrée n'est pas vide
    if not commandes_str or commandes_str.strip() == "":
        erreurs.append("❌ ERREUR: La chaîne de commandes ne peut pas être vide.")
        return codes_et_quantites, erreurs
    
    # Séparer les commandes individuelles en utilisant '|' comme délimiteur
    commandes = commandes_str.split("|")
    
    # Vérifier qu'il y a au moins une commande après la séparation
    if len(commandes) == 0:
        erreurs.append("❌ ERREUR: Aucune commande trouvée.")
        return codes_et_quantites, erreurs
    
    # Traiter et valider chaque commande individuellement
    for i, commande in enumerate(commandes, 1):  # Commencer la numérotation à 1
        # Ignorer les commandes vides
        if commande.strip() == "":
            erreurs.append(f"❌ ERREUR: Commande #{i} est vide.")
            continue
        
        # Valider le format de la commande en utilisant la fonction de validation
        valide, message_erreur, code_produit, quantite = valider_format_commande(commande)
        
        # Si le format n'est pas valide, ajouter l'erreur et passer à la suivante
        if not valide:
            erreurs.append(f"Commande #{i}: {message_erreur}")
            continue
        
        # Vérifier que le produit existe dans le stockage
        produit_trouve = None
        for produit in stockage:
            if produit["code_produit"] == code_produit:
                produit_trouve = produit
                break  # Sortir de la boucle dès qu'on trouve le produit
        
        # Si le produit n'existe pas dans le stockage
        if not produit_trouve:
            erreurs.append(f"❌ ERREUR: Commande #{i} - Produit avec le code C{code_produit:02d} n'existe pas dans le stockage.")
            continue
        
        # Vérifier qu'il n'y a pas de doublons dans les commandes
        for existing in codes_et_quantites:
            if existing["code_produit"] == code_produit:
                erreurs.append(f"❌ ERREUR: Commande #{i} - Le produit C{code_produit:02d} est déjà dans la commande.")
                break
        else:
            # Si pas de doublon trouvé, ajouter la commande validée à la liste
            codes_et_quantites.append({
                "code_produit": code_produit,  # Code du produit validé
                "quantite": quantite          # Quantité validée
            })
    
    # Retourner les commandes valides et la liste des erreurs
    return codes_et_quantites, erreurs


def initialiser_stockage_par_defaut():
    """
    Initialise le stockage avec une liste de produits par défaut.
    Cette fonction peuple le stockage avec 10 produits couramment utilisés pour les tests.
    
    Liste des produits ajoutés:
        - C01: pack de coca (5.00€)
        - C02: kilo de pdt (1.00€)
        - C03: pack Biscotte (2.00€)
        - C04: Pain complet (1.50€)
        - C05: Fromage de chèvre (4.20€)
        - C06: Salade verte (1.80€)
        - C07: Lait (1.20€)
        - C08: Yaourts (3.50€)
        - C09: Bananes (2.30€)
        - C10: Pommes (2.80€)
    """
    # Vider le stockage existant et réinitialiser le compteur
    stockage_list()
    
    # Ajouter les produits un par un avec leurs prix HT
    stockage_ajouter_produit("pack de coca", 5.0)      # C01
    stockage_ajouter_produit("kilo de pdt", 1.0)       # C02
    stockage_ajouter_produit("pack Biscotte", 2.0)     # C03
    stockage_ajouter_produit("Pain complet", 1.50)     # C04
    stockage_ajouter_produit("Fromage de chèvre", 4.20) # C05
    stockage_ajouter_produit("Salade verte", 1.80)     # C06
    stockage_ajouter_produit("Lait", 1.20)             # C07
    stockage_ajouter_produit("Yaourts", 3.50)          # C08
    stockage_ajouter_produit("Bananes", 2.30)          # C09
    stockage_ajouter_produit("Pommes", 2.80)           # C10


# =============================================================================
# FONCTIONS DE GÉNÉRATION DU TICKET DE CAISSE
# =============================================================================
def afficher_ticket_caisse(date, nom_client, nom_magasin, pourcentage_tva, articles, somme_totale):
    """
    Génère un ticket de caisse formaté similaire à l'exemple fourni et l'enregistre dans un fichier .txt.
    Cette fonction est le cœur du système de génération de tickets, créant un fichier formaté 
    avec tous les détails de la transaction.
    
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
    
    # Génération d'un numéro de ticket aléatoire à 4 chiffres pour identification
    numero_ticket = random.randint(1000, 9999)
    
    # Formatage de la date et heure actuelles pour créer un nom de fichier unique
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")  # Format: AAAAMMJJ_HHMMSS
    nom_fichier = f"ticket_caisse_{timestamp}.txt"
    
    # Initialisation des variables pour les calculs de totaux
    total_ht = 0    # Total hors taxes
    total_tva = 0   # Total de la TVA
    
    # Création de la liste qui contiendra toutes les lignes du ticket
    contenu_ticket = []
    
    # =============================================================================
    # CRÉATION DE L'EN-TÊTE DU TICKET (STYLE ENCADRÉ)
    # =============================================================================
    largeur = 60  # Largeur totale du ticket en caractères
    
    # Ligne supérieure du cadre
    contenu_ticket.append("+" + "-" * (largeur - 2) + "+")
    
    # Nom du magasin centré dans le cadre
    contenu_ticket.append("|" + nom_magasin.center(largeur - 2) + "|")
    
    # Numéro de ticket aligné à gauche
    contenu_ticket.append("|" + f"Ticket numéro : {numero_ticket}".ljust(largeur - 2) + "|")
    
    # Ligne vide pour la séparation
    contenu_ticket.append("|" + " " * (largeur - 2) + "|")
    
    # Date du ticket
    contenu_ticket.append("|" + f"Date : {date}".ljust(largeur - 2) + "|")
    
    # Ligne vide pour la séparation
    contenu_ticket.append("|" + " " * (largeur - 2) + "|")
    
    # Nom du vendeur/client
    contenu_ticket.append("|" + f"Vous avez été servi par : {nom_client}".ljust(largeur - 2) + "|")
    
    # Ligne vide avant le tableau des articles
    contenu_ticket.append("|" + " " * (largeur - 2) + "|")
    
    # =============================================================================
    # CRÉATION DE L'EN-TÊTE DU TABLEAU DES ARTICLES
    # =============================================================================
    contenu_ticket.append("|" + f"{'NB':<3} {'Desc.':<20} {'HT unitaire':<12} {'TVA':<5} {'Total':<10}".ljust(largeur - 2) + "|")
    
    # =============================================================================
    # TRAITEMENT DE CHAQUE ARTICLE
    # =============================================================================
    for i, article in enumerate(articles, 1):  # Numérotation des articles à partir de 1
        # Extraction des données de l'article
        nom = article["nom"]           # Description du produit
        quantite = article["quantite"] # Quantité commandée
        prix_ht = article["prix_ht"]   # Prix hors taxes unitaire
        
        # Calculs financiers pour cet article
        prix_ttc = prix_ht * (1 + pourcentage_tva / 100)  # Prix TTC unitaire
        total_article_ttc = quantite * prix_ttc            # Total TTC pour cet article
        total_article_ht = quantite * prix_ht              # Total HT pour cet article
        
        # Calcul de la TVA pour cet article
        tva_article = total_article_ht * (pourcentage_tva / 100)
        
        # Accumulation des totaux généraux
        total_ht += total_article_ht   # Ajouter au total HT général
        total_tva += tva_article       # Ajouter au total TVA général
        
        # Formatage de la ligne article avec alignement des colonnes
        ligne = f"{quantite:<3} {nom:<20} {prix_ht:.2f}€{'':<6} {pourcentage_tva:g}% {total_article_ttc:.2f}€"
        contenu_ticket.append("|" + ligne.ljust(largeur - 2) + "|")
    
    # =============================================================================
    # AJOUT DES TOTAUX EN BAS DU TICKET
    # =============================================================================
    
    # Ligne vide pour séparer les articles des totaux
    contenu_ticket.append("|" + " " * (largeur - 2) + "|")
    
    # Ligne du total HT
    contenu_ticket.append("|" + f"{'Total HT':<40} {total_ht:.2f}€".ljust(largeur - 2) + "|")
    
    # Ligne du total TVA
    contenu_ticket.append("|" + f"{'Total TVA':<40} {total_tva:.2f}€".ljust(largeur - 2) + "|")
    
    # Ligne du total TTC final
    contenu_ticket.append("|" + f"{'Total':<40} {somme_totale:.2f}€".ljust(largeur - 2) + "|")
    
    # Ligne inférieure du cadre pour fermer le ticket
    contenu_ticket.append("+" + "-" * (largeur - 2) + "+")
    
    # =============================================================================
    # ÉCRITURE DU TICKET DANS UN FICHIER
    # =============================================================================
    
    # Création et écriture du fichier ticket avec encodage UTF-8 pour les caractères spéciaux
    with open(nom_fichier, 'w', encoding='utf-8') as fichier:
        # Écrire chaque ligne du ticket dans le fichier
        for ligne in contenu_ticket:
            fichier.write(ligne + '\n')  # Ajouter un retour à la ligne après chaque ligne
    
    # Confirmer la génération réussie du ticket
    print(f"Ticket de caisse généré avec succès: {nom_fichier}")
    
    # Retourner le nom du fichier créé pour usage ultérieur
    return nom_fichier


# =============================================================================
# PROGRAMME PRINCIPAL - GESTION DES ARGUMENTS DE LIGNE DE COMMANDE
# =============================================================================

if __name__ == "__main__":
    initialiser_stockage_par_defaut()

    if len(sys.argv) == 4:
        nom_magasin = sys.argv[1]
        nom_client = sys.argv[2]
        commandes_str = sys.argv[3]

        valide_magasin, erreur_magasin = valider_nom_magasin(nom_magasin)
        if not valide_magasin:
            print(erreur_magasin)
            sys.exit(1)

        valide_client, erreur_client = valider_nom_client(nom_client)
        if not valide_client:
            print(erreur_client)
            sys.exit(1)

        codes_et_quantites, erreurs_commandes = parser_commandes(commandes_str)
        if erreurs_commandes:
            print("❌ ERREURS DÉTECTÉES DANS LES COMMANDES:")
            for erreur in erreurs_commandes:
                print(f"   {erreur}")
            sys.exit(1)

        if not codes_et_quantites:
            print("❌ ERREUR: Aucune commande valide trouvée.")
            sys.exit(1)

        date_aujourd_hui = datetime.now().strftime("%d/%m/%Y")
        generer_ticket_depuis_stockage(
            date=date_aujourd_hui,
            nom_client=nom_client,
            nom_magasin=nom_magasin,
            pourcentage_tva=10.0,
            codes_produits_et_quantites=codes_et_quantites
        )

    else:
        print("❌ ERREUR: Nombre d'arguments incorrect!")
        print("Usage: python3 main.py \"Nom_Magasin\" \"Nom_Client\" \"Commandes\"")
        print("Exemple: python3 main.py \"But Market\" \"Lisa\" \"C01:10|C02:2\"")
        afficher_stockage()
    
