"""
============
main.py
============

***************
History
***************

- 02/10/2024, Alexis P.: Gestion des articles
- 02/10/2024, Malo J.: Impression des tickets

***************
Description
***************
Script for creating Receipts and managing items

***************
Usage
***************
usage: main.py [-h] (-a | -r | -l | -t) [-c CODE_ARTICLE] [-d DESCRIPTION] [-p PRICE_HT] [-n NAME] [-m MARCKET] [-i ITEMS]

options:
  -h, --help            show this help message and exit
  -a, --add             Add an item
  -r, --remove          Remove an item
  -l, --list            List all items
  -t, --ticket          Print a ticket
  -c CODE_ARTICLE, --code_article CODE_ARTICLE
                        Code article
  -d DESCRIPTION, --description DESCRIPTION
                        Description
  -p PRICE_HT, --price-ht PRICE_HT
                        Price HT
  -n NAME, --name NAME  Name of the person
  -m MARCKET, --marcket MARCKET
                        Name of the marcket
  -i ITEMS, --items ITEMS
                        Items
"""
# ===== Imports =====
# == Standard Imports ==
from os import path
from json import load, dump
from argparse import ArgumentParser, Namespace
from datetime import datetime

# == Third-Party Imports ==


# == Local Imports ==


# ===== Constant =====
with open('ticket_number.txt', 'r', encoding='utf-8') as ticket_file:
    nb_ticket = ticket_file.read()

# ===== Functions =====
def parse_arguments() -> Namespace:
    """Parse the command line arguments
    """
    parser: ArgumentParser = ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-a', '--add', help='Add an item', action='store_true')
    group.add_argument('-r', '--remove', help='Remove an item', action='store_true')
    group.add_argument('-l', '--list', help='List all items', action='store_true')
    group.add_argument('-t', '--ticket', help='Print a ticket', action='store_true')

    parser.add_argument('-c', '--code_article', help='Code article')
    parser.add_argument('-d', '--description', help='Description')
    parser.add_argument('-p', '--price-ht', help='Price HT')
    parser.add_argument('-tva', '--tva', help='TVA')
    parser.add_argument('-w', '--weight', help='Weight of the product in kg')
    parser.add_argument('-u', '--unit', help='Unit of the product')
    parser.add_argument('-n', '--name', help='Name of the person')
    parser.add_argument('-m', '--marcket', help='Name of the marcket')
    parser.add_argument('-i', '--items', help='Items')

    return parser.parse_args()

def decrypt_product(item_manager,arg1:str)->str:
    """
    This function decrypts the strings containing the product id and the number of items into a string readable for the ticket
    arg1 => string containing the product id and the number of items C01:10|C02:2
    return => string readable for the ticket 10x Product 1 2x Product 2
    """
    products = arg1.split('|')
    products_strings = ""
    for product in products:
        product_id, product_number = product.split(':')
        item = item_manager.get_specific_item(product_id)
        products_strings += f"{product_number:<7} {item['description']:<23} {f'{item['price_ht']} €':<15} {f'{item['tva']}%':<7} {f'{round(item['price_ht'] * 1.2 * int(product_number), 2)}€':<10}\n"
    return products_strings

def calculate_total(arg1:str,arg2:'ItemManager')->tuple:
    """
    This function calculates the total of the ticket
    arg1 => string containing the product id and the number of items C01:10|C02:2
    arg2 => ItemManager object
    return => tuple of the total of the ticket (total_ht, total_tva, total)
    """
    products = arg1.split('|')
    total_ht = 0
    total_tva = 0
    for product in products:
        product_id, product_number = product.split(':')
        product = arg2.get_specific_item(product_id)
        total_ht += product['price_ht'] * int(product_number)
        total_tva += product['price_ht'] * product['tva']/100 * int(product_number)
    total = total_ht + total_tva
    return (total_ht, total_tva, total)

def print_ticket(arg1:str,arg2:str,arg3 : str,arg4 : tuple)->None:
    """
    This function prints the ticket with the given arguments
    arg1 => Name of the marcket
    arg2 => Name of the person
    arg3 => Id and Number of items
    arg4 => tuple of the total of the ticket
    """
    marcket_name :str = arg1
    person_name : str = arg2
    ticket :str = f"""{marcket_name}
Ticket numéro :{nb_ticket}

Date : {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}

Vous avez été servi par : {person_name}

NB	Desc.			HT unitaire 	TVA	Total
{arg3}
                                                Total HT : {arg4[0]}
                                                Total TVA : {arg4[1]}
                                                Total : {arg4[2]}
    """
    with open('ticket_number.txt', 'w', encoding='utf-8') as ticket_file:
        ticket_file.write(str(int(nb_ticket)+1))
    print(ticket)

# ===== Classes =====
class ItemManager:
    """Class for managing items
    """
    def __init__(self) -> None:
        """Initialize the items.json file if it doesn't exist
        """
        if not path.exists('items.json'):
            with open('items.json', 'w', encoding='utf-8') as items_file:
                items_file.write('[]')
        with open('items.json', 'r', encoding='utf-8') as items_file:
            self._items: list[dict] = load(items_file)

    def _save_items(self) -> None:
        """Save the items list to items.json
        """
        with open('items.json', 'w', encoding='utf-8') as items_file:
            dump(self._items, items_file)

    def get_items(self) -> list[dict]:
        """Get the items list

        Returns:
            list[dict]: The items list
        """
        return self._items

    def get_specific_item(self, code_article: str) -> dict:
        """Get a specific item by its code

        Args:
            code_article (str): The code of the item

        Returns:
            dict: The item
        """
        for item in self._items:
            if item['code_article'] == code_article:
                return item

    def add_item(self, item: dict) -> None:
        """Add an item to the items list

        Args:
            item (dict): The item to add
        """
        if not self.get_specific_item(item['code_article']):
            self._items.append(item)
            print(f'Added item {item["code_article"]}')
        else:
            print(f'Item {item["code_article"]} already exists')
        self._save_items()

    def remove_item(self, item: dict) -> None:
        """Remove an item from the items list
        """
        self._items.remove(item)
        self._save_items()


# ===== Main =====
def main() -> None:
    """Entry point
    """
    args: Namespace = parse_arguments()
    item_manager: ItemManager = ItemManager()

    if args.add: # Add an article
        if not args.code_article or not args.description or not args.price_ht and args.weight and args.unit and args.tva: # Verify if all arguments are present
            print('Missing arguments: code_article, description, price_ht')
            return
        item: dict = { # Creation of the item
            'code_article': args.code_article,
            'description': args.description,
            'price_ht': args.price_ht,
            'tva': args.tva,
            'weight': args.weight,
            'unit': args.unit
        }
        item_manager.add_item(item) # Add the item to the list

    elif args.remove: # Remove an article
        for item in item_manager.get_items():
            if item['code_article'] == args.code_article: # Verify if the item exists
                item_manager.remove_item(item) # Delete the item
                print(f'Removed item: {args.code_article}')
                break
        else:
            print(f'Item {args.code_article} not found')

    elif args.list: # List all articles
        print(f'{'Code article':<15} | {'Description':<30} | {'Price HT':<10} | {'TVA:':<5} | {'Weight:':<5}') # Show the header
        for item in item_manager.get_items():
            print(f'{item["code_article"]:<15} | {item["description"]:<30} | {f'{item["price_ht"]} euros':<10} | {f'{item["tva"]} %':<5} | {f'{item["weight"]} {item["unit"]}':<5}') # Show the item

    elif args.ticket: # Print a ticket
        if not args.items or not args.name or not args.marcket: # Verify if all arguments are present
            print('Missing arguments: items, name, marcket')
            return
        product = decrypt_product(item_manager,args.items)
        total = calculate_total(args.items, item_manager)
        print_ticket(args.marcket, args.name, product, total)

if __name__ == '__main__':
    main()
