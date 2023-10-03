import datetime


def generation_ticket(ticket_number, produit: dict):
    """
    generation_ticket génère un ticket à partir des données passées en paramètre

    Args:
        produit (dict): description de la commande
    """

    # Ecriture de l'entête

    ticket: TicketGenerator = TicketGenerator()

    ticket.add_line(produit["market_name"])
    ticket.add_line(f"Ticket Numéro : {ticket_number + 1}")
    ticket.add_line(f"Date : {datetime.date.today().strftime('%d/%m/%Y')}")
    ticket.add_line(f"Vous avez été servi par : {produit['seller_name']}")

    ticket.add_product_line(
        "NB",
        "Desc",
        "Pds/vol. unitaire",
        "Pds/vol. total",
        "Orig.",
        "HT Unitaire",
        "TVA",
        "Total",
    )

    # Préparation des totaux
    tt_ht: float = 0.0
    tt_tva: float = 0.0
    tt_tt: float = 0.0

    # Ajout des produits dans le ticket
    for v in produit["cart"].values():
        total_tva = v["price"] * v["number"] * (1 + v["tva"])
        tt_tt += total_tva
        tt_ht += v["price"] * v["number"]
        tt_tva += (v["price"] * v["number"]) * v["tva"]

        ticket.add_product_line(
            v["number"],
            v["description"],
            f"{v['volume']:.2f}{v['volume_type']}",
            f"{v['volume'] * v['number']:.2f}{v['volume_type']}",
            v["origine"],
            f"{v['price']}€",
            f"{v['tva'] * 100:.2f}%",
            f"{float(v['price'] * v['number']):.2f}€",
        )

    # Afficher les totaux
    ticket.add_line(f"\n\nTotal HT : {tt_ht:.2f} €")
    ticket.add_line(
        f"\nTotal TVA : {tt_tva:.2f} €",
    )
    ticket.add_line(f"\nTotal : {tt_tt:.2f} €")

    return ticket_number + 1, str(ticket)


class TicketGenerator:
    def __init__(self):
        self.content = []

    def add_product_line(self, *args):
        self.content.append("\t\t\t".join(map(str, args)))

    def add_line(self, line):
        self.content.append(line)

    def __str__(self) -> str:
        return "\n".join(self.content)


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
