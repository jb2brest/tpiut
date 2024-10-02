"""
============
main.py
============

***************
License
***************

Copyright (c) 2024

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

***************
History
***************

- [Date], [Name]: [Modification]

***************
Description
***************

[Description]

***************
Usage
***************
[Usage]
"""
# ===== Imports =====
# == Standard Imports ==
from os import path
from json import load, dump
from argparse import ArgumentParser, Namespace
from datetime import date

# == Third-Party Imports ==


# == Local Imports ==


# ===== Constant =====
with open('ticket_number.txt', 'r') as ticket_file:
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
        products_strings += f"{product_number}x {item_manager.get_specific_item(product_id)}\n"
    return products_strings
def total(arg1:str,arg2:ItemManager)->tuple:
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
        total_tva += product['price_ht'] * 0.2 * int(product_number)
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

Date : {date.date()}

Vous avez été servi par : {person_name}

NB	Desc.			HT unitaire 	TVA	Total
{arg3}
                                Total HT : {arg4[0]}
                                Total TVA : {arg4[1]}
                                Total : {arg4[2]}
    """
    with open('ticket_number.txt', 'w') as ticket_file:
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
        self._items.append(item)
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
        if not args.code_article or not args.description or not args.price_ht: # Verify if all arguments are present
            print('Missing arguments: code_article, description, price_ht')
            return
        item: dict = { # Creation of the item
            'code_article': args.code_article,
            'description': args.description,
            'price_ht': args.price_ht
        }
        item_manager.add_item(item) # Add the item to the list

    elif args.remove: # Remove an article
        for item in item_manager.get_items():
            if item['code_article'] == args.code_article: # Verify if the item exists
                item_manager.remove_item(item) # Delete the item

    elif args.list: # List all articles
        print(f'{'Code article':<15} | {'Description':<30} | {'Price HT':<10}') # Show the header
        for item in item_manager.get_items():
            print(f'{item["code_article"]:<15} | {item["description"]:<30} | {item["price_ht"]:<10}') # Show the item

    elif args.ticket: # Print a ticket
        product = decrypt_product(item_manager,args.items)
        total = total(item_manager,args.items)
        print_ticket(args.marcket, args.name, product, total)

if __name__ == '__main__':
    main()
