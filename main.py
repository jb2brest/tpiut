import datetime
import sys
import re 

aujourd_hui = datetime.datetime.today()
date = aujourd_hui.strftime("%d/%m/%Y")
fichier = "compteur.txt"

# Lire la valeur actuelle
try:
    with open(fichier, "r") as f:
        num_ticket = int(f.read())
except FileNotFoundError:
    num_ticket = 0  # valeur initiale si le fichier n'existe pas

# Incrémenter
num_ticket += 1

# Sauvegarder la nouvelle valeur
with open(fichier, "w") as f:
    f.write(str(num_ticket))

lieu = sys.argv[1]

prenom = sys.argv[2]

articles = sys.argv[3]

# Vérifications de la comformité des variables
lieu_valid = re.match(r"^[A-Za-z0-9\- ]+$", lieu)

prenom_valid = re.match(r"^[A-Za-zÀ-ÖØ-öø-ÿ\-]+$", prenom)

articles_valid = re.match(r"^([A-Z0-9]+:\d+)(\|[A-Z0-9]+:\d+)*$", articles)

# liste des objets
lst_item = {"C01":{"nom":"pack de coca","prix":5},
            "C02":{"nom":"kilo de pdt","prix":1},
            "C03":{"nom":"pack Biscotte","prix":2},
            "C04":{"nom":"Café soluble","prix":3},
            "C05":{"nom":"Crackers","prix":4}}

articles_liste = articles.split("|")
# vérifie si les regex sont valides 
if lieu_valid and prenom_valid and articles_valid:
    # vérifie si on ne cherche pas un code article inexistant
    nb=0
    erreur=False
    while nb < len(articles_liste) and erreur == False:
        if articles_liste[nb][0:3] not in lst_item:
            erreur=True
        else:
            nb+=1
    # Impression du ticket en console        
    if erreur==False:
        print(lieu)
        print(f"Ticket numéro : {num_ticket} \n")
        print(f"Date : {date}\n")
        print(f"Vous avez été servi par : {prenom}\n")
        print("NB   Desc.           HT unitaire     TVA     Total")
        total_HT=0
        total_TTC=0
        total_TVA=0
        for article in articles_liste:
            lst=article.split(":")
            total_prduit=lst_item[lst[0]]["prix"]*1.1*int(lst[1])
            total_HT+=lst_item[lst[0]]["prix"]*int(lst[1])
            total_TTC+=lst_item[lst[0]]["prix"]*1.1*int(lst[1])
            total_TVA+=lst_item[lst[0]]["prix"]*int(lst[1])*0.1
            print(f"{int(lst[1])}    {lst_item[lst[0]]['nom']}       {lst_item[lst[0]]['prix']}         10%         {total_prduit}")
        print("\n")
        print(f"Total HT {total_HT}")
        print(f"Total TVA {total_TVA}")
        print(f"Total {total_TTC}") 
    else:
        print("le code d'article que vous avez rentrer n'est pas dans la liste des item.")
else: 
    # En cas de nom respect des regexs message d'erreur adapté 
    if not re.match(r'^[\w\s]+$', lieu):
        print("Erreur : Le lieu contient des caractères non autorisés")
        sys.exit(1)

    if not re.match(r'^[A-Za-zÀ-ÖØ-öø-ÿ]+$', prenom):
        print("Erreur : Le prénom n'est pas valide")
        sys.exit(1)

    if not re.match(r'^(C0[1-5]:[0-9]+)(\|C0[1-5]:[0-9]+)*$', articles):
        print("Erreur : La liste d'articles n'est pas valide ")