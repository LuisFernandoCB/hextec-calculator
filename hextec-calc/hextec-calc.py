import math
  
  
jogadores = {
     "Akshan":{
          "Vida":, 
          "Classe de Armadura":13,
          "Força":19,
          "Destreza":30,
          "Constituição":21,
          "Inteligência":30,
          "Sabedoria":16,
          "Carisma":21,
          }, 
     "Lux":{
      "Vida" : ,  
         "Classe de Armadura": 13,
         "Força":15,  
         "Destreza":18,  
         "Constituição":20,  
         "Inteligência":22,  
         "Sabedoria":22,  
         "Carisma":14,  
     }, 
     "ogaiH": { 
         "Vida" :,  
         "Classe de Armadura": 13,  
         "Força":12,  
         "Destreza":24,  
         "Constituição":18,  
         "Inteligência":12,  
         "Sabedoria":12,  
         "Carisma":16,  
     }, 
     "Sett": { 
         "Vida" :,  
         "Classe de Armadura": 13,  
         "Força":16,  
         "Destreza":24,  
         "Constituição":18,  
         "Inteligência":12,  
         "Sabedoria":12,  
         "Carisma":16,  
     }, 
     "Vayne": { 
         "Vida" :,  
         "Classe de Armadura": 10,  
         "Força":14,  
         "Destreza":24,  
         "Constituição":18,  
         "Inteligência":12,  
         "Sabedoria":12,  
         "Carisma":16,  
     }, 
     "Yasuo": { 
         "Vida" :,  
         "Classe deZArmadura": 10,  
         "Força":14,  
         "Destreza":24,  
         "Constituição":18,  
         "Inteligência":12,  
         "Sabedoria":12,  
         "Carisma":16,  
     }, 
     "Jinx": { 
         "Vida" :,  
         "Classe de Armadura": 10,  
         "Força": 20,
         "Destreza":24,  
         "Constituição":18,  
         "Inteligência":12,  
         "Sabedoria":12,  
         "Carisma":14,  
     }
 }  
 
for up in jogadores:
     print(up)
  
 habilidades = { 
     "Akshan": { 
         "Q": math.floor((jogadores["Akshan"]["Destreza"]-10)/2/2),  
     } 
 }  
  
 modificadores = {  
     "Akshan": [  
         math.floor((jogadores["Akshan"]["Força"]-10)/2/2),  
         math.floor((jogadores["Akshan"]["Destreza"]-10)/2/2),  
         math.floor((jogadores["Akshan"]["Constituição"]-10)/2/2),  
         math.floor((jogadores["Akshan"]["Inteligência"]-10)/2/2),  
         math.floor((jogadores["Akshan"]["Sabedoria"]-10)/2/2),  
         math.floor((jogadores["Akshan"]["Carisma"]-10)/2/2)  
     ]  
 }  
  
 
 '''for c in modificadores["Akshan"]:  
     print(c)
      
  
 print(habilidades["Akshan"]["Q"])'''
