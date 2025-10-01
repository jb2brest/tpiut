#Projet Python - ticket de caisse Gestion de Projet 

# MURY Gurvan et SALOU Elian 3A1 R&T

## Description

# importation des modules nécessaires
import os
import json
import sys

# Variables globales
date = "01/10/2025"
TVA = 0.10

# Fonction pour charger la base de données
def load_database():
    try:
        with open('bdd.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Erreur : fichier bdd.json non trouvé")
        return None
    except json.JSONDecodeError:
        print("Erreur : fichier bdd.json corrompu")
        return None

# Fonction pour obtenir un article par son code
def get_article(code):
    db = load_database()
    if db and code in db['articles']:
        return db['articles'][code]
    return None

# Fonction pour afficher tous les articles disponibles
def afficher_articles():
    db = load_database()
    if db:
        print("\n--- ARTICLES DISPONIBLES ---")
        for code, article in db['articles'].items():
            print(f"{code}: {article['description']} - {article['prix_unitaire']}€")
        print("-----------------------------")

# Fonction pour obtenir le prochain numéro de ticket
def get_next_ticket_number():
    ticket_file = "num_ticket.txt"
    
    # Lire le dernier numéro ou initialiser à 0
    if os.path.exists(ticket_file):
        with open(ticket_file, 'r') as f:
            try:
                current_number = int(f.read().strip())
            except ValueError:
                current_number = 0
    else:
        current_number = 0
    
    # Incrémenter
    new_number = current_number + 1
    
    # Sauvegarder le nouveau numéro
    with open(ticket_file, 'w') as f:
        f.write(str(new_number))
    
    return new_number

# Fonction pour parser les articles depuis les arguments
def parser_articles_args(articles_string):
    panier = []
    erreurs = []
    articles_list = articles_string.split("|")
    
    for article_info in articles_list:
        try:
            if ":" not in article_info:
                erreurs.append(f"Format invalide pour '{article_info}'. Utilisez 'CODE:QUANTITE'")
                continue
                
            code, quantite_str = article_info.split(":", 1)
            code = code.upper().strip()
            
            try:
                quantite = int(quantite_str.strip())
            except ValueError:
                erreurs.append(f"Quantité invalide '{quantite_str}' pour l'article {code}. Utilisez un nombre entier.")
                continue
            
            if quantite <= 0:
                erreurs.append(f"Quantité invalide '{quantite}' pour l'article {code}. La quantité doit être positive.")
                continue
                
            article = get_article(code)
            if not article:
                erreurs.append(f"Article '{code}' non trouvé dans la base de données.")
                continue
                
            panier.append({
                'code': code,
                'description': article['description'],
                'prix_unitaire': article['prix_unitaire'],
                'quantite': quantite,
                'total': article['prix_unitaire'] * quantite
            })
            
        except ValueError as e:
            erreurs.append(f"Erreur de format pour '{article_info}'. Vérifiez le format CODE:QUANTITE")
    
    return panier, erreurs

# Fonction pour sauvegarder la base de données
def save_database(db):
    try:
        with open('bdd.json', 'w', encoding='utf-8') as f:
            json.dump(db, f, ensure_ascii=False, indent=2)
        return True
    except Exception as e:
        print(f"Erreur lors de la sauvegarde : {e}")
        return False

# Fonction pour ajouter un article
def ajouter_article(code, description, prix):
    db = load_database()
    if not db:
        print("ERREUR : Impossible de charger la base de données")
        return False
    
    code = code.upper()
    
    if code in db['articles']:
        print(f"ERREUR : L'article '{code}' existe déjà")
        return False
    
    try:
        prix = float(prix)
        if prix <= 0:
            print("ERREUR : Le prix doit être positif")
            return False
    except ValueError:
        print("ERREUR : Le prix doit être un nombre valide")
        return False
    
    db['articles'][code] = {
        'description': description,
        'prix_unitaire': prix
    }
    
    if save_database(db):
        print(f"Article '{code}' ajouté avec succès :")
        print(f"   {description} - {prix}€")
        return True
    return False

# Fonction pour supprimer un article
def supprimer_article(code):
    db = load_database()
    if not db:
        print(" Impossible de charger la base de données")
        return False
    
    code = code.upper()
    
    if code not in db['articles']:
        print(f"ERREUR : L'article '{code}' n'existe pas")
        return False
    
    article = db['articles'][code]
    del db['articles'][code]
    
    if save_database(db):
        print(f"Article '{code}' supprimé avec succès :")
        print(f"   {article['description']} - {article['prix_unitaire']}€")
        return True
    return False

# Fonction pour modifier un article
def modifier_article(code, description=None, prix=None):
    db = load_database()
    if not db:
        print("ERREUR : Impossible de charger la base de données")
        return False
    
    code = code.upper()
    
    if code not in db['articles']:
        print(f"ERREUR : L'article '{code}' n'existe pas")
        return False
    
    if prix is not None:
        try:
            prix = float(prix)
            if prix <= 0:
                print("ERREUR : Le prix doit être positif")
                return False
        except ValueError:
            print("ERREUR : Le prix doit être un nombre valide")
            return False
    
    article = db['articles'][code]
    ancien_article = article.copy()
    
    if description is not None:
        article['description'] = description
    if prix is not None:
        article['prix_unitaire'] = prix
    
    if save_database(db):
        print(f"Article '{code}' modifié avec succès :")
        print(f"   Avant : {ancien_article['description']} - {ancien_article['prix_unitaire']}€")
        print(f"   Après : {article['description']} - {article['prix_unitaire']}€")
        return True
    return False

# Fonction pour afficher l'aide générale
def afficher_aide_generale():
    print("SYSTÈME DE GESTION - BUT MARKET")
    print("=" * 50)
    print("\nMODES DISPONIBLES :")
    print("\n1. MODE CAISSE (génération de ticket) :")
    print("   python main.py \"NOM_MAGASIN\" \"NOM_SERVEUR\" \"ARTICLES\"")
    print("   Exemple : python main.py \"But Market\" \"Lisa\" \"C01:10|C02:2\"")
    
    print("\n2. MODE AJOUT (ajouter un article) :")
    print("   python main.py ajout \"CODE\" \"DESCRIPTION\" \"PRIX\"")
    print("   Exemple : python main.py ajout \"C06\" \"Eau minérale\" \"1.5\"")
    
    print("\n3. MODE SUPPRESSION (supprimer un article) :")
    print("   python main.py suppression \"CODE\"")
    print("   Exemple : python main.py suppression \"C06\"")
    
    print("\n4. MODE MODIFICATION (modifier un article) :")
    print("   python main.py modification \"CODE\" \"NOUVELLE_DESCRIPTION\" \"NOUVEAU_PRIX\"")
    print("   Exemple : python main.py modification \"C01\" \"Coca-Cola 2L\" \"6\"")
    
    print("\nArticles disponibles :")
    afficher_articles()

# Fonction pour afficher l'aide pour le mode caisse
def afficher_aide():
    print("MODE CAISSE - Génération de ticket")
    print("Usage : python main.py \"NOM_MAGASIN\" \"NOM_SERVEUR\" \"ARTICLES\"")
    print("Exemple : python main.py \"But Market\" \"Lisa\" \"C01:10|C02:2\"")
    print("\nFormat des articles : CODE:QUANTITE|CODE:QUANTITE")
    print("Articles disponibles :")
    afficher_articles()

# Fonction pour afficher le ticket final
def afficher_ticket_final(panier, serveur, ticket_num, date, nom_magasin):
    print("\n" + "==================================================")
    print(f"{nom_magasin}")
    print(f"Ticket numéro : {ticket_num}")
    print("")
    print(f"Date : {date}")
    print("")
    print(f"Vous avez été servi par : {serveur}")
    print("")
    
    # En-tête du tableau
    print(f"{'NB':<3} {'Desc.':<15} {'HT unitaire':<11} {'TVA':<4} {'Total':<6}")
    
    total_ht = 0
    for item in panier:
        ht_unitaire = f"{item['prix_unitaire']:.0f}€"
        tva_percent = f"{int(TVA*100)}%"
        total_item = f"{item['total']:.1f}€"
        
        print(f"{item['quantite']:<3} {item['description']:<15} {ht_unitaire:<11} {tva_percent:<4} {total_item:<6}")
        total_ht += item['total']
    
    print("")
    print(f"{'':<31} Total HT   {total_ht:.0f}€")
    
    tva_montant = total_ht * TVA
    print(f"{'':<31} Total TVA  {tva_montant:.1f}€")
    
    total_ttc = total_ht + tva_montant
    print(f"{'':<31} Total      {total_ttc:.1f}€")
    
    print("==================================================")

# Programme principal
if __name__ == "__main__":
    # Vérifier qu'il y a au moins un argument
    if len(sys.argv) < 2:
        print("ERREUR : Aucun argument fourni")
        afficher_aide_generale()
        sys.exit(1)
    
    # Récupérer le premier argument (mode ou nom du magasin)
    premier_arg = sys.argv[1].lower().strip()
    
    # MODE AJOUT
    if premier_arg == "ajout":
        if len(sys.argv) != 5:
            print("ERREUR : Arguments incorrects pour le mode ajout")
            print("Usage : python main.py ajout \"CODE\" \"DESCRIPTION\" \"PRIX\"")
            print("Exemple : python main.py ajout \"C06\" \"Eau minérale\" \"1.5\"")
            sys.exit(1)
        
        code = sys.argv[2].strip()
        description = sys.argv[3].strip()
        prix = sys.argv[4].strip()
        
        if not code or not description or not prix:
            print("ERREUR : Tous les arguments doivent être renseignés")
            sys.exit(1)
        
        ajouter_article(code, description, prix)
    
    # MODE SUPPRESSION
    elif premier_arg == "suppression":
        if len(sys.argv) != 3:
            print("ERREUR : Arguments incorrects pour le mode suppression")
            print("Usage : python main.py suppression \"CODE\"")
            print("Exemple : python main.py suppression \"C06\"")
            sys.exit(1)
        
        code = sys.argv[2].strip()
        
        if not code:
            print("ERREUR : Le code article doit être renseigné")
            sys.exit(1)
        
        supprimer_article(code)
    
    # MODE MODIFICATION
    elif premier_arg == "modification":
        if len(sys.argv) != 5:
            print("ERREUR : Arguments incorrects pour le mode modification")
            print("Usage : python main.py modification \"CODE\" \"NOUVELLE_DESCRIPTION\" \"NOUVEAU_PRIX\"")
            print("Exemple : python main.py modification \"C01\" \"Coca-Cola 2L\" \"6\"")
            sys.exit(1)
        
        code = sys.argv[2].strip()
        description = sys.argv[3].strip()
        prix = sys.argv[4].strip()
        
        if not code or not description or not prix:
            print("ERREUR : Tous les arguments doivent être renseignés")
            sys.exit(1)
        
        modifier_article(code, description, prix)
    
    # MODE CAISSE (mode par défaut)
    else:
        # Vérifier les arguments de ligne de commande pour le mode caisse
        if len(sys.argv) != 4:
            print("ERREUR : Arguments incorrects pour le mode caisse")
            print(f"Vous avez fourni {len(sys.argv) - 1} argument(s), il en faut 3.\n")
            afficher_aide()
            sys.exit(1)

        # Récupérer les arguments
        nom_magasin = sys.argv[1].strip()
        serveur = sys.argv[2].strip()
        articles_string = sys.argv[3].strip()

        # Vérifier que les arguments ne sont pas vides
        if not nom_magasin:
            print("ERREUR : Le nom du magasin ne peut pas être vide.\n")
            afficher_aide()
            sys.exit(1)
        
        if not serveur:
            print("ERREUR : Le nom du serveur ne peut pas être vide.\n")
            afficher_aide()
            sys.exit(1)
        
        if not articles_string:
            print("ERREUR : La liste des articles ne peut pas être vide.\n")
            afficher_aide()
            sys.exit(1)

        print(f"Bienvenue dans notre supermarché {nom_magasin} !")

        # Parser les articles depuis les arguments
        panier, erreurs = parser_articles_args(articles_string)

        # Vérifier s'il y a des erreurs
        if erreurs:
            print("\nERREURS DÉTECTÉES :")
            for i, erreur in enumerate(erreurs, 1):
                print(f"  {i}. {erreur}")
            
            print("\nVeuillez corriger les erreurs et relancer le programme.")
            afficher_aide()
            sys.exit(1)

        # Vérifier qu'il y a au moins un article valide
        if not panier:
            print("\nERREUR : Aucun article valide trouvé.")
            print("Veuillez vérifier vos codes d'articles et relancer le programme.")
            afficher_aide()
            sys.exit(1)

        # Générer le numéro de ticket seulement si tout est correct
        Ticket_num = get_next_ticket_number()
        
        # Afficher le ticket final
        afficher_ticket_final(panier, serveur, Ticket_num, date, nom_magasin)