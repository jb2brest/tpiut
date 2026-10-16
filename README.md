# Système d'édition de ticket de caisse

Ce projet est un script Python permettant de générer un ticket de caisse à partir d'une commande passée dans le terminal.

## Lancement de l'application
Assurez-vous d'avoir Python installé. Ouvrez un terminal et exécutez le script `main.py` en lui passant 3 arguments entre guillemets :
1. Le nom du magasin
2. Le nom du caissier
3. La liste des articles commandés, séparés par un pipe `|`, sous le format `CodeArticle:Quantité`.

**Exemple d'utilisation :**
```bash
python3 main.py "BUT Market" "Louise" "C01:1|C02:3|C03:4"
```

## Fonctionnement
Le script récupère les arguments via `sys.argv`. Il découpe ensuite la chaîne des articles pour isoler chaque code et sa quantité. Il cherche ces données dans un catalogue pour retrouver la description et le prix HT. 

Il calcule ensuite :
- Le total HT par article (Prix HT * Quantité)
- Le total HT global
- Le montant de la TVA (fixée à 10%)
- Le total TTC

Enfin, il affiche le ticket dans la console comme pour l'exmple donné.

## Ajout de produits
Pour ajouter un nouveau produit au catalogue, il suffit d'ouvrir le fichier `main.py` et d'ajouter une ligne dans le dictionnaire `catalogue` situé au début du fichier. 

Respectez cette syntaxe :
`"Code": {"desc": "Description du produit", "prix": Prix_HT_en_chiffre}`