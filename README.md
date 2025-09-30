# BUT3-A2-CHATEAU-BAGOT

## Programme d'édition de ticket de caisse

### Description :
Ceci est un programme permettant de générer un ticket de caisse en fonction des articles qu'on veut commander et leur quantité à partir d'une base de données pré-enrégistrée.

### Utilisation du programme :
Il est avant tout nécessaire que Python soit installé sur le système.

Une fois que cela est bon, éxecutez le fichier ___main.py___ via la ligne de commande suivante :

```python
python main.py "[Tableau des articles déjà pré-enregistré]" "[Nom du Magasin]" "[Nom du caissier]" "[code article]:[quantité]|[code article suivante]:[quantité]"
```

Vous pouvez toujours précisez le nom du magasin en 1er paramètre et le nom du caissier en 2ème. Pour la liste des produits vous déclarer en premier le code de l'article ainsi que la quantité souhaitée en les séparants de deux points ***":"*** . Vous pouvez rajouter autant d'articles que souhaités en les séparant avec un ***" | "*** (pipe (AltGr + 6))

Vous devriez alors avoir un ticket de caisse complet avec la liste de vos articles et les différents totaux.

***Tableau des articles déjà pré-enregistré :***

| Code article | Description  | Prix HT unitaire | TVA |
|--------------|--------------|------------------|-----|
|C01           | pack de coca | 5                | 20% |
|C02           | kilo de pdt  | 1                | 10% |
|C03           | pack Biscotte| 2                | 10% |

Exemple d'exécution du code :

```console
python main.py "BUT MARKET" "Guenael" "C01:1|C02:3|C03:40"
BUT MARKET
Ticket numéro: 2200
Date: 04/10/2023
Vous avez été servi par: Guenael
NB  Desc.                  HT unitaire  TVA   Total    
10   pack de coca              5           10%    55.0   
1   kilo de pdt                1           10%    1.1    
5   pack Biscotte              2           10%    11
Total HT: 61€
Total TVA: 6.1€
Total: 66.6€
```