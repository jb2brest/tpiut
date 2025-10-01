import sys
from datetime import datetime
import tkinter as tk

# Tableau des articles
articles : list
articles = [{"Code" : "C01", "Description" : "Pack de coca", "Prix"  : 5},
            {"Code" : "C02", "Description" : "Kilo de pdt", "Prix"  : 1},
            {"Code" : "C03", "Description" : "Pack de Biscotte", "Prix"  : 2},
            {"Code" : "C04", "Description" : "Café soluble", "Prix"  : 3},
            {"Code" : "C05", "Description" : "Crakers", "Prix"  : 4}]

# Définition des variables
TVA : float = 0.1
Total_TVA : float = 0.0
Total_HT : float = 0.0
Total_articles : float = 0.0
Total_final : float = 0.0
num_ticket : str = 2200


# Fonction Date
def Date() -> str : 
    """Fonction qui récupère la date.
    
    Returns:
        str: Date au format JJ/MM/YYYY
    """
    date : str = datetime.now()     # Récupère la date à l'instant T
    Date = date.strftime("%d/%m/%Y")    # Mise au format JJ/MM/YYYY
    return Date()     # Affectation de cette valeur à la variable Date


def recuperer_infos_ticket(nom_mag, personnel, commande, articles_disponibles):
    catalogue = {art["Code"]: art for art in articles_disponibles}
    articles_ticket = []

    for item in commande.split('|'):
        code, quant = item.split(':')
        quant = int(quant)
        if code in catalogue:
            art = catalogue[code]
            articles_ticket.append({
                "Desc": art["Description"],
                "Prix": art["Prix"],
                "TVA": TVA,
                "Quantite": quant
            })
        else:
            print(f"Attention : code {code} non trouvé dans le catalogue.")

    return {
        "nom_mag": nom_mag,
        "personnel": personnel,
        "articles": articles_ticket
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
    num = num_ticket + 1
    
    # Création de la fenêtre
    ticket_c : tk = tk.Tk()
    ticket_c.title("Ticket de caisse")
    text = tk.Text(ticket_c, width=50, height=25)
    text.pack(padx=10, pady=10)

    # Mise en forme de notre ticket
    ticket = []
    # Affichage du nom du magasin dans le ticket
    ticket.append(f"{nom_mag}")
    # Affichage du numéro de ticket
    ticket.append(f"Ticket numéro : {num}")
    ticket.append("")
    # Affichage de la date
    ticket.append(f"Date : {Date}")
    ticket.append("")
    # Affichage du prénom du caissier/ière
    ticket.append(f"Vous avez été servi par : {personnel}")
    ticket.append("")
    # Mise en place de l'entête de la liste des articles achetés
    ticket.append(f"{'NB':<4}{'Desc.':<15}{'HT unitaire':<12}{'TVA':<6}{'Total'}")

    total_ht = Total_HT
    total_tva = Total_TVA

    # Pour chaque articles qui se trouve dans la liste
    for article in articles:
        quantite = article["Quantite"]
        description = article["Desc"]
        prix = article["Prix"]
        tva = article["TVA"]

        ht = prix * quantite
        montant_tva = ht * tva
        total = ht + montant_tva

        # Affichage des totaux HT/TVA/final avec mise en page
        ticket.append(f"{quantite:<4}{description:<15}{prix}€{'':<6}{int(tva*100)}%{total:>6.1f}€")

        total_ht += ht
        total_tva += montant_tva

    ticket.append("")
    
    # Mise en page de ces données
    ticket.append(f"{'Total HT':<20}{total_ht:.1f}€")
    ticket.append(f"{'Total TVA':<20}{total_tva:.1f}€")
    ticket.append(f"{'Total':<20}{total_ht+total_tva:.1f}€")

    # Ajout du texte au widget
    text.insert(tk.END, "\n".join(ticket))
    text.config(state="disabled")  #lecture seule

    ticket_c.mainloop()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage : python3 main.py <NomMagasin> <Personnel> <Commande>")
        print('Exemple : python3 main.py "But Maket" "Lisa" "C01:10|C02:2"')
        sys.exit(1)

    nom_mag, personnel, commande_client = sys.argv[1], sys.argv[2], sys.argv[3]

    infos = recuperer_infos_ticket(nom_mag, personnel, commande_client, articles)

    Ticket_caisse(
        nom_mag=infos["nom_mag"],
        num=num_ticket,
        personnel=infos["personnel"],
        articles=infos["articles"]
    )
