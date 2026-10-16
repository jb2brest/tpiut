# Projet Générateur de Ticket de Caisse – DENAIS & JEGO (Version 2)

## Description

L'objectif de ce projet Python est de générer dynamiquement un **ticket de caisse** détaillé depuis un terminal. Le programme édite un reçu authentique comprenant les informations générales (nom du magasin, date de transaction, identifiant du ticket, serveur) ainsi que l'inventaire précis des articles. Cette deuxième version intègre désormais la gestion des **quantités (poids/volume à l'unité et au total) et l'application de taux de TVA variables**. Le bas du ticket propose un bilan financier clair (**totaux HT, TVA et TTC**) avec des montants parfaitement alignés.

## Auteurs

Maxime DENAIS \
Baptiste JEGO \
3A2

## Prérequis

- Assurez-vous d'avoir **Python 3.x** d'installé sur votre machine.
- Le système gère lui-même l'incrémentation des numéros de ticket : en l'absence du fichier `compteur_ticket.txt`, le programme le crée automatiquement lors de sa première exécution.

## Lancement du programme

### Commande générale

```bash
python3 DENAIS-JEGO_mainV2.py "Nom Magasin" "Nom Caissier" "ListeProduits"
```

### Format de la liste de produits

Chaque article doit être renseigné en associant sa référence et la quantité désirée, séparées par deux-points : `Cxx:nb`.

Si votre panier contient plusieurs références, chainez-les simplement en utilisant le caractère `|` comme délimiteur.

Exemple :

```bash
python3 DENAIS-JEGO_mainV2.py "Super U" "Jean" "C01:2|C02:3|C06:1"
```

## Fonctionnement du programme

1. **Génération automatique du ticket**
   Sous réserve de paramètres valides, le script édite sur-le-champ un reçu textuel entouré d'un cadre soigné. Le contenu y est organisé méthodiquement, avec un alignement à droite pour les valeurs financières.

2. **Conversion dynamique des unités**
   Le programme détermine automatiquement la quantité totale par article. Pour plus de lisibilité, tout poids cumulé atteignant ou dépassant les 1000 grammes (`g`) bascule de lui-même en affichage kilogrammes (`kg`).

3. **Mise à jour du catalogue**
   La base de données des articles est facilement modifiable. Pour rajouter un produit en rayon, éditez simplement le fichier `DENAIS-JEGO_mainV2.py` en insérant une nouvelle ligne dans le dictionnaire `CATALOGUE`.
   Exemple :
```python
"C08": {"description": "Chocolat", "poids_vol": 200, "unite": "g", "prix_ht": 2.5, "tva": 0.20}
```

4. **Prévention des erreurs**
   Le script vérifie la conformité de chaque saisie. Face à un formatage incorrect, une quantité illogique (texte ou valeur négative), un produit non référencé ou un panier vide, **le processus s'interrompt instantanément**. Un message d'alerte s'affiche pour vous guider, bloquant l'impression d'un ticket erroné.

5. **Arrêt autonome**
   Dès que le ticket est imprimé dans le terminal (ou qu'une erreur critique est détectée), l'application se clôture de façon autonome. Vous n'avez pas besoin d'intervenir pour fermer le programme.

## Articles disponibles

| Code | Description | Poids/Vol unitaire | Prix HT | TVA |
| :--- | :--- | :--- | :--- | :--- |
| **C01** | pack de coca | 2 kg | 5.0 € | 20% |
| **C02** | kilo de pdt | 1 kg | 1.0 € | 10% |
| **C03** | pack Biscotte | 950 g | 2.0 € | 10% |
| **C04** | Café soluble | 250 g | 3.0 € | 10% |
| **C05** | Crakers | 125 g | 4.0 € | 20% |
| **C06** | Eau | 1.5 L | 6.0 € | 10% |
| **C07** | Pain | 250 g | 1.0 € | 10% |