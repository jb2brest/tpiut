from data import get_product
from cli import parseCLI
from sys import argv
from ticket import generation_ticket


from os import listdir


if __name__ == "__main__":
    # Récupération du CLI

    cli_data = parseCLI(*argv)

    # Mise à jour des produits avec leurs valeurs

    for product_number in cli_data["cart"]:
        marchandise = get_product(product_number)
        full_data = {
            "number": cli_data["cart"][product_number],
            "description": marchandise[1],
            "price": marchandise[2],
        }

        cli_data["cart"][product_number] = full_data

    # Génération du ticket
    number_of_ticket = len(listdir("./tickets/"))
    ticket_number, ticket_file = generation_ticket(number_of_ticket, cli_data)
    with open(f"./tickets/ticket_{ticket_number}.txt", "w", encoding="utf-8") as file:
        file.write(ticket_file)

    print(ticket_file)
