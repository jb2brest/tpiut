# GP3-A1-TRAINI-DRÉVILLON
## Programme d'édition de ticket de caisse

### __Description :__
Ceci est un programme permettant de générer un ticket de caisse en fonction des articles qu'on veut commander et leur quantité à partir d'une base de données pré-enrégistrés

### __Utilisation du programme :__
Il est avant tout nécessaire que Python soit installé sur le système.
Une fois que cela est bon, éxecutez le fichier ___main.py___ via ligne de commandes ou tout autre types d'outils graphique le permettant.

Il vous suffit alors de renseigner la code de l'article que vous souhaité ainsi que la quantité souhaitée.

Une fois que tous vos articles ont été renseignés, appuyer sur la touche __"q"__ puis __Entrée__ pour valider et afficher le Ticket final.

__<u> Tableau des articles déjà pré-enregistré :</u>__

| Code article | Description  | Prix HT unitaire | TVA |
|--------------|--------------|------------------|-----|
|C01           | pack de coca | 5                | 20% |
|C02           | kilo de pdt  | 1                | 10% |
|C03           | pack Biscotte| 2                | 10% |

Exemple d'exécution du code :

```console
Code de l'article (ou 'q' pour quitter) : C01
Quantite : 1
Code de l'article (ou 'q' pour quitter) : C02
Quantite : 3
Code de l'article (ou 'q' pour quitter) : C03
Quantite : 4
Code de l'article (ou 'q' pour quitter) : q
BUT MARKET
Ticket numéro: 2200
Date: 04/10/2023
Vous avez été servi par: Lisa

NB  Desc.                  HT unitaire  TVA   Total
1   pack de coca              5           10%    5.5
3   kilo de pdt              1           10%    3.3
4   pack Biscotte              2           10%    8.8

Total HT: 16€
Total TVA: 1.6€
Total: 17.6€
```
