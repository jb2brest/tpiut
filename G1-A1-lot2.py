# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 09:48:52 2023

@author: luprigent
"""

import datetime

def BUT_Market(nom_magasin: str, serveur: str, achats: str):
    
    global ticket
    ticket += 1
    
    #
    articles_info = {
        "C01": {"description": "pack de coca ", "prix_unitaire_ht": 5, "poids_volume_unitaire": "2 kg", "tva": 20},
        "C02": {"description": "kilo de pdt  ", "prix_unitaire_ht": 1, "poids_volume_unitaire": "1 kg", "tva": 10},
        "C03": {"description": "pack Biscotte", "prix_unitaire_ht": 2, "poids_volume_unitaire": "950g", "tva": 10},
        "C04": {"description": "Café soluble ", "prix_unitaire_ht": 3, "poids_volume_unitaire": "250g", "tva": 10},
        "C05": {"description": "Crakers      ", "prix_unitaire_ht": 4, "poids_volume_unitaire": "125g", "tva": 20},
        "C06": {"description": "Eau          ", "prix_unitaire_ht": 6, "poids_volume_unitaire": "1,5L", "tva": 10},
        "C07": {"description": "Pain         ", "prix_unitaire_ht": 1, "poids_volume_unitaire": "250g", "tva": 10}
    }
    
    articles_list = achats.split('|') ##Permet la séparation des articles
     
    # Liste des articles
    articles = []
    total_ht = 0
    
    for article in articles_list:
        code, quantite = article.split(":")
        quantite = int(quantite)
        article_info = articles_info.get(code, {})
        description = article_info.get('description', 'N/A')
        prix_unitaire_ht = article_info.get('prix_unitaire_ht', 0)
        poids_volume_unitaire = article_info.get('poids_volume_unitaire', 'N/A')
        tva = article_info.get('tva', 0)
        
        # Calculs pour chaque article
        total_article = quantite * prix_unitaire_ht
        total_ht += total_article
        
        articles.append({
            "quantite": quantite,
            "description": description,
            "prix_unitaire_ht": prix_unitaire_ht,
            "poids_volume_unitaire": poids_volume_unitaire,
            "tva": tva,
            "total_article": total_article
        })

    total_tva = sum((article["quantite"] * article["prix_unitaire_ht"] * article["tva"] / 100) for article in articles)
    total = total_ht + total_tva
    
    # Affichage du ticket de caisse
    date = datetime.datetime.today().strftime('%d-%m-%Y')
    print(f"{nom_magasin}")
    print(f"Ticket numéro : {ticket}\n")
    print(f"Date : {date}\n")
    print(f"Vous avez été servi par : {serveur}\n")
    print("NB\tDescription\t\t\tPoids/Volume\tHT unitaire\t\t\tTVA\t\tTotal")
    
    for article in articles:
        quantite = article["quantite"]
        description = article["description"]
        poids_volume_unitaire = article["poids_volume_unitaire"]
        prix_unitaire_ht = article["prix_unitaire_ht"]
        tva = article["tva"]
        total_article = article["total_article"]
        print(f"{quantite}\t{description}\t\t{poids_volume_unitaire}\t\t\t{prix_unitaire_ht}€\t\t\t\t\t{tva}%\t\t{total_article:.1f}€")
    
    print("\n\t\t\t\t\t\t\t\t\t\t\t\t\tTotal HT\t\t{:.1f}€".format(total_ht))
    print("\t\t\t\t\t\t\t\t\t\t\t\t\tTotal TVA\t\t{:.1f}€".format(total_tva))
    print("\t\t\t\t\t\t\t\t\t\t\t\t\tTotal\t\t\t{:.1f}€".format(total))
   
