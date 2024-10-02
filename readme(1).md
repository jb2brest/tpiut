# Documentation du programme Python main.py
Afin d'exécuter le programme suivant, il faut cette synthaxe :
```
python3 main.py "<Nom du magasin>" "<Nom du serveur>" "<Article1:nombre|Article2:nombre|...ArticleN:nombre>" 
```
L'article doit être contenu dans la liste suivante :<br>
Code article - Description - Poids ou volume unitaire - Prix HT unitaire - TVA<br>
C01 - pack de coca - 2kg - 5 - 20 %<br>
C02 - kilo de pdt - 1kg - 1 - 10 %<br>
C03 - pack Biscotte - 950g - 2 - 10 %<br>
C04 - Café soluble - 250g - 3 - 10 %<br>
C05 - Crakers - 125g - 4 - 20 %<br>
C06 - Eau - 1,5L - 6 - 10 %<br>
C07 - Pain - 250g - 1 - 10 %<br>


Si l'on souhaite faire évoluer cette liste, il faut opérer des modifications directement dans le code :<br>
A la ligne 27, rajouter dans le Tuple générale (les paranthèses générales) un sous-tuple avec la synthaxe suivante :<br>
```
("< Code_produit >", "< nom >, "< poids_unitaire >", "< prix >", "< TVA >")
```
Ligne 27, il sera aussi possible de modifier les articles déjà existants au niveau de leur TVA par exemple ou de leurs poids.

ATTENTION : Ne pas déplacer le fichier JSON, car il permet de sauvegarder le numéro du prochain ticket.