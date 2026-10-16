# Projet programme ticket de caisse

> Ce programme permet de générer un ticket de caisse d'une liste de produit déjà définie en dure dans le programme. On entre en paramètre à l'execution du programme, le nom du magasin, le/la caissier(ère) et les produit avec leur quantité. Il calcule automatiquement le prix de chaque produit avec leur quantité et calcule la TVA pour afficher à la fin du ticket le prix TTC

**Version :** 1.0 · **Auteur :** Antoine et Thomas · **Dernière mise à jour :** 16/10/2026 · **Statut :** terminé

---

## 1. Contexte et objectifs
- **Objectifs :** l'objectif est de faire fonctionnel qui s'execute avec cette commande (à ajuster) :
```bash
python3 nom_du_fichier "nom_du_magasin" "nom_du_caiser" "C01:10|C02:2"
```
avec comme sortie un truc qui resemble à ça :

![imagedelasortieàavoir](image1.webp)

## 2. Prérequis
- Matériel / environnement : Linux/Windows/MacOSX
- Logiciels et versions : Python 3.x

## 3. Installation
1. Récupérer le projet :
```bash
   git clone <url>
   cd <projet>
```
2. Installer les dépendances : `python3`
Sur Windows : "winget install python3"
Sur Linxu (Debian, Ubuntu) : "sudo apt install python3"
Sur les autres distribution Linux : débrouillé vous
Sur MaxOSX : qui utilise macos même ? 

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

## 5. Utilisation
Exemple de commande d'utilisation :
```bash
python3 main.py "carrouf" "Lise" "C01:41|C02:7|C05:1"
```

## 6. Structure du projet
```bash
projet/
├── main.py <- le code
└── README.md <- la doc à lire
```

## 7. Historique des versions
| Version | Date | Modifications |
|---------|------|---------------|
| 1.0 | 16/10/2026 | Version initiale |