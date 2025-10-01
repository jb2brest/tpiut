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

def stockage_ajouter_produit(description: str, prix_ht_unitaire: float, tva_percent: float = 10.0, poids_volume: str = "", origine: str = ""):
    """Ajoute un produit dans le stockage avec TVA spécifique"""
    global stockage, code_counter
    product = {
        "code_produit": code_counter,
        "description": description,
        "prix_ht_unitaire": prix_ht_unitaire,
        "tva_percent": tva_percent,
        "poids_volume": poids_volume,
        "origine": origine
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
            print(f"C{produit['code_produit']:02d}: {produit['description']} - {produit['prix_ht_unitaire']:.2f}€ HT - TVA {produit['tva_percent']:.0f}% - {produit['poids_volume']} - {produit['origine']}")


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
                "prix_ht": produit_trouve["prix_ht_unitaire"],
                "tva_percent": produit_trouve["tva_percent"],
                "poids_volume": produit_trouve.get("poids_volume", ""),
                "origine": produit_trouve.get("origine", "")
            }
            articles.append(article)
        else:
            print(f"Attention: Produit avec le code {code_produit} non trouvé dans le stockage")
    
    return articles


def generer_ticket_depuis_stockage(date, nom_client, nom_magasin, codes_produits_et_quantites):
    """Génère un ticket de caisse à partir des produits en stockage avec TVA par produit"""
    # Convertir les codes produits en articles
    articles = convertir_stockage_vers_articles(codes_produits_et_quantites)
    
    # Calculer la somme totale TTC en tenant compte du taux de TVA de chaque produit
    somme_totale = 0
    for article in articles:
        tva_produit = article.get("tva_percent", 10.0)  # TVA par défaut 10% si non spécifiée
        prix_ttc = article["prix_ht"] * (1 + tva_produit / 100)
        somme_totale += article["quantite"] * prix_ttc
    
    # Générer le ticket (la TVA sera calculée individuellement pour chaque produit)
    return afficher_ticket_caisse(date, nom_client, nom_magasin, articles, somme_totale)


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
    Initialise le stockage avec la liste de produits selon les exigences.
    Produits de C01 à C07 avec leurs taux de TVA spécifiques.
    """
    # Vider le stockage existant et réinitialiser le compteur
    stockage_list()
    
    # Ajouter les produits selon le tableau des exigences
    stockage_ajouter_produit("pack de coca", 5.0, 20.0, "2kg", "Lituanie")        # C01
    stockage_ajouter_produit("kilo de pdt", 1.0, 10.0, "1kg", "Espagne")          # C02
    stockage_ajouter_produit("pack Biscotte", 2.0, 10.0, "950g", "France")        # C03
    stockage_ajouter_produit("Café soluble", 3.0, 10.0, "250g", "Roumanie")       # C04
    stockage_ajouter_produit("Crackers", 4.0, 20.0, "125g", "Angleterre")         # C05
    stockage_ajouter_produit("Eau", 6.0, 10.0, "1,5L", "Suisse")                 # C06
    stockage_ajouter_produit("Pain", 1.0, 10.0, "250g", "France")                 # C07


# =============================================================================
# FONCTIONS DE GÉNÉRATION DU TICKET DE CAISSE
# =============================================================================
def afficher_ticket_caisse(date, nom_client, nom_magasin, articles, somme_totale):
    """
    Génère un ticket de caisse formaté selon le nouveau format avec poids/volume et TVA par produit.
    
    Args:
        date (str): Date du ticket (format: "DD/MM/YYYY")
        nom_client (str): Nom du client/vendeur
        nom_magasin (str): Nom du magasin
        articles (list): Liste des articles avec TVA individuelle
        somme_totale (float): Somme totale TTC du ticket
    
    Returns:
        str: Le nom du fichier généré
    """
    
    # Génération d'un numéro de ticket aléatoire à 4 chiffres
    numero_ticket = random.randint(1000, 9999)
    
    # Formatage de la date et heure actuelles pour créer un nom de fichier unique
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    nom_fichier = f"ticket_caisse_{timestamp}.txt"
    
    # Initialisation des variables pour les calculs de totaux
    total_ht = 0
    total_tva = 0
    
    # Création de la liste qui contiendra toutes les lignes du ticket
    contenu_ticket = []
    
    # =============================================================================
    # CRÉATION DE L'EN-TÊTE DU TICKET
    # =============================================================================
    
    # En-tête simple comme dans l'exemple
    contenu_ticket.append(nom_magasin)
    contenu_ticket.append(f"Ticket numéro : {numero_ticket}")
    contenu_ticket.append("")
    contenu_ticket.append(f"Date : {date}")
    contenu_ticket.append("")
    contenu_ticket.append(f"Vous avez été servi par : {nom_client}")
    contenu_ticket.append("")
    
    # En-tête du tableau selon le nouveau format
    contenu_ticket.append(f"{'NB':<3} {'Desc.':<15} {'Poids/volume unitaire':<20} {'Poids/volume total':<18} {'HT unitaire':<12} {'TVA':<5} {'Total':<8}")
    
    # =============================================================================
    # TRAITEMENT DE CHAQUE ARTICLE
    # =============================================================================
    for article in articles:
        nom = article["nom"]
        quantite = article["quantite"]
        prix_ht = article["prix_ht"]
        tva_percent = article["tva_percent"]
        poids_volume = article.get("poids_volume", "")
        
        # Calculs financiers pour cet article
        prix_ttc_unitaire = prix_ht * (1 + tva_percent / 100)
        total_article_ht = quantite * prix_ht
        tva_article = total_article_ht * (tva_percent / 100)
        total_article_ttc = total_article_ht + tva_article
        
        # Calcul du poids/volume total (si numérique)
        try:
            if poids_volume.replace('kg', '').replace('g', '').replace('L', '').replace(',', '.').replace(' ', ''):
                poids_num = float(poids_volume.replace('kg', '').replace('g', '').replace('L', '').replace(',', '.'))
                if 'kg' in poids_volume:
                    poids_total = f"{poids_num * quantite}kg"
                elif 'g' in poids_volume:
                    if poids_num * quantite >= 1000:
                        poids_total = f"{(poids_num * quantite)/1000}kg"
                    else:
                        poids_total = f"{poids_num * quantite}g"
                elif 'L' in poids_volume:
                    poids_total = f"{poids_num * quantite}L"
                else:
                    poids_total = f"{poids_num * quantite}"
            else:
                poids_total = f"{quantite}x{poids_volume}"
        except:
            poids_total = f"{quantite}x{poids_volume}"
        
        # Accumulation des totaux généraux
        total_ht += total_article_ht
        total_tva += tva_article
        
        # Formatage de la ligne selon le nouveau format
        ligne = f"{quantite:<3} {nom:<15} {poids_volume:<20} {poids_total:<18} {prix_ht:<12.0f} {tva_percent:<5.0f}% {total_article_ttc:<8.2f}"
        contenu_ticket.append(ligne)
    
    # =============================================================================
    # AJOUT DES TOTAUX
    # =============================================================================
    contenu_ticket.append("")
    contenu_ticket.append(f"{'Total HT':<60} {total_ht:.0f}€")
    contenu_ticket.append(f"{'Total TVA':<60} {total_tva:.1f}€")
    contenu_ticket.append(f"{'Total':<60} {somme_totale:.1f}€")
    
    # =============================================================================
    # ÉCRITURE DU TICKET DANS UN FICHIER
    # =============================================================================
    with open(nom_fichier, 'w', encoding='utf-8') as fichier:
        for ligne in contenu_ticket:
            fichier.write(ligne + '\n')
            print(ligne)
    
    print(f"\nTicket de caisse généré avec succès: {nom_fichier}")
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
            codes_produits_et_quantites=codes_et_quantites
        )

    else:
        print("❌ ERREUR: Nombre d'arguments incorrect!")
        print("Usage: python3 main.py \"Nom_Magasin\" \"Nom_Client\" \"Commandes\"")
        print("Exemple: python3 main.py \"But Market\" \"Lisa\" \"C01:10|C02:2\"")
        afficher_stockage()
    
