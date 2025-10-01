# GÉNÉRER UN TICKET DE CAISSE
# Auteurs : Titouan ALMAIRAC et Alexandre GRALL
# Créé le 1 octobre 2025
# Version 1.2
# Dernière modification : 1 octobre 2025


import sys
from datetime import datetime
import re

def parse_weight_volume(s):
    s = s.strip().lower()
    match = re.match(r"([\d\.]+)\s*(kg|g|l|ml)", s)
    if not match:
        return None
    value, unit = match.groups()
    value = float(value)
    if unit == "kg":
        return value * 1000  # grammes
    elif unit == "g":
        return value
    elif unit == "l":
        return value * 1000  # millilitres
    elif unit == "ml":
        return value
    return None

if len(sys.argv) != 4:
    print("Doit s'utiliser comme ça : python3 main.py \"NOM_MAGASIN\" \"NOM_HOTE-DE-CAISSE\" \"ARTICLE1:QTE1|ARTICLE2:QTE2|...\"")
    sys.exit(1)

param1 = sys.argv[1].strip()
param2 = sys.argv[2].strip()
param3 = sys.argv[3].strip()


# Articles disponibles avec description, poids/volume unitaire, prix HT unitaire, taux TVA, origine
articles_disponibles = {
    "C01": ("pack de coca", "2kg", 5, 0.20),
    "C02": ("kilo de pdt", "1kg", 1, 0.10),
    "C03": ("pack Biscotte", "950g", 2, 0.10),
    "C04": ("Café soluble", "250g", 3, 0.10),
    "C05": ("Crakers", "125g", 4, 0.20),
    "C06": ("Eau", "1.5L", 6, 0.10),
    "C07": ("Pain", "250g", 1, 0.10)
}

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
    description, poids_unitaire, prix_unitaire, taux_tva = articles_disponibles[code_article]
    poids_unitaire_val = parse_weight_volume(poids_unitaire)
    if poids_unitaire_val is None:
        poids_unitaire_val = 0
    poids_total_val = poids_unitaire_val * quantite

    def format_weight(val):
        if val >= 1000:
            if poids_unitaire.lower().endswith("l"):
                return f"{val/1000:.2f}L"
            else:
                return f"{val/1000:.2f}kg"
        else:
            if poids_unitaire.lower().endswith("l"):
                return f"{int(val)}ml"
            else:
                return f"{int(val)}g"

    poids_total_str = format_weight(poids_total_val)

    ht = prix_unitaire * quantite
    tva = ht * taux_tva
    total_ligne = ht + tva
    total_ht += ht
    total_tva += tva
    total_ttc += total_ligne
    lignes.append((quantite, description, poids_unitaire, poids_total_str, prix_unitaire, int(taux_tva*100), ht, tva, total_ligne))
    
# Affichage du ticket
print()
print(param1)
print(f"Ticket numéro : {numero_ticket}")
print()
print(f"Date : {date_str}")
print()
print(f"Vous avez été servi par : {param2}")
print()
print("NB  Desc.              Poids/volume unitaire  Poids/volume total  HT unitaire  TVA   Total")

if lignes:
    for quantite, description, poids_unitaire, poids_total, prix_unitaire, tva_pourcent, ht, tva_val, total_ligne in lignes:
        print(f"{quantite:<3} {description:<18} {poids_unitaire:<22} {poids_total:<19} {prix_unitaire}€           {tva_pourcent}%   {total_ligne:.1f}€")
    print()
    
    print(f"{'':>60}Total HT     {total_ht:.0f}€")
    print(f"{'':>60}Total TVA    {total_tva:.1f}€")
    print(f"{'':>60}Total        {total_ttc:.1f}€")
else:
    print("Aucun article valide à afficher.")
    print(f"{'':>60}Total HT     0€")
    print(f"{'':>60}Total TVA    0€")
    print(f"{'':>60}Total        0€")

print("\n")

# Incrémenter le numéro de ticket et l'écrire dans le fichier
numero_ticket += 1
with open('num_ticket.txt', 'w') as f:
    f.write(str(numero_ticket))
