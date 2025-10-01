import sys
import json
from datetime import datetime
import os

ITEMS_FILE = "items.json"

def charger_items():
    """
    Charge la liste des produits depuis le fichier JSON.
    Si le fichier n'existe pas, crée une liste par défaut et la sauvegarde.
    Retourne le dictionnaire des produits.
    """
    if not os.path.exists(ITEMS_FILE):
        # Création d'une liste de produits par défaut si le fichier n'existe pas
        items = {
            "C01": {"desc": "pack de coca", "prix": 5},
            "C02": {"desc": "kilo de pdt", "prix": 1},
            "C03": {"desc": "pack Biscotte", "prix": 2},
            "C04": {"desc": "Café soluble", "prix": 3},
            "C05": {"desc": "Crakers", "prix": 4},
        }
        with open(ITEMS_FILE, "w", encoding="utf-8") as f:
            json.dump(items, f, ensure_ascii=False, indent=4)
        return items
    # Lecture du fichier JSON existant
    with open(ITEMS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def sauvegarder_items(items):
    """
    Sauvegarde la liste des produits dans le fichier JSON.
    """
    with open(ITEMS_FILE, "w", encoding="utf-8") as f:
        json.dump(items, f, ensure_ascii=False, indent=4)

TVA = 0.10  # Taux de TVA (10%)
TICKET_NUMBER = 2200  # Numéro de ticket (fixe pour l'exemple, à adapter pour incrémentation)

def ajouter_produit(items, code, desc, prix):
    """
    Ajoute un produit à la liste ITEMS et sauvegarde dans le JSON.
    Vérifie que le code n'existe pas déjà et que le prix est valide.
    """
    if code in items:
        print("Ce code existe déjà.")
        return
    try:
        prix = float(prix)
    except ValueError:
        print("Prix invalide.")
        return
    items[code] = {"desc": desc, "prix": prix}
    sauvegarder_items(items)
    print(f"Produit {code} ajouté.")

def enlever_produit(items, code):
    """
    Enlève un produit de la liste ITEMS à l'aide de son code et sauvegarde.
    Affiche un message si le code n'existe pas.
    """
    if code in items:
        del items[code]
        sauvegarder_items(items)
        print(f"Produit {code} supprimé.")
    else:
        print("Code produit introuvable.")

def afficher_liste_produits(items):
    """
    Affiche la liste des produits disponibles dans un format lisible.
    """
    print("\nListe des produits :")
    print("Code   Description         Prix HT")
    for code, info in items.items():
        print(f"{code:<6} {info['desc']:<18} {info['prix']}€")
    print()

def modifier_produit(items, code, desc=None, prix=None):
    """
    Modifie la description ou le prix d'un produit existant dans ITEMS et sauvegarde.
    Si le code n'existe pas, affiche un message d'erreur.
    """
    if code not in items:
        print("Code produit introuvable.")
        return
    if desc:
        items[code]['desc'] = desc
    if prix:
        try:
            items[code]['prix'] = float(prix)
        except ValueError:
            print("Prix invalide, modification annulée.")
            return
    sauvegarder_items(items)
    print(f"Produit {code} modifié.")

def ticket(magasin, caissier, panier, items):
    """
    Affiche le ticket de caisse formaté et esthétique.
    Affiche chaque ligne d'article, les totaux, et les informations du ticket.
    """
    print("=" * 40)
    print(f"{magasin:^40}")  # Nom du magasin centré
    print(f"Ticket numéro : {TICKET_NUMBER}")
    print(f"Date : {datetime.now().strftime('%d/%m/%Y')}")
    print("-" * 40)
    print(f"Servi par : {caissier}")
    print("-" * 40)
    print(f"{'NB':<3} {'Description':<16} {'PU HT':>6} {'TVA':>5} {'Total':>7}")
    print("-" * 40)
    total_ht = 0
    total_tva = 0
    total_ttc = 0
    # Parcours du panier pour afficher chaque ligne d'article
    for code, qte in panier:
        item = items.get(code)
        if not item:
            continue
        ht = item["prix"]
        tva = ht * TVA
        total = (ht + tva) * qte
        print(f"{qte:<3} {item['desc']:<16} {ht:>6.2f}€ {TVA*100:>4.0f}% {total:>7.2f}€")
        total_ht += ht * qte
        total_tva += tva * qte
        total_ttc += total
    print("-" * 40)
    print(f"{'Total HT':<25}{total_ht:>7.2f}€")
    print(f"{'Total TVA':<25}{total_tva:>7.2f}€")
    print(f"{'Total TTC':<25}{total_ttc:>7.2f}€")
    print("=" * 40)

if __name__ == "__main__":
    items = charger_items()
    # Si aucun argument n'est fourni, affiche l'aide et quitte
    if len(sys.argv) < 2:
        print("Usage :")
        print('  python main.py "But Maket" "Lisa" "C01:10|C02:2"')
        print('  python main.py Ajout C06 "Nouveau produit" 7.5')
        print('  python main.py Suppression C06')
        print('  python main.py Modification C06 "Nouveau nom" 8.0')
        print('  python main.py Liste')
        sys.exit(1)

    action = sys.argv[1]

    # Ajout d'un produit : python main.py Ajout C06 "desc" 7.5
    if action.lower() == "ajout" and len(sys.argv) == 5:
        _, _, code, desc, prix = sys.argv
        ajouter_produit(items, code, desc, prix)
    # Suppression d'un produit : python main.py Suppression C06
    elif action.lower() == "suppression" and len(sys.argv) == 3:
        _, _, code = sys.argv
        enlever_produit(items, code)
    # Modification d'un produit : python main.py Modification C06 "desc" 8.0
    elif action.lower() == "modification" and len(sys.argv) >= 3:
        code = sys.argv[2]
        desc = sys.argv[3] if len(sys.argv) > 3 else None
        prix = sys.argv[4] if len(sys.argv) > 4 else None
        modifier_produit(items, code, desc, prix)
    # Affichage de la liste : python main.py Liste
    elif action.lower() == "liste":
        afficher_liste_produits(items)
    # Génération d'un ticket : python main.py "But Maket" "Lisa" "C01:10|C02:2"
    elif len(sys.argv) >= 4:
        magasin = sys.argv[1]
        caissier = sys.argv[2]
        achats = sys.argv[3].split('|')
        panier = []      # Liste des articles valides à mettre sur le ticket
        erreurs = []     # Liste des erreurs rencontrées lors du parsing des articles
        for achat in achats:
            try:
                code, qte = achat.split(':')
                # Vérifie si le code produit existe
                if code not in items:
                    erreurs.append(f"Produit inconnu : {code}")
                    continue
                # Vérifie que la quantité est un entier positif
                qte = int(qte)
                if qte <= 0:
                    erreurs.append(f"Quantité invalide pour {code} : {qte}")
                    continue
                panier.append((code, qte))
            except ValueError:
                # Erreur de format (ex: oubli des deux points ou quantité non entière)
                erreurs.append(f"Format invalide pour l'article : '{achat}' (attendu CODE:QTE)")
        # Si aucun produit valide, on affiche les erreurs et on quitte
        if not panier:
            print("Aucun produit valide dans la commande.")
            if erreurs:
                print("Erreurs rencontrées :")
                for err in erreurs:
                    print(" -", err)
            sys.exit(1)
        # Si certains articles sont ignorés, on affiche un avertissement
        if erreurs:
            print("Attention, certains articles ont été ignorés :")
            for err in erreurs:
                print(" -", err)
        # Affichage du ticket avec les articles valides
        ticket(magasin, caissier, panier, items)
    # Cas d'une commande invalide
    else:
        print("Commande invalide. Voir l'usage ci-dessous :")
        print('  python main.py "But Maket" "Lisa" "C01:10|C02:2"')
        print('  python main.py Ajout C06 "Nouveau produit" 7.5')
        print('  python main.py Suppression C06')
        print('  python main.py Modification C06 "Nouveau nom" 8.0')
        print('  python main.py Liste')