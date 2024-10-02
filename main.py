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
from argparse import ArgumentParser

# == Third-Party Imports ==


# == Local Imports ==


# ===== Constant =====


# ===== Functions =====
def parse_arguments() -> None:
    """Parse the command line arguments
    """
    parser: ArgumentParser = ArgumentParser()

    pars


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
        """
        return self._items

    def add_item(self, item: dict) -> None:
        """Add an item to the items list
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

if __name__ == '__main__':
    main()
