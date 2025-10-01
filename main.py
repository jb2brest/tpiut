import sys
from datetime import datetime
import tkinter as tk

# Tableau des articles
articles : list
articles = [{"Code" : "C01", "Description" : "Pack de coca", "Poids" : 2000, "Prix"  : 5, "TVA" : 0.2, "Origine" : "Lituanie"},
            {"Code" : "C02", "Description" : "Kilo de pdt", "Poids" : 1000, "Prix"  : 1, "TVA" : 0.1, "Origine" : "Espagne"},
            {"Code" : "C03", "Description" : "Pack de Biscotte", "Poids" : 950, "Prix"  : 2, "TVA" : 0.1, "Origine" : "France"},
            {"Code" : "C04", "Description" : "Café soluble", "Poids" : 250, "Prix"  : 3, "TVA" : 0.1, "Origine" : "Roumanie"},
            {"Code" : "C05", "Description" : "Crakers", "Poids" : 125, "Prix"  : 4, "TVA" : 0.2, "Origine" : "Angleterre"},
            {"Code" : "C06", "Description" : "Eau", "Poids" : 1500, "Prix"  : 6, "TVA" : 0.1, "Origine" : "Suisse"},
            {"Code" : "C07", "Description" : "Pain", "Poids" : 250, "Prix"  : 1, "TVA" : 0.1, "Origine" : "France"}]

# Définition des variables
num_ticket : int = 2200

# Fonction Date
def Date() -> str : 
    """Fonction qui récupère la date.
    
    Returns:
        str: Date au format JJ/MM/YYYY
    """
    date : str = datetime.now()     # Récupère la date à l'instant T
    Date = date.strftime("%d/%m/%Y")    # Mise au format JJ/MM/YYYY
    return Date     # Affectation de cette valeur à la variable Date


def recuperer_infos_ticket(nom_mag, personnel, commande, articles_disponibles):
    catalogue = {art["Code"]: art for art in articles_disponibles}
    articles_ticket = []
    # Parcours les données rentrées par l'utilisateur
    for item in commande.split('|'):
        code, quant = item.split(':')
        quant = int(quant)
        if code in catalogue:
            art = catalogue[code]
            articles_ticket.append({
                "Desc": art["Description"],
                "Prix": art["Prix"],
                "TVA": art["TVA"],
                "Poids": art["Poids"],
                "Quantite": quant
            })
        else:
            print(f"Attention : code {code} non trouvé dans le catalogue.")

    return {
        "nom_mag": nom_mag,
        "personnel": personnel,
        "articles": articles_ticket,
        "TVA": articles_ticket[2]
    }


# Fonction Ticket de caisse
def Ticket_caisse(nom_mag : str, num : int, personnel : str, articles : list) : 
    """Fonction qui renvoi le ticket de caisse
    Args:
        nom_mag (str): Nom du magasin
        num (int): Numéro du ticket de caisse
        personnel (str): Prénom du caissier/ère
        articles (list): Liste des articles achetés par le client
    """
    num = num_ticket
    date = Date()
    
    # Création de la fenêtre
    ticket_c : tk = tk.Tk()
    ticket_c.title("Ticket de caisse")
    text = tk.Text(ticket_c, width=100, height=25)
    text.pack(padx=10, pady=10)

    # Mise en forme de notre ticket
    ticket = []
    # Affichage du nom du magasin dans le ticket
    ticket.append(f"{nom_mag}")
    # Affichage du numéro de ticket
    ticket.append(f"Ticket numéro : {num}")
    ticket.append("")
    # Affichage de la date
    ticket.append(f"Date : {date}")
    ticket.append("")
    # Affichage du prénom du caissier/ière
    ticket.append(f"Vous avez été servi par : {personnel}")
    ticket.append("")
    # Mise en place de l'entête de la liste des articles achetés
    ticket.append(f"{'NB':<4}{'Desc.':<20}{'Poids/volume unitaire':<25}{'Poids/volume total':<25}{'HT unitaire':<12}{'TVA':<6}{'Total'}")

    total_ht : int = 0
    total_tva : int = 0

    # Pour chaque articles qui se trouve dans la liste
    for article in articles:
        quantite = article["Quantite"]
        description = article["Desc"]
        prix = article["Prix"]
        poids = article["Poids"]
        TVA = article["TVA"]
        # Calcul des valeurs
        ht = prix * quantite
        montant_tva = ht * TVA
        total = ht + montant_tva
        
        volume_total = poids * quantite

        # Affichage des totaux HT/TVA/final avec mise en page
        ticket.append(f"{quantite:<4}{description:<20}{poids}g{'':<20}{volume_total}g{'':<20}{prix}€{'':<11}{int(TVA*100)}%{total:>6.1f}€")

        total_ht += ht
        total_tva += montant_tva

    ticket.append("")
    
    # Mise en page de ces données
    ticket.append(f"{'Total HT':<15}{total_ht:.1f}€")
    ticket.append(f"{'Total TVA':<15}{total_tva:.1f}€")
    ticket.append(f"{'Total':<15}{total_ht+total_tva:.1f}€")

    # Ajout du texte au widget
    text.insert(tk.END, "\n".join(ticket))
    text.config(state="disabled")  #lecture seule

    ticket_c.mainloop()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        # Affichage du mode d'usage si l'utilisateur oubli un paramètre
        print("Usage : python3 main.py <NomMagasin> <Personnel> <Commande>")
        print('Exemple : python3 main.py "But Maket" "Lisa" "C01:10|C02:2"')
        sys.exit(1)

    #Incrémentation du numéro de ticket
    num_ticket += 1
    nom_mag, personnel, commande_client = sys.argv[1], sys.argv[2], sys.argv[3]

    # Vérification si il y a un numéro dans le prénom
    while not personnel.isalpha():
        personnel = input("Veuillez saisir un prénom valide : ")

    # Vérification de la commande faite
    while True:
        try:
            commande_dict = dict(item.split(":") for item in commande_client.split("|"))
            # Vérification que toutes les quantités sont des entiers > 0
            for quant in commande_dict.values():
                if int(quant) <= 0:
                    raise ValueError
            break  # Tout est ok
        except (ValueError, AttributeError):
            commande_client = input(
                'Merci de renseigner les articles sous la forme C01:10|C02:2 : '
            )
    # Récupère les informations nécessaires
    infos = recuperer_infos_ticket(nom_mag, personnel, commande_client, articles)

    # Récupère les infos nécessaire pour générer notre ticket
    Ticket_caisse(
        nom_mag=infos["nom_mag"],
        num=num_ticket,
        personnel=infos["personnel"],
        articles=infos["articles"]
    )
