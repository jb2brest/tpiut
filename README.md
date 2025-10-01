# Projet : Système d’édition de ticket de caisse  

## Informations générales  
- Sujet: Gestion de projet - Réalisation d'un système d’édition de ticket de caisse
- Formateur: Jean BERNARD
- Description: Vous allez réaliser un système d’édition de ticket de caisse qui sera de la forme suivante :
- Type d'évaluation: Binôme
- Membres de l'équipe: Alexandre Grall, Titouan Almairac

---

##  Description du projet  

L'objectif est de réaliser un programme en Python permettant de créer un ticket de caisse avec le format fourni, à partir de valeurs fournies par le client.

Le ticket contient :  
- Le nom du magasin  
- Le nom du client 
- Les produits, la quantité, le prix unitaire, la TVA, le prix total, le poids et le volume.
- Le prix total sans TVA, de la TVA et sans TVA

---

## Utilisation du programme  

### Lancement  
Exécution du programme avec la commande :  
```bash
python3 main.py "NOM_MAGASIN" "NOM_CLIENT" "ARTICLE1:NB1|ARTICLE2:NB2|..."
```

### Exemple  
```bash
python3 main.py "But Market" "Lisa" "C01:10|C02:2"
```

### Résultat attendu  
```
But Maket
Ticket numéro : 26

Date : 01/10/2025

Vous avez été servi par : Lisa

NB  Desc.              Poids/volume unitaire  Poids/volume total  HT unitaire  TVA   Total
1   pack de coca       2kg                    2.00kg              5€           20%   6.0€
10  Café soluble       250g                   2.50kg              3€           10%   33.0€

                                                            Total HT     35€
                                                            Total TVA    4.0€
                                                            Total        39.0€
```

---

## Listes des produits 
| Code | Description          | Prix unitaire (€) | Poids/Volume unitaire | Taux de TVA |
|------|----------------------|-------------------|-----------------------|-------------|
| C01  | Pack de BZHCola      | 5 €               | 2kg                   | 20%         |
| C02  | Kilo de PDT          | 1 €               | 1kg                   | 10%         |
| C03  | Pack de Biscotte     | 2 €               | 950g                  | 10%         |
| C04  | Café soluble         | 3 €               | 250g                  | 10%         |
| C05  | Crackers             | 4 €               | 125g                  | 20%         |
| C06  | Eau                  | 6 €               | 1.5L                  | 10%         |
| C07  | Pain                 | 1 €               | 250g                  | 10%         |

Pour rajouter un article, il faut rajouter une ligne dans "article_disponnible" avec le même format que les précédents produits : 


```python
articles_disponibles = {
    "C01": ("pack de coca", "2kg", 5, 0.20),
    "C02": ("kilo de pdt", "1kg", 1, 0.10),
    "C03": ("pack Biscotte", "950g", 2, 0.10),
    "C04": ("Café soluble", "250g", 3, 0.10),
    "C05": ("Crakers", "125g", 4, 0.20),
    "C06": ("Eau", "1.5L", 6, 0.10),
    "C07": ("Pain", "250g", 1, 0.10)
}
```


---

##  GitHub  
- Repository : [Projet sur GitHub](https://github.com/jb2brest/tpiut.git)  
- Branche : **2025-Lannion-GPB1-ALMAIRAC-GRALL**  



