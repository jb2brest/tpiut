import datetime as dt
current_date = dt.date.today()
current_date = current_date.strftime("%d/%m/%Y")

def Entete(entreprise,nticket,nom): #fonction pour la mise en place de l'entete
    titre : str =  entreprise #variable pour afficher BUT Market
    n_ticket : str = nticket #variable pour afficher le numéros du ticket
    date_du_jour = current_date #variable pour afficher la date du jour
    servi = nom #variable pour afficher le nom de la personne qui à servi
    list =  [titre,n_ticket, date_du_jour,nom,servi] #list de toute les variables
    return list #renvoie la liste



