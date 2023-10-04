# tpiut
TP sur la gestion de projet niveau IUT

# Utilisation du projet

Pour utiliser le programme, il faut se déplacer dans le bon dossier du programme
  cd /chemin

Pour générer un ticket de caisse, exécutez le script `G1-A1-lot1.py` avec les arguments suivants :

python3 main.py "<nom_magasin>" "<nom_caissier>" "<num_qté_articles>"

- <nom_magasin> : Le nom du magasin
- <nom_caissier> : Le nom du caissier/cassière
- <num_qté_articles> : La liste des articles au format `CXX:quantite|CXX:quantite|...

  Exemple d'utilisation : 

    - python3 main.py "But Market" "Lisa" "C01:10|C02:2"

# Ajout d'un article pour le lot1

Pour ajouter un article au programme : 
  Aller dans la fonction BUT_Market 
    - Ensuite dans la variable "info_articles"
      - Rajouter une ligne de ce type : 
    
    - "C0X": {"description": "<Nom_article>", "prix_ht": <Prix souhaités>}
    
  Exemple de création d'article : 
    
      - "C06": {"description": "Cigarette", "prix_ht": 11},

# Ajout d'un article pour le lot2
exécutez le script `G1-A1-lot2.py`

Pour ajouter un article au programme : 
  Aller dans la fonction BUT_Market 
    - Ensuite dans la variable "info_articles"
      - Rajouter une ligne de ce type : 
      
    - "C08": {"description": "<Nom_article>", "prix_ht": <Prix souhaités>, "poids_volume_unitaire": <Volume souhaités>, "tva": <tva souahités>}
    
  Exemple de création d'article : 
  
    - "C08": {"description": "shampoing    ", "prix_ht": 5.55, "poids_volume_unitaire": "500g", "tva": 10}
  
      
