# Readme Utilisation du progamme de ticket de caisse 
Contexte : Création d'un système d'édition de tickets de caisse à destination de commerces.

# Fonctionnement 
## Fonctionnalités
### Depuis l'interface 
- Ajouter des articles avec leur quantité 
- Ajouter le nom de la caissière 
- Ajouter le nom du magasin
### Affichage
- Afficher les informations rentrées depuis l'interface
- Affichage des informations + du prix total 

## Saisie des informations par l'utilisateur
On utilise le programme de génération de ticket de caisse en ligne de commande via le service Python3 le document "main.py" contient le programme de génération de tickets de caisse suivi du nom du magasin entre guillemets, de la caissier.e puis de.s article.s achetés ("Code:Nombre d'Article|Code:Nombre d'Article|...").

Exemple : Python3 main.py “But Maket” “Lisa” “C01:10|C02:2”

# Précautions et indications
A NE PAS FAIRE
  - Ne pas oublier de saisir le nom du magasin, celui de la caissier.e puis de.s article.s achetés lors du lancement du programme
  - Pour l'écriture des articles dans la commande : "Code:Nombre d'Article|Code:Nombre d'Article|..."
  - Ne pas modifier le programme principal "main.py"

