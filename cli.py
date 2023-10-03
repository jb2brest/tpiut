def parseCLI(*args) -> dict:
    """
    parseCLI Transforme une liste de args en dictionnaire

    Python3 main.py “But Maket” “Lisa” “C01:10|C02:2”

    =

    {
        "market_name": "But Maket",
        "seller_name": "Lisa",
        "cart": {
            "C01": 10,
            "CO2": 2,
        }
    }

    Returns:
        dict: representation des arguments du CLI
    """

    products: dict = {}
    for prod in args[3].split("|"):
        c, v = prod.split(":")
        products[c] = int(v)

    return {"market_name": args[1], "seller_name": args[2], "cart": products}


if __name__ == "__main__":
    from sys import argv

    print(parseCLI(*argv))
