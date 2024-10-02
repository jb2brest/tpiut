import sys, csv
from typing import List, Dict
from datetime import date

# Fonctions

def ParseArgs(arguments: list) -> tuple:
	"""Fonction qui retourne un tuple avec le nom du magasin, le nom de la caisière et la quantité de chaque item
	@args: arguments: list -> La liste des arguments
	@return: tuple -> un tuple avec le nom du magasin, le nom de la caisière et la quantité de chaque item
	"""
	# Initialisation des variables
	magasin: str = ""
	caisiere: str = ""
	liste_produits: List[str] = []
	dict_produits: Dict[str] = {}
	error: bool = False

	if len(arguments) < 3:
		# Contrôle du nombre d'arguments dans la saisie utiliisateur
		error = True
	else:
		try:
			magasin = arguments[1]
			caisiere = arguments[2]
			liste_produits = str(arguments[3]).split("|")
		except IndexError as e:
			error = True

		try:
			dict_produits = {}
			for item in liste_produits:
				reference = str(item).split(":")[0]
				quantite = str(item).split(":")[1]
				if reference == "" or quantite == "":
					error = True
				dict_produits[reference] = quantite
		except IndexError as e:
			error = True

	return error, magasin, caisiere, dict_produits


def Visuel(market_name: str, cashier: str, basket: dict, catalogue: dict, num_ticket: int) -> None:
	"""Méthode Visuel qui permet d'afficher dans la console le ticket de caisse. Elle affiche les différentes informations du magasin et calcul le total.
	Parametres : market_name(str)   : Nom du magasin.
				 cashier(str)		: Nom du caissier.
				 basket(dict)		: Panier du client. Dico de référence produit(clé) et de leur quantitié(valeur).
				 catalogue(dict)	: Liste des items à vendre.
	"""
	# Initialisation des variables
	total_HT: float = 0
	prix_TVA: float = 0
	total_TVA: float = 0
	prix: float = 0
	prix_unitaire: float = 0
	total: float = 0
	poids_unitaire: float = 0
	unite_poid: str = "kg"

	# Vérification des types de variable
	assert type(market_name) == str, "Le nom du magasin doit être une chaine de caractère."
	assert type(cashier) == str, "Le nom du caisser doit être une chaine de caractère."
	assert type(basket) == dict, "Le panier doit être un dictionnaire."

	# Création du ticket
	print("______________________________________________________")
	print(f"| {market_name}") # Affichage du nom de magasin
	print("| Ticket numéro :", num_ticket) # Affichage du numéro de magasin
	print("|")
	print(f"| Date : {date.today()}") # Affichage de la date
	print("|")
	print(f"| Vous avez été servi par : {cashier}") # Affichage du nom du caissier
	print("|")
	print("| NB		Desc.	        Pds/vol. unitaire   Pds/vol. total	HT unitaire		TVA		Total") # Affichage de l'en-tête du tableau
	for key in basket.keys() :
		prix_unitaire = float(catalogue[key][1]) # Prix unitaire du produit
		prix_TVA = (prix_unitaire * float(catalogue[key][2])) # TVA du produit
		quantity = float(basket[key]) # Quantité 
		prix = (quantity * prix_unitaire) + (prix_TVA * quantity)# Prix
		poids_unitaire = float(catalogue[key][3])
		unite_poids = catalogue[key][4]
		print(f"| {int(quantity)}		{catalogue[key][0]}	{poids_unitaire}{unite_poids}	            {poids_unitaire*quantity}{unite_poids}	        {prix_unitaire}		        {float(catalogue[key][2])*100}%		{prix}€")
		total_TVA += (prix_TVA * quantity)
		total_HT += (prix_unitaire * quantity)
	# Affichage des totaux
	total = total_HT + total_TVA
	print("|")
	print(f"| 								                        Total HT	{total_HT}€")
	print(f"| 								                        Total TVA	{total_TVA}€")
	print(f"| 								                        Total		{total}€")
	print("______________________________________________________")




# Déclaration des variables
USAGE: str
items: dict
magasin: str
caisiere: str
dict_produits: dict
nb_ticket: int
not_such_item_error: bool

# Définition des variables
items = {}
with open('data/produits.csv', newline='\n', encoding="utf-8") as csvfile:
	# Boucle pour récupérer tout les produits dans le fichier csv
	spamreader = csv.reader(csvfile, delimiter=',')
	for row in spamreader:
		nom = row[0] # Nom du produit
		reference = row[1] # Référence du produit
		prix = row[2] # Prix du produit
		tva = row[3]
		poids = row[4]
		unite_poids = row[5]

		if reference in items.keys():
			print(f"WARNING: La même référence est présente au moins deux fois. Le produit {nom} n'a donc pas été pris en compte.")
		else:
			items[reference] = [nom, prix, tva, poids, unite_poids]
# Récupération du numéro de ticket			
try :
	with open('data/nb_ticket', 'r') as file:
		nb_ticket = int(file.readline(1)) + 1
except : # Si le fichier n'existe pas on l'ajoute
	nb_ticket = 1
	with open('data/nb_ticket', 'x') as file:
		file.write(str(nb_ticket))

# Récupération des paramètres
USAGE = "Utilisation: python main.py [NOM DU MAGASIN] [CAISIERE] [REF:NOMBRE|REF:NOMBRE|...]"
arguments = sys.argv
not_such_item_error = False

# Contrôle de la saisie et retour des variables
error, magasin, caisiere, dict_produits = ParseArgs(arguments=arguments)

if not error:
	for key in dict_produits.keys():
		if key not in items.keys():
			not_such_item_error = True
			print(f"ERREUR: Identifiant {key} inexistant dans la base de données CSV.")

	if not not_such_item_error:
		Visuel(market_name=magasin, cashier=caisiere, basket=dict_produits, catalogue=items, num_ticket=nb_ticket)

    # Incrémentation du numéro de ticket
	with open('data/nb_ticket', 'w') as file:
		file.write(str(nb_ticket))
else:
	print(USAGE)