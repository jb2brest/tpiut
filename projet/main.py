import sys
import datetime

produits:dict = {
    "C01" : {"desc":"pack de coca","HTuni":5,"TVA":10,"poids":2},
    "C02" : {"desc":"kilo de pdt","HTuni":1,"TVA":10,"poids":1},
    "C03" : {"desc":"pack biscotte","HTuni":2,"TVA":10,"poids":0.950},
    "C04" : {"desc":"Café soluble","HTuni":3,"TVA":10,"poids":0.250},
    "C05" : {"desc":"Crakers","HTuni":4,"TVA":10,"poids":0.125}
}

if __name__ == "__main__":

    tot = len(sys.argv)
    nom_mag :str = sys.argv[1]
    employe :str = sys.argv[2]
    articles :str = sys.argv[3]

    date = datetime.date.today().strftime("%d/%m/%Y")
    total : int = 0


print(nom_mag)
print(f"Numéro du ticket : 2200")
print(f"\n{date}")
print(f"\nVous avez été servi par {employe}\n")
print("NB   Desc    poids    HT unitaire TVA Total_HT    Total_TTC")
for article in articles.split("|") :
    code , qte = article.split(":")
    TVA_art = round(((produits[code]['HTuni'] * ((produits[code]['TVA'])/100+1))*int(qte)),3)
    print(f"{qte}   {produits[code]['desc']}    {produits[code]['poids']*int(qte)}kg    {float(produits[code]['HTuni']*int(qte))}€  {produits[code]['TVA']}% {TVA_art}€")
    total += int(TVA_art)
print(f"\nTotal TTC: {total}€")
