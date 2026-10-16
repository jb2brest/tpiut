# Projet Ticket de Caisse – BIRRE & PAUL

## Description
Ce projet est un script Python permettant de générer un ticket de caisse à partir d'articles saisis en ligne de commande. Le rendu final simule un reçu complet incluant l'en-tête (nom du magasin, numéro de ticket, date, caissier), le détail des produits achetés, ainsi que le calcul formaté des totaux HT, TVA et TTC. 

---

## Auteurs
Baptiste JEGO \
Maxime DENAIS \
Groupe 3A2

---

## Prérequis
Pour faire fonctionner ce programme, on doit simplement avoir Python 3.x installé. Lors de sa première exécution, il créera automatiquement un fichier `compteur_ticket.txt` s'il n'existe pas déjà. 

---

## Lancement du programme

### Commande
```bash
python3 DENAIS-JEGO_main.py "Nom Magasin" "Nom Caissier" "ListeProduits"
```

### Format de la liste de produits

Le format des produits est Code:Quantité (ex: Cxx:nb). Les entrées multiples doivent être délimitées par le caractère |.

Exemple :

```bash
python3 DENAIS-JEGO_main.py "Market IUT" "Lisa" "C01:2|C02:3"
```

## Fonctionnement du programme
1. **Génération du ticket de caisse**

Une fois le script lancé avec des paramètres valides, le ticket est généré instantanément. Le résultat s'affiche sous la forme d'un encadré soigné regroupant l'en-tête (magasin, n° de ticket, date, caissier), le détail des achats et la synthèse des totaux.

2. **Ajout d'un produit**

Pour modifier la base de données avec de nouveaux articles, il suffit d'éditer le fichier `DENAIS-JEGO_main.py` et d'ajouter des produits directement dans le dictionnaire `CATALOGUE`.
Exemple :

```python
"C06": {"description": "Brioche", "prix_ht": 2.8}
```

3. **Suppression d'un produit**

De la même manière, pour retirer un produit du système, il suffit de supprimer la ligne correspondante (sa clé et ses attributs) au sein du dictionnaire `CATALOGUE` du fichier `DENAIS-JEGO_main.py`.

4. **Annulation d'un ticket**

En cas de format de saisie incorrect, le programme interrompt la génération du ticket et affiche un message d'erreur vous rappelant l'usage attendu. Par ailleurs, si un code article n'existe pas dans le catalogue, il sera tout simplement ignoré. Enfin, si vous avez besoin de réinitialiser ou d'ajuster la numérotation, vous pouvez éditer manuellement le fichier `compteur_ticket.txt`.

5. **Fermeture du programme**

Une fois le ticket généré et affiché dans la console, le programme se ferme de lui-même. Vous n'avez aucune manipulation supplémentaire à effectuer.

## Articles disponibles

| Code | Description   | Prix HT unitaire |
| ---- | ------------- | ---------------- |
| C01  | pack de coca  | 5.0 €            |
| C02  | kilo de pdt   | 1.0 €            |
| C03  | pack Biscotte | 2.0 €            |
| C04  | Café soluble  | 3.0 €            |
| C05  | Crakers       | 4.0 €            |


## Notes

- Le fichier `compteur_ticket.txt` est utilisé pour mémoriser le dernier numéro de ticket et l’incrémenter à chaque exécution. S'il n'existe pas, il est généré.
- Le taux de TVA est fixé à 10% (`TAUX_TVA = 0.10`) pour tous les articles.
- Le formatage des prix gère l'affichage avec la virgule et le symbole € sans zéros inutiles.