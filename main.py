import sys
import datetime


# BDD : Dictionnaire avec code article comme clé
# Pour rajouter un produit dans ce dictionnaire, il suffit de copier-coller une ligne et de modifier les valeurs
bdd = {
    "C01": {"description": "pack de coca", "poids": 2, "prix": 5, "TVA": 0.2, "Orgine": "Lituanie"},
    "C02": {"description": "kilo de pdt", "poids": 1, "prix": 1, "TVA": 0.1, "Orgine": "Espagne"},
    "C03": {"description": "pack Biscotte", "poids": 0.95, "prix": 2, "TVA": 0.1, "Orgine": "France"},
    "C04": {"description": "Café soluble", "poids": 0.25, "prix": 3, "TVA": 0.1, "Orgine": "Roumanie"},
    "C05": {"description": "Crakers", "poids": 0.125, "prix": 4, "TVA": 0.2, "Orgine": "Angleterre"},
    "C06": {"description": "Eau", "poids": 1.5, "prix": 6, "TVA": 0.1, "Orgine": "Suisse"},
    "C07": {"description": "Pain", "poids": 0.25, "prix": 1, "TVA": 0.1, "Orgine": "France"}
}

try:
    nom_magasin = str(sys.argv[1])
except:
    print("Erreur: Veuillez entrer un nom de magasin valide.")
    exit()
try:
    serveur = str(sys.argv[2])
except:
    print("Erreur: Veuillez entrer un nom de serveur valide.")
    exit()
articles = sys.argv[3].split("|")

articles_dict = {}
for article in articles :
    code, qnt = article.split(":")

    try:
        bdd[code]
    except KeyError:
        print(f"Erreur: Le code article '{code}' n'existe pas dans la base de données.")
        exit()
    try:
        qnt = int(qnt)
    except ValueError:
        print(f"Erreur: La quantité '{qnt}' n'est pas un nombre valide.")
        exit()
        
    articles_dict[code] = qnt


def calcul_resultat(dico: dict, articles:dict) -> tuple:
    """Calcule les résultats de la vente.

    Args:
        dico (dict): le dictionnaire des articles disponibles à la vente.
        articles (dict): le dictionnaire des articles du ticket de caisse et de leur quantité.

    Returns:
        tuple: liste_prix, total, TVA_total
    """
    prix:list = []
    liste_prix:list = []
    total = 0
    TVA_total = 0
    
    for article in articles.keys():
        if article in dico:
            quantite = articles[article]
            prix_unitaire = dico[article]["prix"]
            prix_total_ht = round(prix_unitaire * quantite,2)
            tva_montant = round(prix_total_ht * dico[article]["TVA"], 2)  # Arrondir pour éviter les problèmes de précision
            poids_unitaire = dico[article]["poids"]
            poids_total = round(poids_unitaire*quantite,2)
            prix=[article, quantite, prix_unitaire, prix_total_ht, tva_montant,poids_unitaire,poids_total]
            liste_prix.append(prix)
            total += prix_total_ht
            TVA_total += tva_montant
    
    return liste_prix, total, round(TVA_total, 2)

def generer_numero_ticket():
    """Génère un numéro de ticket incrémental en le sauvegardant dans un fichier."""
    fichier_numero = "numero_ticket.txt"
    
    try:
        # Lire le dernier numéro utilisé
        with open(fichier_numero, "r") as f:
            numero_actuel = int(f.read().strip())
    except (FileNotFoundError, ValueError):
        # Si le fichier n'existe pas ou est corrompu, commencer à 1
        numero_actuel = 1
    
    # Incrémenter le numéro
    numero_actuel += 1
    
    # Sauvegarder le nouveau numéro
    with open(fichier_numero, "w") as f:
        f.write(str(numero_actuel))
    
    return numero_actuel

def formater_poids(poids_kg):
    """Formate le poids en kg ou g selon la valeur pour une meilleure lisibilité."""
    if poids_kg < 1:
        return f"{int(poids_kg * 1000)}g"
    else:
        return f"{poids_kg:.2f}kg"

def affichage(articles: dict, bdd: dict) -> str:
    """Affiche le ticket de caisse.

    Args:
        articles (dict): le dictionnaire des articles du ticket de caisse et de leur quantité.
        bdd (dict): le dictionnaire des articles disponibles à la vente.

    Returns:
        str: le ticket de caisse formaté.
    """
    # Utiliser la fonction calcul_resultat
    liste_prix, total_ht, total_tva = calcul_resultat(bdd, articles)
    total_ttc = total_ht + total_tva

    # Générer un numéro de ticket incrémental
    numero_ticket = generer_numero_ticket()

    print(nom_magasin)
    print(f"Ticket numéro : {numero_ticket}")
    print()
    print(f"Date : {datetime.date.today().strftime('%d/%m/%Y')}")
    print()
    print(f"Vous avez été servi par : {serveur}")
    print()
    
    print(f"{'NB':<4} {'Description':<15} {'Poids Unit.':<12} {'Poids Total':<12} {'HT unitaire':<12} {'TVA':<5} {'Total':<8}")
    
    # Utiliser les données calculées par calcul_resultat
    poids_total_commande = 0
    for prix_info in liste_prix:
        article_code = prix_info[0]
        quantite = prix_info[1]
        prix_unitaire = prix_info[2]
        prix_total_ht = prix_info[3]
        tva_montant = prix_info[4]
        poids_unitaire = prix_info[5]
        poids_total_article = prix_info[6]
        total_ligne_ttc = prix_total_ht + tva_montant
        
        # Ajouter au poids total de la commande
        poids_total_commande += poids_total_article
        
        print(f"{quantite:<4} {bdd[article_code]['description']:<15} {formater_poids(poids_unitaire):<12} {formater_poids(poids_total_article):<12} {prix_unitaire}€{'':<10} {int(bdd[article_code]['TVA']*100)}%{'':<2} {total_ligne_ttc:.2f}€")
    
    print()
    # Afficher les totaux calculés par calcul_resultat
    print(f"{'':<48}{'Total Poids':<11} : {formater_poids(poids_total_commande):>9}")
    print(f"{'':<48}{'Total HT':<11} : {total_ht:>8.2f}€")
    print(f"{'':<48}{'Total TVA':<11} : {total_tva:>8.2f}€")
    print(f"{'':<48}{'Total TTC':<11} : {total_ttc:>8.2f}€")

affichage(articles_dict, bdd)

# Test de la fonction calcul_resultat
if __name__ == "__main__":
    # Test avec des données spécifiques
    art_test = {'C03': 12, 'C01': 10}
    resultat_test = calcul_resultat(bdd, art_test)
    print("Test de calcul_resultat:", resultat_test)
    
    # Vérification que les calculs sont corrects
    expected = ([['C03', 12, 2, 24, 2.4, 0.95, 11.4], ['C01', 10, 5, 50, 10.0, 2, 20]], 74, 12.4)
    assert resultat_test == expected, f"Test échoué: attendu {expected}, obtenu {resultat_test}"
