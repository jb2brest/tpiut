from datetime import datetime

# Tableau des articles
articles : list
articles = [{"Code" : "C01", "Description" : "Pack de coca", "Prix"  : 5},
            {"Code" : "C02", "Description" : "Kilo de pdt", "Prix"  : 1},
            {"Code" : "C03", "Description" : "Pack de Biscotte", "Prix"  : 2},
            {"Code" : "C04", "Description" : "Café soluble", "Prix"  : 3},
            {"Code" : "C05", "Description" : "Crakers", "Prix"  : 4}]

# Définition des variables
TVA : float = 0.01
Total_TVA : float = 0.0
Total_HT : float = 0.0
Total_articles : float = 0.0
Total_final : float = 0.0

num_ticket : str = "2200"
Date : str = ""


# Fonction Date
def Date() -> str : 
    """Fonction qui récupère la date.

    Returns:
        str: Date au format JJ/MM/YYYY
    """
    date : str = datetime.now()     # Récupère la date à l'instant T
    Date = date.strftime("%d/%m/%Y")    # Mise au format JJ/MM/YYYY
    return Date     # Affectation de cette valeur à la variable Date
