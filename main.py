import sys
import json
from datetime import datetime
import os

ITEMS_FILE = "items.json"
TICKET_FILE = "ticket_number.json"

def charger_items():
    """
    Charge la liste des produits depuis le fichier JSON.
    Si le fichier n'existe pas, crée une liste par défaut et la sauvegarde.
    Retourne le dictionnaire des produits.
    """
    if not os.path.exists(ITEMS_FILE):
        # Création d'une liste de produits par défaut si le fichier n'existe pas
        items = {
            "C01": {"desc": "pack de coca", "poids_unitaire": "2kg", "prix": 5, "tva": 20, "origine": "Lituanie"},
            "C02": {"desc": "kilo de pdt", "poids_unitaire": "1kg", "prix": 1, "tva": 10, "origine": "Espagne"},
            "C03": {"desc": "pack Biscotte", "poids_unitaire": "950g", "prix": 2, "tva": 10, "origine": "France"},
            "C04": {"desc": "Café soluble", "poids_unitaire": "250g", "prix": 3, "tva": 10, "origine": "Roumanie"},
            "C05": {"desc": "Crakers", "poids_unitaire": "125g", "prix": 4, "tva": 20, "origine": "Angleterre"},
            "C06": {"desc": "Eau", "poids_unitaire": "1.5L", "prix": 6, "tva": 10, "origine": "Suisse"},
            "C07": {"desc": "Pain", "poids_unitaire": "250g", "prix": 1, "tva": 10, "origine": "France"}
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

def charger_ticket_number():
    """
    Charge le numéro de ticket depuis un fichier JSON séparé.
    Si le fichier n'existe pas, initialise à 2200.
    """
    if not os.path.exists(TICKET_FILE):
        with open(TICKET_FILE, "w", encoding="utf-8") as f:
            json.dump({"ticket_number": 2200}, f)
        return 2200
    with open(TICKET_FILE, "r", encoding="utf-8") as f:
        return json.load(f)["ticket_number"]

def sauvegarder_ticket_number(ticket_number):
    """
    Sauvegarde le numéro de ticket dans le fichier JSON.
    """
    with open(TICKET_FILE, "w", encoding="utf-8") as f:
        json.dump({"ticket_number": ticket_number}, f)

def ajouter_produit(items, code, desc, poids_unitaire, prix, tva, origine):
    """
    Ajoute un produit à la liste ITEMS et sauvegarde dans le JSON.
    Vérifie que le code n'existe pas déjà et que le prix est valide.
    """
    if code in items:
        print("Ce code existe déjà.")
        return
    try:
        prix = float(prix)
        tva = int(tva)
    except ValueError:
        print("Prix ou TVA invalide.")
        return
    items[code] = {
        "desc": desc,
        "poids_unitaire": poids_unitaire,
        "prix": prix,
        "tva": tva,
        "origine": origine
    }
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
    Affiche la liste des produits disponibles dans un format tableau avancé.
    """
    print("\nCode  Description        Poids/vol.  Prix HT  TVA   Origine")
    print("---------------------------------------------------------------")
    for code, info in items.items():
        print(f"{code:<5} {info['desc']:<18} {info['poids_unitaire']:<10} {info['prix']:<7} {str(info['tva'])+' %':<5} {info['origine']}")
    print()

def modifier_produit(items, code, desc=None, poids_unitaire=None, prix=None, tva=None, origine=None):
    """
    Modifie les champs d'un produit existant dans ITEMS et sauvegarde.
    Si le code n'existe pas, affiche un message d'erreur.
    """
    if code not in items:
        print("Code produit introuvable.")
        return
    if desc:
        items[code]['desc'] = desc
    if poids_unitaire:
        items[code]['poids_unitaire'] = poids_unitaire
    if prix:
        try:
            items[code]['prix'] = float(prix)
        except ValueError:
            print("Prix invalide, modification annulée.")
            return
    if tva:
        try:
            items[code]['tva'] = int(tva)
        except ValueError:
            print("TVA invalide, modification annulée.")
            return
    if origine:
        items[code]['origine'] = origine
    sauvegarder_items(items)
    print(f"Produit {code} modifié.")

def ticket(magasin, caissier, panier, items, ticket_number):
    """
    Affiche le ticket de caisse formaté comme sur les captures d'écran.
    """
    print(f"{magasin}")
    print(f"Ticket numéro : {ticket_number}")
    print(f"Date : {datetime.now().strftime('%d/%m/%Y')}")
    print(f"\nVous avez été servi par : {caissier}\n")
    print("NB  Desc.            Pds/vol. uni.  Pds/vol.   HT uni.   TVA    Total")
    print("-------------------------------------------------------------------------------------")
    total_ht = 0
    total_tva = 0
    total_ttc = 0
    for code, qte in panier:
        item = items.get(code)
        if not item:
            continue
        ht = item["prix"]
        tva = item["tva"]
        poids_uni = item["poids_unitaire"]
        # Calcul du poids total (simple concat si unité, sinon à adapter)
        try:
            if poids_uni.endswith("kg"):
                poids_total = f"{float(poids_uni[:-2]) * qte}kg"
            elif poids_uni.endswith("g"):
                poids_total = f"{float(poids_uni[:-1]) * qte}g"
            elif poids_uni.endswith("L"):
                poids_total = f"{float(poids_uni[:-1]) * qte}L"
            else:
                poids_total = f"{poids_uni}*{qte}"
        except:
            poids_total = f"{poids_uni}*{qte}"
        total_ligne_ht = ht * qte
        tva_ligne = total_ligne_ht * tva / 100
        total_ligne_ttc = total_ligne_ht + tva_ligne
        print(f"{qte:<3} {item['desc']:<16} {poids_uni:<13} {poids_total:<13} {ht:<7}€ {str(tva)+'%':<5} {total_ligne_ttc:.1f}€")
        total_ht += total_ligne_ht
        total_tva += tva_ligne
        total_ttc += total_ligne_ttc
    print("-------------------------------------------------------------------------------------")
    print(f"{'Total HT':<60}{total_ht:.1f}€")
    print(f"{'Total TVA':<60}{total_tva:.1f}€")
    print(f"{'Total TTC':<60}{total_ttc:.1f}€")

if __name__ == "__main__":
    # Génère les fichiers JSON si absents AVANT toute commande
    if not os.path.exists(ITEMS_FILE):
        charger_items()
    if not os.path.exists(TICKET_FILE):
        charger_ticket_number()

    items = charger_items()
    # Correction automatique des anciens produits
    for code, prod in items.items():
        if "tva" not in prod:
            prod["tva"] = 10
        if "origine" not in prod:
            prod["origine"] = "France"
        if "poids_unitaire" not in prod:
            prod["poids_unitaire"] = "1kg"
    sauvegarder_items(items)
    ticket_number = charger_ticket_number()
    # Si aucun argument n'est fourni, affiche l'aide et quitte
    if len(sys.argv) < 2:
        print("Usage :")
        print('  python mainv2.py "But Maket" "Lisa" "C01:10|C02:2"')
        print('  python mainv2.py Ajout C08 "Produit" 500g 2.5 10 Espagne')
        print('  python mainv2.py Suppression C06')
        print('  python mainv2.py Modification C06 "desc" 1.5L 6 10 Suisse')
        print('  python mainv2.py Liste')
        sys.exit(1)

    action = sys.argv[1]

    # Ajout d'un produit : python mainv2.py Ajout C08 "desc" 500g 2.5 10 Espagne
    if action.lower() == "ajout" and len(sys.argv) == 8:
        _, _, code, desc, poids_unitaire, prix, tva, origine = sys.argv
        ajouter_produit(items, code, desc, poids_unitaire, prix, tva, origine)
    # Suppression d'un produit : python mainv2.py Suppression C06
    elif action.lower() == "suppression" and len(sys.argv) == 3:
        _, _, code = sys.argv
        enlever_produit(items, code)
    # Modification d'un produit : python mainv2.py Modification C06 "desc" 1.5L 6 10 Suisse
    elif action.lower() == "modification" and len(sys.argv) >= 3:
        code = sys.argv[2]
        desc = sys.argv[3] if len(sys.argv) > 3 else None
        poids_unitaire = sys.argv[4] if len(sys.argv) > 4 else None
        prix = sys.argv[5] if len(sys.argv) > 5 else None
        tva = sys.argv[6] if len(sys.argv) > 6 else None
        origine = sys.argv[7] if len(sys.argv) > 7 else None
        modifier_produit(items, code, desc, poids_unitaire, prix, tva, origine)
    # Affichage de la liste : python mainv2.py Liste
    elif action.lower() == "liste":
        afficher_liste_produits(items)
    # Génération d'un ticket : python mainv2.py "But Maket" "Lisa" "C01:10|C02:2"
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
        ticket(magasin, caissier, panier, items, ticket_number)
        # Incrémentation du numéro de ticket et sauvegarde
        ticket_number += 1
        sauvegarder_ticket_number(ticket_number)
    # Cas d'une commande invalide
    else:
        print("Commande invalide. Voir l'usage ci-dessous :")
        print('  python mainv2.py "But Maket" "Lisa" "C01:10|C02:2"')
        print('  python mainv2.py Ajout C08 "Produit" 500g 2.5 10 Espagne')
        print('  python mainv2.py Suppression C06')
        print('  python mainv2.py Modification C06 "desc" 1.5L 6 10 Suisse')
        print('  python mainv2.py Liste')