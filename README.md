#Utilisation du programme :

Une liste d'item vous apparaît à chaque éxécution du programme.

Choisissez les items que vous souhaitez avec la syntaxe suivante :

py main.py "*<nom_du_ticket>*" "*<nom_du_serveur>*" "*<id_de_larticle>:<quantite>|<id_du_second_article_souhaité>:<quantite>*"

**Exemple :**

PS C:\Votre\path> py main.py "But Maket" "Lisa" "C01:10|C02:2"
Code article         Description          Prix unitaire hors taxe  
C01                  pack de coca         5
C02                  kilo de pdt          1
C03                  pack Biscotte        2
C04                  Café soluble         3
C05                  Crackers             4

But Maket
Ticket numéro : 2683

Date : 02/10/2024

Vous avez été servi par : Lisa

NB       Desc.                HT unitaire     TVA      Total
10       pack de coca         5€            10%      55.0€
2        kilo de pdt          1€            10%      2.2€

                                            Total HT    52.0€
                                            Total TVA   5.2€
                                            Total       57.2€

*NB : Vous n'êtes pas limité à 2 produits*

**Pour ajouter un produit**

Appelez la fonction ajouter_produits dans un terminal avec les arguments ci-dessous
Les arguments sont :
- id 
- description
- poids
- prix hors taxes
- TVA

**exemple**

ajouter_produit('C08','Chocolat',125g,3,20)

cela ajoutera dans la liste la dernière ligne

Code article         Description          poids/volume         Prix unitaire HT       TVA
C01                  pack de coca         2kg                  5                      20 %
C02                  kilo de pdt          1kg                  1                      10 %
C03                  pack Biscotte        950g                 2                      10 %
C04                  Café soluble         250g                 3                      10 %
C05                  Crackers             125g                 4                      20 %
C06                  Eau                  1,5L                 6                      10 %
C07                  Pain                 250g                 1                      10 %
C08                  Chocolat             125g                 3                      20 %
