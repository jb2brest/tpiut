from data import marchandise
from cli import parseCLI
from sys import argv
from ticket import generation_ticket

if __name__ == "__main__":
    # Récupération du CLI

    cli_data = parseCLI(*argv)

    # Mise à jour des produits avec leurs valeurs

    for product_number in cli_data["cart"]:
        full_data = {
            "number": cli_data["cart"][product_number],
            "description": marchandise[product_number][0],
            "price": marchandise[product_number][1],
        }

        cli_data["cart"][product_number] = full_data

    generation_ticket(cli_data)
