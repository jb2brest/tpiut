# Système d'édition de ticket de caisse

Ce projet est un script Python permettant de générer un ticket de caisse à partir d'une commande passée dans le terminal.

## Lancement de l'application
Assurez-vous d'avoir Python installé. Ouvrez un terminal **dans le dossier du projet** (là où se trouvent `main.py` et `articles.json`) et exécutez le script `main.py` en lui passant 3 arguments entre guillemets :
1. Le nom du magasin
2. Le nom du caissier
3. La liste des articles commandés, séparés par un pipe `|`, sous le format `CodeArticle:Quantité`.

**Exemple d'utilisation :**
```bash
python3 main.py "BUT Market" "Lisa" "C01:1|C02:3|C03:4"
```

## Fonctionnement
Le script récupère les arguments via `sys.argv`. Il découpe ensuite la chaîne des articles pour isoler chaque code et sa quantité. Il cherche ces données dans le catalogue `articles.json` pour retrouver la description, le poids ou volume, le prix HT et le taux de TVA de chaque article.

Si un code article n'existe pas ou si la commande est mal écrite, le script affiche un message d'erreur au lieu du ticket.

Il calcule ensuite :
- Le poids ou volume total par article (Poids unitaire * Quantité)
- Le total HT par article (Prix HT * Quantité)
- La TVA par article (Total HT de l'article * Taux de TVA de l'article)
- Le total TTC par article (Total HT + TVA)
- Le total HT global
- Le total TVA global (somme des TVA de chaque article)
- Le total TTC global

Enfin, il affiche le ticket dans la console comme pour l'exemple donné.

### Le poids et le volume
Chaque article possède un poids ou un volume unitaire, écrit sous forme de texte avec son unité (par exemple `"950g"`, `"2kg"` ou `"1,5L"`).

Le script sépare le nombre de l'unité, le multiplie par la quantité commandée, puis affiche le résultat dans la colonne « Poids/volume total ». Quand le total dépasse 1000 g, il est converti en kilogrammes pour rester lisible.

Exemple : 4 packs de biscottes de `950g` donnent `3,8kg`.

### Les différentes TVA
Tous les produits n'ont pas le même taux de TVA : certains sont à **10 %** et d'autres à **20 %**. Le taux est donc indiqué pour chaque article dans `articles.json`, et la TVA est calculée ligne par ligne avant d'être additionnée.

Exemple avec la commande ci-dessus :
- 1 pack de coca à 5 € avec 20 % de TVA → 1 € de TVA
- 3 kilos de pdt à 1 € avec 10 % de TVA → 0,3 € de TVA
- 4 packs de biscottes à 2 € avec 10 % de TVA → 0,8 € de TVA

Soit un total TVA de 2,1 € et un total TTC de 18,1 €.

### Le numéro de ticket
Le numéro du premier ticket est 2200. À chaque lancement, le script lit le dernier numéro utilisé dans le fichier `dernier_ticket.txt`, l'augmente de 1, puis l'enregistre. Ce fichier est créé automatiquement au premier lancement.

## Ajout de produits
Pour ajouter un nouveau produit au catalogue, il suffit d'ouvrir le fichier `articles.json` et d'ajouter une ligne. Aucune modification de `main.py` n'est nécessaire.

Respectez cette syntaxe :
`"Code": { "description": "Description du produit", "poids": "Poids avec unité", "prix_ht": Prix_HT_en_chiffre, "tva": Taux_de_TVA, "origine": "Pays d'origine" }`

Le taux de TVA s'écrit en décimal : `0.10` pour 10 % et `0.20` pour 20 %.

**Exemple :**
```json
"C08": { "description": "Lait", "poids": "1L", "prix_ht": 1.5, "tva": 0.10, "origine": "France" }
```

Attention à bien mettre une virgule à la fin de la ligne précédente, sinon le fichier ne pourra pas être lu.
