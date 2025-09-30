articles:dict = {
    "CO1" : {"desc":"pack de coca","HTuni":5,"TVA":0.1},
    "CO2" : {"desc":"kilo de pdt","HTuni":1,"TVA":0.1},
    "CO3" : {"desc":"pack biscotte","HTuni":2,"TVA":0.1},
    "CO4" : {"desc":"Café soluble","HTuni":3,"TVA":0.1},
    "CO5" : {"desc":"Crakers","HTuni":4,"TVA":0.1}
}



nom_mag : int
employe :str = "Lisa"


num_tic:int = 1
date = "30/09/2025"
ticket1 : str = f"BUT Market \nTicket num : {num_tic}\n\nDate : {date}\nVous avez été desservi par {employe}\n"

ticket2 : str = ""

print (ticket1+ticket2)
