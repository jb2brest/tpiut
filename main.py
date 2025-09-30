
articles = [
        {"code": "C01", "description": "pack de coca", "prix_unite": 5, "tva": 20},
        {"code": "C02", "description": "kilo de pdt", "prix_unite": 1, "tva": 10},
        {"code": "C03", "description": "pack Biscotte", "prix_unite": 2, "tva": 10},
        {"code": "C04", "description": "Café soluble", "prix_unite": 3, "tva": 5},
        {"code": "C05", "description": "Crakers", "prix_unite": 4, "tva": 10},
    ]

def ticket(articles,titre,nom_caiss,chaine) :
    print(chaine)
    assert(chaine!=""),"La chaine ne dois pas etre vide"
    assert(chaine[0]=="C"),"Le format de chaine est incorrect"
    assert(chaine[-1]!="|"),"Ne dois pas terminer pas un |"
    
    
    
    totalHT = 0
    for dico in articles :
        dico["quantite"] = 0
    
    try :
        for chaine_carac in chaine.split("|") :
            code = chaine_carac.split(":")[0]
            quantite = chaine_carac.split(":")[1]
    
            for dico in articles :
                
                if dico["code"] == code :
                    dico["quantite"] = quantite
    except :
        raise IndexError("Il faut utiliser le caractère : pour séparer la quantité et le code dans la chaine")

    
        
    print(titre)
    print("Ticket numéro : 2200")
    print("Date : 08/09/2023")
    print("")
    print(f"Vous avez été servi par : {nom_caiss}")
    print("")
    print("NB	 Desc.	 HT unitaire  TVA	  Total")
    print("")
    total_TVA = 0
    total_HT = 0
    total = 0
    
    try : 
        for dico in articles :
            
            if dico["quantite"] != 0 :
                quant = dico['quantite']
                desc = dico['description']
                prix = dico['prix_unite']
                tva = int(dico['tva'])/100
               
                total_article = (int(quant) * int(prix)) + (int(quant) * int(prix)) * tva 
                
                totalHT += int(quant) * int(prix)
                total_TVA += int(quant) * int(prix) * tva

                total += total_article
                
                print(f"{quant}  {desc}    {prix}     {tva}      {total_article}")
    except :
        raise ValueError("Il faut respecter le format suivant : Cnombre:quantite|")
    
    print("")    
    print(f"Total Hors Taxes : {round(totalHT,3)}")
    print(f"Total Des Taxes : {round(total_TVA,3)}")
    print(f"Total : {round(total,3)}")
        
    
    
    

ticket(articles,"BUT MARKET","GUENAEL","C01:10|C02:10")
