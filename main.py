from random import randrange
import datetime

# Nom de l'entreprise
nom_entreprise: str = "Test"  # A changer

# Articles du client : {description: {"nb": quantité, "ht": prix HT unitaire, "tva": taux en %}}
item_list: dict = {}

# Lignes du ticket (générées avant le template)
lignes = []
total_ht = 0.0
total_tva = 0.0

# On calcule les totaux en même temps qu'on génère les lignes du ticket
for desc, data in item_list.items():
    nb, ht, tva = data["nb"], data["ht"], data["tva"]

    ligne_ht = nb * ht                  # total HT de la ligne
    ligne_tva = ligne_ht * tva / 100    # montant de TVA de la ligne
    ligne_ttc = ligne_ht + ligne_tva    # total TTC de la ligne

    total_ht += ligne_ht
    total_tva += ligne_tva

    lignes.append(f"{nb:<8}{desc:<12}{ht:>11.2f}€{tva:>8}%{ligne_ttc:>10.2f}€")

total_general = total_ht + total_tva

lignes_txt = "\n".join(lignes)

template: str = f"""\
{nom_entreprise}
Ticket numéro : {randrange(1, 10000)}

Date : {datetime.datetime.now():%d/%m/%Y %H:%M}

Vous avez été servi par : Lisa

NB      Desc.       HT Unitaire     TVA     Total
{lignes_txt}

TOTAL HT  : {total_ht:>10.2f}€
TOTAL TVA : {total_tva:>10.2f}€
TOTAL TTC : {total_general:>10.2f}€
"""

if __name__ == "__main__":
    print(template)