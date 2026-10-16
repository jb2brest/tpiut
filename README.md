# Système d'édition de ticket de caisse - Lot 1

##Présentation

Ce projet est un générateur de ticket de caisse codé en Python. Il correspond à la validation du **Lot 1** demandé par le client. 
Le script fonctionne directement en ligne de commande, calcule automatiquement la TVA et met en forme le texte pour générer un vrai ticket de caisse lisible.

**Fonctionnalités actuelles :**
- Récupération des données depuis le terminal (Nom du magasin, Vendeur, Articles).
- Calcul des montants : Total HT, TVA (10%) et Total TTC.
- Formatage visuel.

---

## 🚀 Utilisation

Le script ne nécessite aucune bibliothèque externe. 
Il s'utilise en exécutant le fichier `main.py` avec 3 arguments entre guillemets.

### Syntaxe :
```bash
python3 main.py "Nom du Magasin" "Nom du Vendeur" "ListeDesArticles"
EX : python3 main.py "Carrefour"  "Lisa" "CO1:2|CO3:4"