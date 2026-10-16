# Création de ticket de caisse 

Ce programme vise à créé un ticket de caisse dans un terminal via un script python

Le programme utilise une liste d'articles préenregistré.

## utilisation 

### ajout d'un produit

Les articles par défaut sont sauvegardé dans un dictionnaire de dictionnaires, 

Articles par défaut : 

![articles](https://robindesbriques.fr//gesproj/uploads/images/68dcbdf8d5500_1759297016.png)

pour ajouter des article, il faut ajouter une ligne au dictionnaire "dic_article" ligne 10 : 

exemple de ligne :

```python
"#CODE": {"description": "# NOM ARTICLE", "prix HT unitaire": 000 , "tva": 0.10},
```
---
### lancement du programme

dans un terminal : 
```bash
python3 main.py "Magasin" "Vendeur" "C01:10|C0
2:2"
```
on appelle dans le fichier main en renseignant le nom de la structure qui vend les articles puis le nom du vendeur, ensuite on utilise le code des articles puis leur quantité, les articles sont séparé par des "|" :

```
"code:quantité|code:quantité"
```



