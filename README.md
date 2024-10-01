# Documentation du Ticket de Caisse

Ce script Python génère un ticket de caisse pour une transaction dans un magasin. Il prend en compte les articles commandés, calcule le total HT et TVA, puis génère un ticket avec tous les détails nécessaires.

## Utilisation

Suivez ces étapes pour utiliser le script :

1. Assurez-vous que vous avez Python installé sur votre système.

2. Clonez ce dépôt Git ou téléchargez le fichier `ticket_caisse.py` sur votre ordinateur.

3. Exécutez le script en utilisant la commande suivante dans votre terminal avec les arguments suivant : nom du magasin, le nom du vendeur, et les articles commandés (au format Code article: Quantité, par exemple, "C01: 10, C02: 2"),  :

```python
python ticket_caisse.py "But Market" "Lisa" "C04:4|C02:2"
```



5. Le ticket de caisse sera généré et affiché dans la console.

## Fonctionnement

Le script utilise une classe `TicketCaisse` pour gérer la création du ticket. Voici comment cela fonctionne :

- Le script demande d'abord le nom du magasin, le nom du caissier et les articles commandés à l'utilisateur.

- Il crée ensuite une instance de la classe `TicketCaisse` avec ces informations.

- La méthode `generer_ticket` de la classe calcule le total HT et TVA pour chaque article, puis affiche un ticket détaillé avec ces informations.

- Les détails des articles sont obtenus à partir de la méthode `trouver_article_par_code`, qui simule une recherche d'article basée sur un code. Dans une application réelle, cela pourrait être remplacé par une requête à une base de données ou une liste d'articles.

## Ajout de produits

Si vous souhaitez ajouter de nouveaux produits au script, vous pouvez le faire en modifiant la méthode `trouver_article_par_code` dans le fichier `ticket_caisse.py`. Ajoutez de nouvelles entrées au dictionnaire `articles` en utilisant le code de l'article comme clé et les détails de l'article comme valeur. Par exemple :

```python
articles = {
 # ...
 "C06": {"description": "Nouveau produit", "prix_ht": 10, "tva": 0.2},
 # ...
}
