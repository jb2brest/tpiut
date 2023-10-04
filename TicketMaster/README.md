# BUT Market Ticket Maker

Ce programme permet de générer un ticket de caisse à l'aide des informations passées en paramètres.

Auteurs : Morvant Théo, Riou Théo


# Fichiers
Ce programme comporte 2 fichiers :
- Main.py
 - nb_tickets.txt


## Utilisation du programme

Dans un premier temps, vérifiez que python est correctement installé sur votre machine.
Le programme prends en compte 3 paramètres :

```python
python .\main.py "BUT Market" "Lisa" "C02:10|C04:6"
```
- Le premier argument ("BUT Market") est une chaîne de caractères contenant de le nom du magasin
- Le deuxième argument ("Lisa") contient de le nom de l'hôte de caisse.
- Le troisième argument ("C01:10|C04:6") représente la liste des articles et leur quantité. Les articles sont répertoriés de la manière suivante :

```
Code article     Description       Prix unitaire HT
C01              Pack de coca      5 
C04              Café Soluble      3 
```

Par exemple, C01:10 correspond à 10 Packs de Coca

Une fois tout les paramètres donnés, le programme retourne un ticket de caisse :

```python
python .\main.py "BUT Market" "Lisa" "C02:10|C04:6"
BUT Market
Ticket numéro : 67

Date : 2023-10-04
Vous avez été servi par : Lisa

NB  Desc                 HT unitaire     TVA   Total
10  Kilo de pdt          1               10%   11.0
6   Café Soluble         3               10%   19.8
```

