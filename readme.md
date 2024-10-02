# Documentation du programme Python main.py
Afin d'exécuter le programme suivant, il faut cette synthaxe :
```
python3 main.py "<Titre du ticket>" "<Nom du serveur>" "<Article1:nombre|Article2:nombre|...ArticleN:nombre>" 
```
L'article doit être contenu dans la liste suivante :
Code article Description Prix HT unitaire
C01     pack de coca        5
C02     kilo de pdt     1
C03     pack Biscotte       2
C04     Café soluble        3
C05     Crakers     4

Si l'on souhaite faire évoluer cette liste, il faut opérer des modifications directement dans le code :
A la ligne 27, rajouter dans le Tuple générale (les paranthèses générales) un sous-tuple avec la synthaxe suivante :
("<Code_produit>", "<"nom">, "<prix>")