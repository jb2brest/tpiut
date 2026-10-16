import sys
from datetime import datetime

# poids : en grammes (unite "g") ou en millilitres (unite "ml")
CATALOGUE = {
    "C01": {"nom": "pack de coca",  "prix_ht": 5.0, "tva": 20, "poids": 2000, "unite": "g"},
    "C02": {"nom": "kilo de pdt",   "prix_ht": 1.0, "tva": 10, "poids": 1000, "unite": "g"},
    "C03": {"nom": "pack Biscotte", "prix_ht": 2.0, "tva": 10, "poids": 950,  "unite": "g"},
    "C04": {"nom": "Café soluble",  "prix_ht": 3.0, "tva": 10, "poids": 250,  "unite": "g"},
    "C05": {"nom": "Crakers",       "prix_ht": 4.0, "tva": 20, "poids": 125,  "unite": "g"},
    "C06": {"nom": "Eau",           "prix_ht": 6.0, "tva": 10, "poids": 1500, "unite": "ml"},
    "C07": {"nom": "Pain",          "prix_ht": 1.0, "tva": 10, "poids": 250,  "unite": "g"},
}


def ajouter_article_catalogue(code, nom, prix_ht, tva, poids, unite):
    """Ajoute un produit au catalogue (exemple : ajouter_article_catalogue("C08", "Jus", 3.5, 10, 1000, "ml"))."""
    CATALOGUE[code] = {"nom": nom, "prix_ht": float(prix_ht), "tva": tva,
                       "poids": poids, "unite": unite}


def formater_poids(valeur, unite):
    """2000 g -> 2kg, 950 g -> 950g, 1500 ml -> 1.5L"""
    if valeur >= 1000:
        return f"{round(valeur / 1000, 3):g}{'kg' if unite == 'g' else 'L'}"
    return f"{round(valeur, 3):g}{unite}"


def euro(montant):
    return f"{round(montant, 2):g}€"


def main():
    if len(sys.argv) < 4:
        print("Erreur : arguments manquants.")
        print('Utilisation : python main.py "Magasin" "Caissier" "C01:1|C02:3"')
        sys.exit(1)

    magasin, caissier, commande = sys.argv[1], sys.argv[2], sys.argv[3]

    colonnes = [("NB", 4), ("Desc.", 15), ("Pds/vol. unitaire", 19), ("Pds/vol. total", 16),
                ("HT unitaire", 13), ("TVA", 6), ("Total", 8)]

    def ligne(valeurs):
        return "".join(f"{v:<{w}}" for v, (_, w) in zip(valeurs, colonnes)).rstrip()

    print(magasin)
    print("Ticket numéro : 2200")
    print(f"Date : {datetime.now().strftime('%d/%m/%Y')}\n")
    print(f"Vous avez été servi par : {caissier}\n")
    print(ligne([titre for titre, _ in colonnes]))

    total_ht = 0.0
    total_tva = 0.0

    for item in commande.split("|"):
        if ":" not in item:
            continue
        code, qte_str = item.split(":", 1)

        try:
            qte = int(qte_str)
        except ValueError:
            print(f"Ligne ignorée (quantité invalide) : {item}")
            continue
        if code not in CATALOGUE:
            print(f"Ligne ignorée (code inconnu) : {code}")
            continue

        a = CATALOGUE[code]
        ligne_ht = a["prix_ht"] * qte
        ligne_tva = ligne_ht * a["tva"] / 100
        total_ht += ligne_ht
        total_tva += ligne_tva

        valeurs = [qte, a["nom"],
                   formater_poids(a["poids"], a["unite"]),
                   formater_poids(a["poids"] * qte, a["unite"]),
                   euro(a["prix_ht"]), f"{a['tva']}%", euro(ligne_ht + ligne_tva)]
        print(ligne([str(v) for v in valeurs]))

    decalage = " " * sum(w for _, w in colonnes[:-3])
    print()
    print(f"{decalage}Total HT   {euro(total_ht)}")
    print(f"{decalage}Total TVA  {euro(total_tva)}")
    print(f"{decalage}Total      {euro(total_ht + total_tva)}")


if __name__ == "__main__":
    main()
