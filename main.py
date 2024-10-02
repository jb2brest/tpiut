"""
============
main.py
============

***************
History
***************

- 02/10/2024, Alexis P.: Gestion des articles

***************
Description
***************
Script for creating Receipts and managing items

***************
Usage
***************
usage: main.py [-h] (-a | -r | -l) [-c CODE_ARTICLE] [-d DESCRIPTION] [-p PRICE_HT]

options:
  -h, --help            show this help message and exit
  -a, --add             Add an item
  -r, --remove          Remove an item
  -l, --list            List all items
  -c CODE_ARTICLE, --code_article CODE_ARTICLE
                        Code article
  -d DESCRIPTION, --description DESCRIPTION
                        Description
  -p PRICE_HT, --price-ht PRICE_HT
                        Price HT
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
nb_ticket = 0

# ===== Functions =====
def parse_arguments() -> Namespace:
    """Parse the command line arguments
    """
    parser: ArgumentParser = ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-a', '--add', help='Add an item', action='store_true')
    group.add_argument('-r', '--remove', help='Remove an item', action='store_true')
    group.add_argument('-l', '--list', help='List all items', action='store_true')

    parser.add_argument('-c', '--code_article', help='Code article')
    parser.add_argument('-d', '--description', help='Description')
    parser.add_argument('-p', '--price-ht', help='Price HT')

    return parser.parse_args()


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
                                Total HT
                                Total TVA
                                Total
    """
    print(ticket)
print_ticket("Carrefour","Jean","1x Pomme 1.5 0.2 1.8")
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

    def _get_specific_item(self, code_article: str) -> dict:
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

if __name__ == '__main__':
    main()
