# Projet programme ticket de caisse

> Ce programme permet de générer un ticket de caisse d'une liste de produit déjà définie en dur dans le programme. On entre en arguments à l'execution du programme : le nom du magasin, le/la caissier(ère) et les produit avec leur quantité. Il calcule automatiquement le prix de chaque produit avec leur quantité et calcule la TVA pour afficher à la fin du ticket le prix TTC

**Version :** 1.1 · **Auteur :** Antoine et Thomas · **Dernière mise à jour :** 16/10/2026 · **Statut :** terminé

---

## 1. Contexte et objectifs  

L'objectif du programme est de générer un ticket de caisse à partir d'un nom de magasin, de caissier et une liste de produits (par code) associés à une quantité.  

## 2. Prérequis
- Matériel : un ordinateur
- Logiciels et versions : Python 3

## 3. Installation
1. Installer Python
2. Récupérer le projet sur Github (`git clone https://github.com/jb2brest/tpiut/tree/LEFLOCH_GUERY`)

## 4. Base de produit utilisé
```bash
+-------------------------------------------------+
| Code Article | Description   | Prix HT unitaire |
+-------------------------------------------------+
|     C01      | pack de coca  | 5                |
|     C02      | kilo de pdt   | 1                |
|     C03      | pack Biscotte | 2                |
|     C04      | Café soluble  | 3                |
|     C05      | Crakers       | 4                |
+-------------------------------------------------+
```
Evitez d'utiliser exprès un code qui n'existe pas. On l'a prévu hein, mais vous allez juste perdre votre temps.

## 5. Utilisation
Pour lancer le programme, la commande ressemble à ça :
```python
python3 main.py "Nom_Magasin" "Prénom_caissier" "C01:41|C02:7|C05:1"
``` 
- 1er argument : Nom du magasin
- Deuxième argument : Prénom du caissier
- Troisième argument : Liste de produits. Le format est code:quantité, chaque produit séparé par un pipe |

## 6. Structure du projet
```bash
projet/
├── main.py <- le code
└── README.md <- la doc à lire
└── compteur.txt <- le compteur pour le numéro de ticket. à ne pas toucher sinon je viendrai vous toucher la nuit
```

## 7. Historique des versions
| Version | Date | Modifications |
|---------|------|---------------|
| 1.0 | 16/10/2026 | Version initiale |
| 1.1 | 16/10/2026 | Version boostée |