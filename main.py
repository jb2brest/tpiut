dict = {'C01':["pack de coca",5],'C02':["kilo de pdt",1],'C03':["pack Biscotte",2],'C04':["Café soluble",3],'C05':["Crackers",4]}

def calcul_prix(dict, id, quantite):
    tva = 0.1
    prix_ht = dict[id][1]
    prix_tva = prix_ht+(tva*prix_ht)
    prix_total_tva = prix_tva*quantite
    prix_total_ht = prix_ht*quantite
    return (prix_ht,prix_tva,prix_total_tva,prix_total_ht)

if __name__ == "__main__":
    print(f"{'Code article':<20} {'Description':<20} {'Prix unitaire hors taxe':<25}")

    for codeArticle, (description, prix) in dict.items():
        print(f"{codeArticle:<20} {description:<20} {prix:<25}")



