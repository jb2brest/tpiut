articles = [
        {"code": "C01", "description": "pack de coca", "prix_unite": 5, "tva": 20, "poids_ou_volume": "2kg", "origine": "Lituanie"},
        {"code": "C02", "description": "kilo de pdt", "prix_unite": 1, "tva": 10, "poids_ou_volume": "1kg", "origine": "Espagne"},
        {"code": "C03", "description": "pas Biscotte", "prix_unite": 2, "tva": 10, "poids_ou_volume": "950g", "origine": "France"},
        {"code": "C04", "description": "Café soluble", "prix_unite": 3, "tva": 10, "poids_ou_volume": "250g", "origine": "Roumanie"},
        {"code": "C05", "description": "Crackers", "prix_unite": 4, "tva": 20, "poids_ou_volume": "125g", "origine": "Angleterre"},
        {"code": "C06", "description": "Eau", "prix_unite": 6, "tva": 10, "poids_ou_volume": "1,5L", "origine": "Suisse"},
        {"code": "C07", "description": "Pain", "prix_unite": 1, "tva": 10, "poids_ou_volume": "250g", "origine": "France"},
    ]
def ticket(articles,titre,nom_caiss,chaine) :
    
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
    print("NB	 Desc.	Poid_unitaire Poid_total  Prix_HT_unitaire  TVA	  Total")
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
                poid_uni = dico['poids_ou_volume']
                poid_total = ""
                
                
                
                try :
                    for lettre in dico['poids_ou_volume'] :
                        if lettre in '0123456789' :
                            poid_total+=lettre
                        elif lettre in ',' :
                            poid_total+='.'
                except :
                    print("")
               
                
                if "." in poid_total :
                    
                    poid_total = str(float(poid_total) * int(quant) )
                else : 
                    poid_total = str(int(poid_total) * int(quant) )
                

                if poid_uni[-1]== 'g' :
                    
                    if poid_uni[-2:]=="kg" :
                        poid_total = poid_total + "kg"
                    else :
                        if int(poid_total) > 999 :
                            poid_total = str(int(poid_total)/1000) + "kg"
                        else :
                            poid_total = poid_total + "g"
                        
                else :
                    poid_total = poid_total + "L"
                
      
                tva = int(dico['tva'])/100
               
                total_article = (int(quant) * int(prix)) + (int(quant) * int(prix)) * tva 
                
                totalHT += int(quant) * int(prix)
                
                total_TVA += int(quant) * int(prix) * tva

                total += total_article
                
                print(f"{quant}  {desc}   {poid_uni}   {poid_total}    {prix}     {tva}      {total_article}")
    except :
        raise ValueError("Il faut respecter le format suivant : Cnombre:quantite|")
    
    print("")    
    print(f"Total Hors Taxes : {round(totalHT,3)}")
    print(f"Total Des Taxes : {round(total_TVA,3)}")
    print(f"Total : {round(total,3)}")
        
    

ticket(articles,"BUT MARKET","GUENAEL","C01:10|C02:10|C03:10|C04:2|C05:10|C06:10|C07:3")
