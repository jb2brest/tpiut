import argparse

class TicketCaisse:
    def __init__(self, nom_magasin, nom_caissier, articles):
        # Initialise les attributs de l'objet TicketCaisse
        self.nom_magasin = nom_magasin
        self.nom_caissier = nom_caissier
        self.articles = articles

    def generer_ticket(self):
        # Entête du ticket
        print(f"{self.nom_magasin}\nTicket numéro : 2200\n")
        print(f"Date : 08/09/2023\n")
        print(f"Vous avez été servi par : {self.nom_caissier}\n")

        # Tableau des articles
        print("{:<4} {:<15} {:<13} {:<7} {:<8}".format("NB", "Desc.", "HT unitaire", "TVA", "Total"))
        total_ht = 0
        total_tva = 0

        for code, quantite in self.articles.items():
            # Recherche les détails de l'article par son code
            article = self.trouver_article_par_code(code)
            if article:
                desc = article['description']
                ht_unitaire = article['prix_ht']
                tva = article['tva']
                total_article = ht_unitaire * quantite
                total_ht += total_article
                total_tva += (total_article * tva)

                # Imprime les détails de l'article dans le tableau
                print("{:<4} {:<15} {:<13} {:<7.2f}% {:<8.2f} €".format(quantite, desc, ht_unitaire, tva * 100, total_article))

        # Total HT et Total TVA
        print("\n{:<30} {:<7.2f} €".format("Total HT", total_ht))
        print("{:<30} {:<7.2f} €".format("Total TVA", total_tva))

        # Total général
        total_general = total_ht + total_tva
        print("{:<30} {:<7.2f} €".format("Total", total_general))

    def trouver_article_par_code(self, code):
        # Remplacez cette fonction par une requête à une base de données ou une liste d'articles
        articles = {
            "C01": {"description": "pack de coca", "prix_ht": 5, "tva": 0.1},
            "C02": {"description": "kilo de pdt", "prix_ht": 1, "tva": 0.1},
            "C03": {"description": "pack Biscotte", "prix_ht": 2, "tva": 0.1},
            "C04": {"description": "Café soluble", "prix_ht": 3, "tva": 0.1},
            "C05": {"description": "Crakers", "prix_ht": 4, "tva": 0.1},
        }

        return articles.get(code)

def main():
    parser = argparse.ArgumentParser(description='Générer un ticket de caisse.')
    parser.add_argument('nom_magasin', type=str, help='Nom du magasin')
    parser.add_argument('nom_caissier', type=str, help='Nom du caissier')
    parser.add_argument('articles', type=str, help='Articles sous forme de chaîne de caractères (ex: "C01:10|C02:2")')

    args = parser.parse_args()
    nom_magasin = args.nom_magasin
    nom_caissier = args.nom_caissier
    articles_commandes = {}
    
    # Analyse de la chaîne d'articles pour créer un dictionnaire
    for item in args.articles.split('|'):
        code, quantite = item.split(':')
        articles_commandes[code] = int(quantite)

    # Crée une instance de TicketCaisse avec les données de la transaction
    ticket = TicketCaisse(nom_magasin, nom_caissier, articles_commandes)
    
    # Génère le ticket de caisse en appelant la méthode generer_ticket
    ticket.generer_ticket()

if __name__ == "__main__":
    main()
