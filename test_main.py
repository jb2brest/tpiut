"""Tests unitaires du système de ticket de caisse. Lancement : python3 -m unittest -v"""

import os
import tempfile
import unittest
from datetime import date
from decimal import Decimal

import main


class TestTicket(unittest.TestCase):

    def setUp(self):
        self.produits = main.charger_produits()

    def test_catalogue_charge(self):
        # Les 7 articles du client sont présents, avec la nouvelle TVA à 20%
        self.assertEqual(len(self.produits), 7)
        self.assertEqual(self.produits["C01"]["prix_ht"], Decimal(5))
        self.assertEqual(self.produits["C01"]["tva"], Decimal(20))
        self.assertEqual(self.produits["C05"]["tva"], Decimal(20))
        self.assertEqual(self.produits["C06"]["poids_volume"], "1,5L")

    def test_parser_panier(self):
        self.assertEqual(main.parser_panier("C01:10|C02:2"), [("C01", 10), ("C02", 2)])

    def test_exemple_client(self):
        # Nouveau ticket du client : coca à 20% de TVA -> 16 / 2,1 / 18,1
        lignes = main.calculer_lignes(main.parser_panier("C01:1|C02:3|C03:4"), self.produits)
        self.assertEqual([main.euro(l["total_ttc"]) for l in lignes], ["6€", "3,3€", "8,8€"])
        self.assertEqual([l["poids_total"] for l in lignes], ["2kg", "3kg", "3,8kg"])
        ht, tva, ttc = main.calculer_totaux(lignes)
        self.assertEqual((main.euro(ht), main.euro(tva), main.euro(ttc)), ("16€", "2,1€", "18,1€"))

    def test_poids_volume(self):
        # Lecture des unités et affichage dans l'unité la plus lisible
        self.assertEqual(main.lire_poids_volume("950g"), (Decimal(950), "g"))
        self.assertEqual(main.lire_poids_volume("1,5L"), (Decimal(1500), "ml"))
        self.assertEqual(main.poids_volume(Decimal(3800), "g"), "3,8kg")
        self.assertEqual(main.poids_volume(Decimal(250), "g"), "250g")
        self.assertEqual(main.poids_volume(Decimal(4500), "ml"), "4,5L")
        self.assertEqual(main.poids_volume(Decimal(330), "ml"), "330mL")

    def test_poids_volume_invalide(self):
        for texte in ("", "abc", "12", "3 tonnes"):
            with self.assertRaises(main.ErreurTicket):
                main.lire_poids_volume(texte)

    def test_code_inconnu(self):
        with self.assertRaises(main.ErreurTicket):
            main.calculer_lignes([("C99", 1)], self.produits)

    def test_code_en_double_regroupe(self):
        # "C01:2|c01:1" -> une seule ligne de 3 coca
        self.assertEqual(main.parser_panier("C01:2|C02:1|c01:1"), [("C01", 3), ("C02", 1)])

    def test_colonnes_alignees(self):
        # Une description longue ne doit pas décaler la colonne Total
        produits = dict(self.produits)
        produits["C99"] = {"description": "Pack de bouteilles d'eau minérale gazeuse",
                           "poids_volume": "50cl", "prix_ht": Decimal("12.99"), "tva": Decimal("5.5")}
        lignes = main.calculer_lignes([("C01", 1), ("C99", 150)], produits)
        ticket = main.generer_ticket("M", "V", 1, date.today(), lignes).splitlines()
        debut = next(i for i, l in enumerate(ticket) if l.startswith("NB"))
        tableau = ticket[debut:debut + 3]  # en-tête + 2 lignes d'articles
        debuts_total = {ligne.rindex(" ") + 1 for ligne in tableau}
        self.assertEqual(len(debuts_total), 1)

    def test_magasin_vide(self):
        self.assertEqual(main.main(["main.py", " ", "Lisa", "C01:1"]), 2)

    def test_quantite_invalide(self):
        for panier in ("C01:abc", "C01:0", "C01:-2", "C01", ""):
            with self.assertRaises(main.ErreurTicket):
                main.parser_panier(panier)

    def test_numero_incremente(self):
        with tempfile.TemporaryDirectory() as d:
            chemin = os.path.join(d, "compteur.txt")
            self.assertEqual(main.prochain_numero(chemin), 2200)
            self.assertEqual(main.prochain_numero(chemin), 2201)

    def test_ticket_contient_infos(self):
        lignes = main.calculer_lignes([("C01", 1)], self.produits)
        ticket = main.generer_ticket("BUT Market", "Lisa", 2200, date(2023, 9, 8), lignes)
        for attendu in ("BUT Market", "Ticket numéro : 2200", "Date : 08/09/2023",
                        "Vous avez été servi par : Lisa", "pack de coca"):
            self.assertIn(attendu, ticket)


if __name__ == "__main__":
    unittest.main()
