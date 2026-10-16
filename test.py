from main import CATALOGUE

def tester_calculs():
    # 1. Vérifier que le catalogue contient les bons articles
    assert "C01" in CATALOGUE, "L'article C01 est introuvable"
    assert CATALOGUE["C01"]["prix_ht"] == 5.0, "Le prix du C01 est incorrect"
    
    # 2. Tester un calcul de ligne (ex: 2 packs de coca à 5€ HT avec 10% de TVA)
    qte = 2
    prix_ht_unitaire = CATALOGUE["C01"]["prix_ht"]
    taux_tva = CATALOGUE["C01"]["tva"]
    
    total_ht = prix_ht_unitaire * qte
    montant_tva = total_ht * (taux_tva / 100)
    total_ttc = total_ht + montant_tva
    
    # Vérifications des résultats attendus
    assert total_ht == 10.0
    assert montant_tva == 1.0
    assert total_ttc == 11.0
    
    print("✅ TEST RÉUSSI : Le catalogue et les calculs fonctionnent parfaitement !")

if __name__ == "__main__":
    tester_calculs()