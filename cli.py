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
    if len(args) < 3:
        raise Exception("usage : python3 main.py <market_name> <seller_name> <cart>")

    products: dict = {}
    for prod in args[3].split("|"):
        c, v = prod.split(":")
        products[c] = int(v)

    return {"market_name": args[1], "seller_name": args[2], "cart": products}


assert parseCLI("main.py", "MARKET", "LISA", "C01:1|C02:2") == {
    "market_name": "MARKET",
    "seller_name": "LISA",
    "cart": {"C01": 1, "C02": 2},
}, "Comportement du parseur FAUX"

if __name__ == "__main__":
    from sys import argv

    print(parseCLI(*argv))
