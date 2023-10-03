#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 08:38:45 2023

@author: axgillet
"""
import random
numero_ticket = 1

def BUT_Market(nom_magasin: str, serveur: str, achats: str):
    
    # Création des articles
    articles_info = {
        "C01": {"description": "pack de coca", "prix_unitaire_ht": 5},
        "C02": {"description": "kilo de pdt", "prix_unitaire_ht": 1},
        "C03": {"description": "pack Biscotte", "prix_unitaire_ht": 2},
        "C04": {"description": "Café soluble", "prix_unitaire_ht": 3},
        "C05": {"description": "Crakers", "prix_unitaire_ht": 4}
    }
    
    articles_list = achats.split('|') # Séparation des articles commandés en liste
     
    # Liste des articles
    articles = []
    total_ht = 0
    global numero_ticket
    numero_ticket += 1
    
    for article in articles_list:
         code, quantite = article.split(":")
         quantite = int(quantite)
         description = articles_info.get(code, {}).get('description', 'N/A')
         prix_unitaire_ht = articles_info.get(code, {}).get('prix_unitaire_ht', 0)
         
         # Calculs pour chaque article
         total_article = quantite * prix_unitaire_ht
         total_ht += total_article
         
         articles.append({
            "quantite": quantite,
            "description": description,
            "prix_unitaire_ht": prix_unitaire_ht,
            "total_article": total_article
         })

    total_tva = 0.1 * total_ht
    total = total_ht + total_tva
    
    
    # Affichage du ticket de caisse
    date = datetime. datetime. today(). strftime('%Y-%m-%d %H:%M:%S')
    print(f"{nom_magasin}")
    print(f"Ticket numéro : {numero_ticket}\n")
    print(f"Date : {date}\n")
    print(f"Vous avez été servi par : {serveur}\n")
    print("Code\tDesc.\t\t\tHT unitaire\tTotal")
    
    for article in articles:
        quantite = article["quantite"]
        description = article["description"]
        prix_unitaire_ht = article["prix_unitaire_ht"]
        total_article = article["total_article"]
        print(f"{quantite}\t{description}\t\t{prix_unitaire_ht}€\t\t{total_article:.1f}€")
        
    print("\n\t\t\t\tTotal HT\t{:.1f}€".format(total_ht))
    print("\t\t\t\tTotal TVA\t{:.1f}€".format(total_tva))
    print("\t\t\t\tTotal\t\t{:.1f}€".format(total))
        
    
    