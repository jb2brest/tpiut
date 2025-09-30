# GP3-A2-Picard-Gimbert
## Programme python création de ticket de caisse

### Description du programme :
Le programme python permettant de générer un ticket de caisse en fonction des articles qu'on a commander, et leur quantité, à partir d'une liste pré-définis.

---

### Utilisation du programme :
En  ligne de commande exécuter le fichier main.py, comme ci-dessous.

```python
python main.py "[Nom du Magasin]" "[Nom du caissier]" "[code article]:[quantité]|[code article suivante]:[quantité]"
```

Pour la liste des articles, vous déclarer en premier le code de l'article ainsi que la quantité souhaitée en les séparants de deux points ":" . Vous pouvez rajouter autant d'articles que souhaités en les séparant avec un "|"

Une fois la commande executé, vous devriez avoir un ticket de caisse complet avec la liste de vos articles et les différents prix (HT,TVA, Total).

Exemple de résultat lorqu'on éxecute le code :

```console
python main.py "BUT MARKET" "ethan" "C01:1|C02:3|C03:4"
BUT MARKET
Ticket numéro: 1
Date: 04-10-2025
Vous avez été servi par: ethan

NB	Desc.			Poids/volume unitaire Poids/volume total	HT unitaire 	TVA	Total
1 	pack de coca	 		2kg	            2kg		            5€		 20%       6€
3	kilo de pdt		        1kg	            3kg		            1€		 10%     3,3€
4	pack Biscotte                   950                 3,8kg		    2€		 10%	 8,8€

Total HT	16€
Total TVA	2,1€
Total 		18.1€
```

---

### Ajout d'une liste au programme :

Cette section ci-dessous concerne les listes déjà présentes dans le programme python.

```python
# Initialise le dictionaire Article
ajout_article("C01","pack de coca",2,"kg",5,20,"Lituanie")
ajout_article("C02","kilo de pdt",1,"kg",1,10,"Espagne")
ajout_article("C03","pack Biscotte",950,"g",2,10,"France")
ajout_article("C04","Café soluble",250,"g",3,10,"Roumanie")
ajout_article("C05","Crakers",125,"g",4,20,"Angleterre")
ajout_article("C06","Eau\t",1.5,"L",6,10,"Suisse")
ajout_article("C07","Pain\t",250,"g",1,10,"France")
```

Si on veut ajouter un article il suffit juste de faire un copier coller d'une des lignes et de modifier les informations qu'on veut.
Par exemple, voici ci-dessous le résultat d'une ligne qu'on veut ajouter

```python
ajout_article("C08","Cidre\t",0.75,"L",4.2,10,"France")
```

Le résultat suite à l'ajout de la ligne

```python
# Initialise le dictionaire Article
ajout_article("C01","pack de coca",2,"kg",5,20,"Lituanie")
ajout_article("C02","kilo de pdt",1,"kg",1,10,"Espagne")
ajout_article("C03","pack Biscotte",950,"g",2,10,"France")
ajout_article("C04","Café soluble",250,"g",3,10,"Roumanie")
ajout_article("C05","Crakers",125,"g",4,20,"Angleterre")
ajout_article("C06","Eau\t",1.5,"L",6,10,"Suisse")
ajout_article("C07","Pain\t",250,"g",1,10,"France")
ajout_article("C08","Cidre\t",0.75,"L",4.2,10,"France")
```