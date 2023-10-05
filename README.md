# GP3-A1-TRAINI-DRÉVILLON
## Programme d'édition de ticket de caisse

### __Description :__
Ceci est un programme permettant de générer un ticket de caisse en fonction des articles qu'on veut commander et leur quantité à partir d'une base de données pré-enrégistrée.

### __Utilisation du programme :__
Il est avant tout nécessaire que Python soit installé sur le système.
Une fois que cela est bon, éxecutez le fichier ___main.py___ via la ligne de commande suivante :

```python
python main.py "[Nom du Magasin]" "[Nom du caissier]" "[code article]:[quantité]|[code article suivante]:[quantité]"
```

Vous pouvez toujours précisez le nom du magasin en 1er paramètre et le nom du caissier en 2ème. Pour la liste des produits vous déclarer en premier le code de l'article ainsi que la quantité souhaitée en les séparants de deux points __":"__ . Vous pouvez rajouter autant d'articles que souhaités en les séparant avec un __" | "__

Vous devriez alors avoir un ticket de caisse complet avec la liste de vos articles et les différents totaux.

__<u> Tableau des articles déjà pré-enregistré :</u>__

| Code article | Description  | Prix HT unitaire | TVA |
|--------------|--------------|------------------|-----|
|C01           | pack de coca | 5                | 20% |
|C02           | kilo de pdt  | 1                | 10% |
|C03           | pack Biscotte| 2                | 10% |

Exemple d'exécution du code :

```console
python main.py "BUT MARKET" "Lison" "C01:1|C02:3|C03:40"
BUT MARKET
Ticket numéro: 2200
Date: 04/10/2023
Vous avez été servi par: Lison

NB  Desc.                  HT unitaire  TVA   Total    
1   pack de coca              5           10%    5.5   
3   kilo de pdt              1           10%    3.3    
40   pack Biscotte              2           10%    88.0

Total HT: 88€
Total TVA: 8.8€
Total: 96.8€
```

### __Nouvelles fonctionnalitées :__

Nous avons rajouté au ticket le volume et le poids de chaque articles ainsi que le total. Le fonctionnement reste le même que la partie __Utilisation du programme__. Voici un exemple : 

```console
python3 .\main.py "BUT MARKET" "Lisa" "C01:1|C02:3|C03:4"
BUT MARKET
Ticket numéro: 2200
Date: 04/10/2023
Vous avez été servi par: Lisa

NB  Desc.                  Poids/volume unitaire  Poids/volume total  HT unitaire  TVA   Total
1   pack de coca                  2kg                     2kg             5€       20%    6.0€
3   kilo de pdt                   1kg                     3kg             1€       10%    3.3€
4   pas Biscotte                  950g                    3800g           2€       10%    8.8€

Total HT: 16.00€
Total TVA: 2.10€
Total: 18.10€
```
