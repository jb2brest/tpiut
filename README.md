#Utilisation du programme :

Une liste d'item vous apparaît à chaque éxécution du programme.

Choisissez les items que vous souhaitez avec la syntaxe suivante :

py main.py "*<nom_du_ticket>*" "*<nom_du_serveur>*" "*<id_de_larticle>:<quantite>|<id_du_second_article_souhaité>:<quantite>*"

**Exemple :**

PS C:\Votre\path> py main.py "But Maket" "Lisa" "C01:10|C02:2" \n
Code article         Description          Prix unitaire hors taxe \n  
C01                  pack de coca         5 \n
C02                  kilo de pdt          1 \n
C03                  pack Biscotte        2 \n
C04                  Café soluble         3 \n
C05                  Crackers             4 \n

But Maket \n
Ticket numéro : 2683 \n

Date : 02/10/2024 \n

Vous avez été servi par : Lisa \n

NB       Desc.                HT unitaire     TVA      Total \n
10       pack de coca         5€            10%      55.0€ \n
2        kilo de pdt          1€            10%      2.2€ \n

                                            Total HT    52.0€  \n
                                            Total TVA   5.2€ \n
                                            Total       57.2€ \n

*NB : Vous n'êtes pas limité à 2 produits*

**Pour ajouter un produit**

Si vous voulez ajouter des produits, répondez "oui" à la question demandée

Ajouter produit au format suivant : id,desc,poids,prix_ht,tva avec les virgules :

Les arguments sont :
- id 
- description
- poids
- prix hors taxes
- TVA

**exemple**

ajouter_produit('C08','Chocolat','125g',3,20)

cela ajoutera dans la liste la dernière ligne

Code article         Description          poids/volume         Prix unitaire HT       TVA \n
C01                  pack de coca         2kg                  5                      20 % \n
C02                  kilo de pdt          1kg                  1                      10 % \n
C03                  pack Biscotte        950g                 2                      10 % \n
C04                  Café soluble         250g                 3                      10 % \n
C05                  Crackers             125g                 4                      20 % \n
C06                  Eau                  1,5L                 6                      10 % \n
C07                  Pain                 250g                 1                      10 % \n
C08                  Chocolat             125g                 3                      20 % \n
