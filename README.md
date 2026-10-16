# Projet programme ticket de caisse

> Ce programme permet de générer un ticket de caisse à partir d'une liste de produits déjà définie en dur dans le programme. On entre en arguments à l'exécution du programme : le nom du magasin, le/la caissier(ère) et les produits avec leur quantité. Il calcule automatiquement le prix de chaque produit avec sa quantité, applique la bonne TVA (10 % ou 20 % selon le produit), affiche le poids ou le volume des articles, et termine le ticket par le prix TTC.

**Version :** 2.0 · **Auteur :** Antoine et Thomas · **Dernière mise à jour :** 16/10/2026 · **Statut :** terminé

---

## 1. Contexte et objectifs

L'objectif du programme est de générer un ticket de caisse à partir d'un nom de magasin, d'un nom de caissier et d'une liste de produits (par code) associés à une quantité.

Le ticket affiche pour chaque produit :
- la quantité achetée ;
- la description du produit ;
- le poids ou le volume d'un article, puis le poids ou le volume total de la ligne (en g/kg pour un poids, en ml/L pour un volume) ;
- le prix HT unitaire ;
- le taux de TVA du produit ;
- le total de la ligne TTC.

En bas de ticket : total HT, total de TVA et total TTC.

## 2. Prérequis
- Matériel : un ordinateur
- Logiciels et versions : Python 3

## 3. Installation
1. Installer Python
2. Récupérer le projet sur Github :
   ```bash
   git clone -b LEFLOCH_GUERY https://github.com/jb2brest/tpiut
   ```
3. Vérifier que le fichier `compteur.txt` existe dans le même dossier que `main.py` et qu'il contient un nombre entier (par exemple `0`). C'est lui qui retient le numéro du dernier ticket : le programme le lit, ajoute 1, puis le réécrit à chaque ticket édité. S'il n'existe pas, le programme plante, et ce n'est pas notre faute.

## 4. Base de produits utilisée
```bash
+-------------------------------------------------------------------------------+
| Code Article | Description   | Prix HT unitaire | TVA | Poids/volume unitaire |
+-------------------------------------------------------------------------------+
|     C01      | Pack de coca  | 5                | 20% | 2 L                   |
|     C02      | Kg patate     | 1                | 10% | 1 kg                  |
|     C03      | Pack biscotte | 2                | 10% | 950 g                 |
|     C04      | Café soluble  | 3                | 10% | 200 g                 |
|     C05      | Crackers      | 4                | 10% | 250 g                 |
+-------------------------------------------------------------------------------+
```
Évitez d'utiliser exprès un code qui n'existe pas. On l'a prévu hein, mais vous allez juste perdre votre temps (le ticket affichera une erreur et une ligne `NONE` à 0 €).

### Ajouter un produit
Rendez-vous dans le code, dans le dictionnaire `ARTICLES` (en haut du fichier, juste sous le compteur). Vous y ajoutez le nouveau produit.
Voici le format à respecter :
```python
ARTICLES = { ...
...
"C05": ("Crackers", 4.00, 10, 250, "g"),
...
"CXX": ("NOM_PRODUIT", PRIX_PRODUIT, TVA, QUANTITE, "UNITE")
}
...
```
- `CXX` : avec XX votre numéro de produit (ou XXX, ça marche aussi).
- `NOM_PRODUIT` : le nom de votre produit. ENTRE GUILLEMETS c'est important.
- `PRIX_PRODUIT` : le prix HT de votre produit. Par exemple 42. Ici c'est sans guillemets. Si vous vous amusez à mettre autre chose, on l'a prévu aussi donc vous allez aussi perdre votre temps (et je viendrai vous toucher cette nuit).
- `TVA` : le taux de TVA en pourcentage, sans le signe `%` et sans guillemets : `10` ou `20`. Si le gouvernement change encore d'avis, c'est ici que ça se passe.
- `QUANTITE` : le poids ou le volume **d'un seul article**, exprimé en **grammes** ou en **millilitres**, sans guillemets. Par exemple `2000` pour un pack de 2 L. Pas la peine de convertir en kg ou en L, le programme s'en charge tout seul à partir de 1000.
- `"UNITE"` : `"g"` si c'est un poids, `"ml"` si c'est un volume. ENTRE GUILLEMETS, et pas d'autres valeurs (pas de `"kg"`, pas de `"cl"`, on ne rigole pas).

N'oubliez pas la virgule à la fin de la ligne, sauf pour le dernier produit.

## 5. Utilisation
Pour lancer le programme, la commande ressemble à ça :
```bash
python3 main.py "Nom_Magasin" "Prénom_caissier" "C01:41|C02:7|C05:1"
```
- 1er argument : Nom du magasin
- 2e argument : Prénom du caissier
- 3e argument : Liste de produits. Le format est `code:quantité`, chaque produit séparé par un pipe `|`. La quantité doit être un nombre entier.

Mettez bien chaque argument entre guillemets, sinon le terminal va croire que « BUT Market » est deux arguments.

### Exemple de ticket
```bash
python3 main.py "BUT Market" "Lisa" "C01:1|C02:3|C03:4"
```
```text
BUT Market
Ticket numéro 1

Date et heure : 16/10/2026 13:51:12

Vous avez été servi par Lisa
ARTICLES
NB  Desc.             Poids/volume unitaire  Poids/volume total  HT unitaire   TVA     Total
1   Pack de coca                         2L                  2L         5.0€   20%     6.00€
3   Kg patate                           1kg                 3kg         1.0€   10%     3.30€
4   Pack biscotte                      950g               3.8kg         2.0€   10%     8.80€
                                                                      Total HT        16.00€
                                                                      Total TVA        2.10€
                                                                      Total TTC       18.10€
```

## 6. Structure du projet
```text
.
├── main.py          # le programme
├── compteur.txt     # numéro du dernier ticket (ne pas toucher sinon je vous touche !)
├── test.py          # le test du catalogue et des calculs
└── README.md        # vous êtes ici
```
