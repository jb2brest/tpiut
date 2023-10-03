import datetime


def generation_ticket(ticket_number, produit: dict):
    """
    generation_ticket génère un ticket à partir des données passées en paramètre

    Args:
        produit (dict): description de la commande
    """

    # Ecriture de l'entête

    ticket: list = []

    ticket.append(produit["market_name"])
    ticket.append(f"\nTicket Numéro : {ticket_number + 1}")
    ticket.append(f"\nDate : {datetime.date.today().strftime('%d/%m/%Y')}")
    ticket.append(f"\nVous avez été servi par : {produit['seller_name']}")
    ticket.append("\nNB\tDesc.\t\tHT unitaire\tTVA\tTotal")

    # Préparation des totaux
    tt_ht: float = 0.0
    tt_tva: float = 0.0
    tt_tt: float = 0.0

    # Ajout des produits dans le ticket
    for v in produit["cart"].values():
        total_tva = (10 * (v["price"] * v["number"]) / 100) + v["price"] * v["number"]
        tt_tt += total_tva
        tt_ht += v["price"] * v["number"]
        tt_tva += 10 * (v["price"] * v["number"]) / 100
        ticket.append(
            f"\n{v['number']}\t{v['description']}\t{v['price']}€\t\t10%\t{total_tva}€"
        )

    # Afficher les totaux
    ticket.append(f"\n\n\t\t\t\t\tTotal HT : {tt_ht} €")
    ticket.append(
        f"\n\t\t\t\t\tTotal TVA : {tt_tva} €",
    )
    ticket.append(f"\n\t\t\t\t\tTotal : {tt_tt} €")

    return ticket_number + 1, "".join(ticket)


if __name__ == "__main__":
    prod: dict = {
        "market_name": "But Maket",
        "seller_name": "Lisa",
        "cart": {
            "C01": {"number": 10, "description": "Pack de Coca", "price": 5},
            "C02": {"number": 2, "description": "Kilo de pdt", "price": 1},
        },
    }
    generation_ticket(prod)
