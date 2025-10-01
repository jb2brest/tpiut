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
- Les produits, la quantité, le prix unitaire, la TVA et le prix total.
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
But Market
Ticket numéro : 2200

Date : 01/10/2025

Vous avez été servi par : Lisa

NB  Desc.              HT unitaire TVA Total
10  Pack de BZHCola    5€          10% 55.0€
2   Kilo de PDT        1€          10% 2.2€

                      Total HT 52€
                      Total TVA 5.2€
                      Total 57.2€
```

---

## Listes des produits 
| Code | Description          | Prix unitaire (€) |  
|------|----------------------|-------------------|  
| C01  | Pack de BZHCola      | 5 € |  
| C02  | Kilo de PDT          | 1 € |  
| C03  | Pack de Biscotte     | 2 € |  
| C04  | Café soluble         | 3 € |  
| C05  | Crackers             | 4 € |  

Pour rajouter un article, il faut rajouter une ligne dans "article_disponnible" avec le même format que les précédents produits : 

```
articles_disponibles = {
        "C01": ("Pack de BZHCola", 5),
        "C02": ("Kilo de PDT", 1),
        "C03": ("Pack de Biscotte", 2),
        "C04": ("Café soluble", 3),
        "C05": ("Crackers", 4)
    }
```

---

##  GitHub  
- Repository : [Projet sur GitHub](https://github.com/jb2brest/tpiut.git)  
- Branche : **2025-Lannion-GPB1-ALMAIRAC-GRALL**  

