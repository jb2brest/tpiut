# GÉNÉRER UN TICKET DE CAISSE
# Auteurs : Titouan ALMAIRAC et Alexandre GRALL
# Créé le 1 octobre 2025
# Version 1.2
# Dernière modification : 1 octobre 2025

import sys
from datetime import datetime

if len(sys.argv) != 4:
    print("Doit s'utiliser comme ça : python3 main.py \"NOM_MAGASIN\" \"NOM_HOTE-DE-CAISSE\" \"ARTICLE1:QTE1|ARTICLE2:QTE2|...\"")
    sys.exit(1)

param1 = sys.argv[1].strip()
param2 = sys.argv[2].strip()
param3 = sys.argv[3].strip()

# Articles disponibles
articles_disponibles = {
    "C01": ("Pack de BZHCola", 5),
    "C02": ("Kilo de PDT", 1),
    "C03": ("Pack de Biscotte", 2),
    "C04": ("Café soluble", 3),
    "C05": ("Crackers", 4)
}

taux_tva = 0.10

# Lire le numéro de ticket actuel depuis le fichier
try:
    with open('num_ticket.txt', 'r') as f:
        numero_ticket = int(f.read().strip())
except (FileNotFoundError, ValueError):
    numero_ticket = 1  # Valeur par défaut au cas où

date_str = datetime.now().strftime("%d/%m/%Y")

# Dictionnaire pour cumuler les articles
articles_commandes = {}

if not param3:
    print("Aucun article fourni, le ticket sera vide.")
else:
    paires = param3.split("|")

    for paire in paires:
        paire = paire.strip()
        if not paire:
            continue

        parts = paire.split(":")
        if len(parts) != 2:
            print(f"Format invalide pour '{paire}': attendu 'CODE:QTE' -> ignoré.")
            continue

        code_article, quantite_str = parts
        code_article = code_article.strip().upper()
        quantite_str = quantite_str.strip()

        try:
            quantite = int(quantite_str)
            if quantite <= 0:
                print(f"Quantité invalide pour '{paire}': doit être > 0 -> ignoré.")
                continue
        except ValueError:
            print(f"Quantité invalide pour '{paire}': '{quantite_str}' n'est pas un entier -> ignoré.")
            continue

        if code_article not in articles_disponibles:
            print(f"Code article '{code_article}' non reconnu -> ignoré.")
            continue

        # Cumul des quantités
        articles_commandes[code_article] = articles_commandes.get(code_article, 0) + quantite

# Préparation du ticket
lignes = []
total_ht = 0
total_tva = 0
total_ttc = 0

for code_article, quantite in articles_commandes.items():
    description, prix_unitaire = articles_disponibles[code_article]
    ht = prix_unitaire * quantite
    tva = ht * taux_tva
    total_ligne = ht + tva
    total_ht += ht
    total_tva += tva
    total_ttc += total_ligne
    lignes.append((quantite, description, prix_unitaire, taux_tva * 100, ht, tva, total_ligne))

    description, prix_unitaire = articles_disponibles[code_article]
    ht = prix_unitaire * quantite
    tva = ht * taux_tva
    total_ligne = ht + tva
    total_ht += ht
    total_tva += tva
    
# Affichage du ticket
print()
print(param1)
print(f"Ticket numéro : {numero_ticket}")
print()
print(f"Date : {date_str}")
print()
print(f"Vous avez été servi par : {param2}")
print()
print("NB  Desc.              HT unitaire  TVA   Total")

if lignes:
    for quantite, description, prix_unitaire, tva_pourcent, ht, tva_val, total_ligne in lignes:
        print(f"{quantite:<3} {description:<18} {prix_unitaire}€           {int(tva_pourcent)}%   {total_ligne:.1f}€")
    print()
    
    print(f"{'':>25}Total HT     {total_ht:.0f}€")
    print(f"{'':>25}Total TVA    {total_tva:.1f}€")
    print(f"{'':>25}Total        {total_ttc:.1f}€")
else:
    print("Aucun article valide à afficher.")
    print(f"{'':>25}Total HT     0€")
    print(f"{'':>25}Total TVA    0€")
    print(f"{'':>25}Total        0€")

print("\n")

# Incrémenter le numéro de ticket et l'écrire dans le fichier
numero_ticket += 1
with open('num_ticket.txt', 'w') as f:
    f.write(str(numero_ticket))
