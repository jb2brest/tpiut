# tpiut
TP sur la gestion de projet niveau IUT

# Utilisation du projet

Pour utiliser le programme, il faut se déplacer dans le bon dossier du programme
  cd /chemin

Pour générer un ticket de caisse, exécutez le script `main.py` avec les arguments suivants :

python3 main.py "<nom_magasin>" "<nom_caissier>" "<articles>"

- <nom_magasin> : Le nom du magasin.
- <nom_caissier> : Le nom du caissier/cassière.
- <articles> : La liste des articles au format `CXX:quantite|CYY:quantite|...

Exemple d'utilisation :
python3 main.py "But Market" "Lisa" "C01:10|C02:2"

# Ajout d'un article

Pour ajouter un article au programme : 
  Aller dans la fonction BUT_Market 
    -> Ensuite dans la variable "info_articles"
    Rajouter une ligne de ce type : "C0X": {"description": "<Nom article>", "prix_ht": <Prix souhaité>}
    
    Exemple de création d'article : 
      "C06": {"description": "Cigarette", "prix_ht": 11},
      
