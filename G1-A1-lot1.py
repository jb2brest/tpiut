# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 08:48:52 2023

@author: luprigent
"""
import datetime

ticket = 1

def BUT_Market(magasin: str, serveur: str, achats: str):
    
    # Création des articles
    info_articles = {
        "C01": {"description": "pack de coca ", "prix_ht": 5},
        "C02": {"description": "kilo de pdt  ", "prix_ht": 1},
        "C03": {"description": "pack Biscotte", "prix_ht": 2},
        "C04": {"description": "Café soluble ", "prix_ht": 3},
        "C05": {"description": "Crakers      ", "prix_ht": 4}
    }
    
    articles_list = achats.split('|')#Permet la séparation des articles
     
    # Liste des articles
    articles = []
    total_ht = 0
    
    global ticket
    ticket += 1
    
    for article in articles_list:
         
         code, quantite = article.split(":")
         quantite = int(quantite)
         description = info_articles.get(code, {}).get('description', 'N/A')
         prix_ht = info_articles.get(code, {}).get('prix_ht', 0)
         
         # Calculs des prix pour chaque articles avec la quantité
         total_article = quantite * prix_ht
         total_ht += total_article
         
         
         articles.append({
            "quantite": quantite,
            "description": description,
            "prix_ht": prix_ht,
            "total_article": total_article
         })
           

    total_tva = total_ht * 0.1
    total = total_ht + total_tva
    
    
    # Affichage du ticket
    date = datetime. datetime. today(). strftime('%d-%m-%Y')
    print(f"{magasin}")
    print(f"Ticket numéro : {ticket}\n")
    print(f"Date : {date}\n")
    print(f"Vous avez été servi par : {serveur}\n")
    print("Code\tDesc.\t\t\tHT \t\tTotal")
    
    for article in articles:
        quantite = article["quantite"]
        description = article["description"]
        prix_ht = article["prix_ht"]
        total_article = article["total_article"]
        print(f"{quantite}\t{description}\t\t{prix_ht}€\t\t{total_article}€")
        
    print("\n\t\t\t\tTotal HT\t{:.1f}€".format(total_ht))
    print("\t\t\t\tTotal TVA\t{:.1f}€".format(total_tva))
    print("\t\t\t\tTotal\t\t{:.1f}€".format(total))
        
    
    
