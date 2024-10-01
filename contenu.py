
entree = "C01:10|C02:2"

def separation(liste_produit):
    produit_separee = liste_produit.split("|")

    print(produit_separee)
    return produit_separee
produit_separee = separation(entree)

""" PRODUITS """
C01 = ["pack de coca", 5]
C02 = ["kilo de pdt", 1]
C03 = ["pack Biscotte", 2]
C04 = ["Café soluble", 3]
C05 = ["Crakers", 4]

tableau_final = [["NB","Desc.","HT unitaire","TVA","Total"]]
total_HT = 0
total_TVA = 0
total_final = 0
tva = "10%"

"""         LISTE PRODUITS          """

for i in produit_separee:
    #print(i)
    produit = i.split(":")
    #print(produit)
    if produit[0] == "C01":
        nombre = produit[1]
        description = C01[0]
        prix_HT = C01[1]
        total = prix_HT*(1.1)*int(nombre)
        tableau_final.append([nombre,description,prix_HT,tva,total])
        #print(tableau_final)

        total_HT = total_HT + (prix_HT*int(nombre))
        total_TVA = total_TVA + (int(nombre) * 1.1)
        total_final = total_final + total


    elif produit[0] == "C02":
        nombre = produit[1]
        description = C02[0]
        prix_HT = C02[1]
        total = prix_HT*(1.1)*int(nombre)
        tableau_final.append([nombre,description,prix_HT,tva,total])
        #print(tableau_final)

        total_HT = total_HT + (prix_HT*int(nombre))
        total_TVA = total_TVA + (int(nombre) * 1.1)
        total_final = total_final + total


    elif produit[0] == "C03":
        nombre = produit[1]
        description = C03[0]
        prix_HT = C03[1]
        total = prix_HT*(1.1)*int(nombre)
        tableau_final.append([nombre,description,prix_HT + "€",tva,total])
        #print(tableau_final)

        total_HT = total_HT + (prix_HT*int(nombre))
        total_TVA = total_TVA + (int(nombre) * 1.1)
        total_final = total_final + total


    elif produit[0] == "C04":
        nombre = produit[1]
        description = C04[0]
        prix_HT = C04[1]
        total = prix_HT*(1.1)*int(nombre)
        tableau_final.append([nombre,description,prix_HT,tva,total])
        #print(tableau_final)

        total_HT = total_HT + (prix_HT*int(nombre))
        total_TVA = total_TVA + (int(nombre) * 1.1)
        total_final = total_final + total


    elif produit[0] == "C05":
        nombre = produit[1]
        description = C05[0]
        prix_HT = C05[1]
        total = prix_HT*(1.1)*int(nombre)
        tableau_final.append([nombre,description,prix_HT,tva,total])
        #print(tableau_final)


        total_HT = total_HT + (prix_HT*int(nombre))
        total_TVA = total_TVA + (int(nombre) * 1.1)
        total_final = total_final + total

"""         LISTE TOTAL          """


for i in range(len(tableau_final)):
    print(tableau_final[i])


print(f"Total HT : {total_HT} €")
print(f"Total TVA : {total_TVA} €")
print(f"Total : {total_final} €")