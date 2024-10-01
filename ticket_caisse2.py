import argparse
import os

# Chemin vers le fichier contenant le numéro de ticket
ticket_file = "numero_ticket.txt"

# Fonction pour lire le numéro de ticket à partir d'un fichier
def lire_numero_ticket():
    if os.path.exists(ticket_file):
        with open(ticket_file, "r") as f:
            return int(f.read().strip())
    return 2200  # Numéro initial si le fichier n'existe pas

# Fonction pour sauvegarder le numéro de ticket dans un fichier
def sauvegarder_numero_ticket(numero):
    with open(ticket_file, "w") as f:
        f.write(str(numero))

class TicketCaisse:
    def __init__(self, nom_magasin, nom_caissier, articles, numero_ticket):
        # Initialise les attributs de l'objet TicketCaisse
        self.nom_magasin = nom_magasin
        self.nom_caissier = nom_caissier
        self.articles = articles
        self.numero_ticket = numero_ticket

    def generer_ticket(self):
        # Entête du ticket
        print(f"{self.nom_magasin}\nTicket numéro : {self.numero_ticket}\n")
        print(f"Date : 01/10/2048\n")
        print(f"Vous avez été servi par : {self.nom_caissier}\n")

        # Tableau des articles
        print("{:<4} {:<15} {:<18} {:<18} {:<10} {:<7} {:<8}".format("NB", "Desc.", "Poids/volume unitaire", "Poids/volume total", "HT unitaire", "TVA", "Total"))
        total_ht = 0
        total_tva = 0

        for code, quantite in self.articles.items():
            # Recherche les détails de l'article par son code
            article = self.trouver_article_par_code(code)
            if article:
                desc = article['description']
                poids_unitaire = article['poids']
                ht_unitaire = article['prix_ht']
                tva = article['tva']
                origine = article['origine']
                total_article = ht_unitaire * quantite
                total_ht += total_article
                total_tva += (total_article * tva)

                poids_total = self.calculer_poids_total(poids_unitaire, quantite)

                # Imprime les détails de l'article dans le tableau
                print("{:<4} {:<15} {:<18} {:<18} {:<10} {:<7.2f}% {:<8.2f} €".format(
                    quantite, desc, poids_unitaire, poids_total, ht_unitaire, tva * 100, total_article))

        # Total HT et Total TVA
        print("\n{:<65} {:<7.2f} €".format("Total HT", total_ht))
        print("{:<65} {:<7.2f} €".format("Total TVA", total_tva))

        # Total général
        total_general = total_ht + total_tva
        print("{:<65} {:<7.2f} €".format("Total", total_general))

    def calculer_poids_total(self, poids_unitaire, quantite):
        # Extraire le nombre et l'unité du poids/volume
        if 'kg' in poids_unitaire or 'g' in poids_unitaire:
            nombre = float(poids_unitaire.replace('kg', '').replace('g', ''))
            if 'g' in poids_unitaire:
                nombre = nombre / 1000  # Conversion grammes -> kilogrammes
        elif 'L' in poids_unitaire:
            nombre = float(poids_unitaire.replace('L', ''))

        total_poids = nombre * quantite
        if 'kg' in poids_unitaire:
            return f"{total_poids}kg"
        elif 'g' in poids_unitaire:
            return f"{total_poids * 1000}g"  # Conversion inverse vers grammes si besoin
        elif 'L' in poids_unitaire:
            return f"{total_poids}L"
        else:
            return f"{total_poids}"

    def trouver_article_par_code(self, code):
        # Liste d'articles mise à jour
        articles = {
            "C01": {"description": "pack de coca", "poids": "2kg", "prix_ht": 5, "tva": 0.20, "origine": "Lituanie"},
            "C02": {"description": "kilo de pdt", "poids": "1kg", "prix_ht": 1, "tva": 0.10, "origine": "Espagne"},
            "C03": {"description": "pack Biscotte", "poids": "950g", "prix_ht": 2, "tva": 0.10, "origine": "France"},
            "C04": {"description": "Café soluble", "poids": "250g", "prix_ht": 3, "tva": 0.10, "origine": "Roumanie"},
            "C05": {"description": "Crakers", "poids": "125g", "prix_ht": 4, "tva": 0.20, "origine": "Angleterre"},
            "C06": {"description": "Eau", "poids": "1,5L", "prix_ht": 6, "tva": 0.10, "origine": "Suisse"},
            "C07": {"description": "Pain", "poids": "250g", "prix_ht": 1, "tva": 0.10, "origine": "France"},
        }

        return articles.get(code)

def analyser_articles(chaine_articles):
    articles_commandes = {}

    try:
        # Analyse de la chaîne d'articles pour créer un dictionnaire
        for item in chaine_articles.split('|'):
            code, quantite = item.split(':')

            # Valider si le code est valide
            if code not in ["C01", "C02", "C03", "C04", "C05", "C06", "C07"]:
                raise ValueError(f"Code d'article invalide : {code}")

            # Valider si la quantité est un entier valide
            quantite = int(quantite)
            if quantite <= 0:
                raise ValueError(f"La quantité pour l'article {code} doit être un entier positif.")

            articles_commandes[code] = quantite

    except ValueError as ve:
        raise ValueError(f"Erreur de format ou de valeur : {ve}")

    except Exception as e:
        raise ValueError(f"Erreur d'analyse des articles : {e}")

    return articles_commandes

def main():
    # Lire le numéro de ticket à partir du fichier
    numero_ticket = lire_numero_ticket()

    # Ajout d'un message personnalisé si aucun argument n'est fourni
    parser = argparse.ArgumentParser(description='Générer un ticket de caisse.')
    parser.add_argument('nom_magasin', type=str, nargs='?', help='Nom du magasin')
    parser.add_argument('nom_caissier', type=str, nargs='?', help='Nom du caissier')
    parser.add_argument('articles', type=str, nargs='?', help='Articles sous forme de chaîne de caractères (ex: "C01:10|C02:2")')

    args = parser.parse_args()

    # Si aucun argument n'est fourni, afficher un message d'erreur et un exemple de format correct
    if not args.nom_magasin or not args.nom_caissier or not args.articles:
        print("Erreur : Tous les paramètres doivent être fournis.")
        print('Format attendu : "python ton_script.py \'Nom du magasin\' \'Nom du caissier\' \'C01:2|C02:3\'"')
        return

    try:
        nom_magasin = args.nom_magasin
        nom_caissier = args.nom_caissier
        articles_commandes = analyser_articles(args.articles)

        # Crée une instance de TicketCaisse avec les données de la transaction
        ticket = TicketCaisse(nom_magasin, nom_caissier, articles_commandes, numero_ticket)
    
        # Génère le ticket de caisse en appelant la méthode generer_ticket
        ticket.generer_ticket()

        # Incrémente le numéro de ticket et le sauvegarde
        numero_ticket += 1
        sauvegarder_numero_ticket(numero_ticket)

    except ValueError as e:
        print(f"Erreur : {e}")
    except Exception as e:
        print(f"Une erreur inattendue s'est produite : {e}")

if __name__ == "__main__":
    main()
