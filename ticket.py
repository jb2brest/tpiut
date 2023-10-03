from datetime import datetime
from exceptions import EntreeVide
import sys

def argParser(argData:str):
    """
    Fonction séparant les données reçus pour analyse des items
    @param: argData = article:nombre|article:nombre
    """
    basket= argData.split('|')
    sArticles = []
    for i in basket:
        art=i.split(':')
        articleCode=art[0]
        articleNb=art[1]
        sArticles.append([articleCode, articleNb])
    return sArticles

def itemParsing(articleCode: str, nb: int)-> str:
    """
    Fonction faisant le lien entre les items et leurs infos
    @param: articleCode = code de l'article
            nb = nombre d'article
    """
    desc: str = ""
    nb: float = float(nb)
    TVA: float = 1.1
    match articleCode:
        case "C01":
                desc="pack de coca"
                priceHT=5
                priceTot=nb*(priceHT*TVA)
        case "C02":
                desc="kilo de pdt"
                priceHT=1
                priceTot=nb*(priceHT*TVA)
        case "C03":
                desc="pack Biscotte"
                priceHT=2
                priceTot=nb*(priceHT*TVA)
        case "C04":
                desc="Café soluble"
                priceHT=3
                priceTot=nb*(priceHT*TVA)
        case "C05":
                desc="Crakers"
                priceHT=4
                priceTot=nb*(priceHT*TVA)
        case _:
                desc="Erreur A1: code article incorrect"
                priceHT=0
                priceTot=0
    return(desc,priceHT,priceTot)

def betterAff(articles: list)->list:
    """
    Fonction serialisant les données pour être exploitées
    @param: listes brute d'articles et des données liées
    """
    nb = []
    desc = []
    pht = []
    ptot = []
    for i in articles:
        nb.append(i[0])
        desc.append(i[1][0])
        pht.append(i[1][1])
        ptot.append(i[1][2])
    return nb, desc, pht, ptot

def ticketAff(ticket):
    """
    Fonction permettant d'afficher et de mettre en page le ticket de caisse
    @param: données serialisées de la commande
    """
    try:
        with open("ticketcounter.txt", "r") as fichier:
            numero = int(fichier.read())
    except FileNotFoundError:
        numero = -1
    with open("ticketcounter.txt", "w") as fichier:
        fichier.write(str(numero + 1))
    nbs, descs, hts, totaux = ticket

    totalHt = 0
    totalTva = 0
    totalGeneral = 0

    print(shopname)
    print("Ticket numéro : "+str(numero)+"\n")
    print("Date : ", tdate)
    print("\nVous avez été servis par : ", employee)
    print("\nNB\tDesc.\t\tHT unitaire\tTVA\tTotal")

    for nb, desc, ht, total in zip(nbs, descs, hts, totaux):
        tva = ht * 0.1
        print(f"{nb}\t{desc}\t\t{ht}€\t10%\t{round(total, 2)}€")

        totalHt += ht * int(nb)
        totalTva += tva * int(nb)
        totalGeneral += total

    # Afficher les totaux


    print(f"\n\t\t\t\tTotal HT	{round(totalHt, 2)}€\n\t\t\t\tTotal TVA	{round(totalTva, 2)}€\n\t\t\t\tTotal 		{round(totalGeneral, 2)}€")


if __name__ == "__main__":
    current_time = datetime.now()
    try:
        shopname=sys.argv[1]
        if shopname == "":
            raise EntreeVide()
        else:
            pass
    except EntreeVide as e:
        print("Erreur A2: Le nom du magasin ne peut pas être vide")
        sys.exit(1)
    
    try:
        employee=sys.argv[2]
        if employee == "":
            raise EntreeVide()
        else:
            pass
    except EntreeVide as e:
        print("Erreur A2: Le nom de l'employé(e) ne peut pas être vide")
        sys.exit(1)
    tdate=current_time.strftime('%d/%m/%Y')
    
    try:
        parsedArgs=argParser(sys.argv[3])
    except IndexError as e:
        print("Erreur A3: Articles invalides")
        sys.exit(1)
    
    articles = []
    for i in parsedArgs:
        articles.append([i[1],itemParsing(i[0], i[1])])
    data=betterAff(articles)
    
    ticketAff(data) # affichage du ticket
