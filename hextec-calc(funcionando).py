import math

#fazer um contador de rodadas dano por rodada
#deu merda, pq pra fazer a tabela de jogadores vc vai se fuder pra mostrar cada jogador, vai ter que refatorar tudo, boa sorte KKKKKKKKKKKKKKKKK

def cls():
    print("\n"*130)

jogadores = {  
         "Akshan": {
             "Vida": 00,
             "Classe de Armadura": 13,
             "Força": 19,
             "Destreza": 30,
             "Constituição": 21,
             "Inteligencia": 30,
             "Sabedoria": 16,
             "Carisma": 21,
             },
         "Lux": {
             "Vida": 00,
             "Classe de Armadura": 12,
             "Força": 15,
             "Destreza": 18,
             "Constituição": 20,
             "Inteligencia": 22,
             "Sabedoria": 22,
             "Carisma": 14,
             },
         "I.A.R.A": {
             "Vida": 00,
             "Classe de Armadura": 13,
             "Força": 14,
             "Destreza": 12,
             "Constituição": 18,
             "Inteligencia": 24,
             "Sabedoria": 24,
             "Carisma": 16,
             },
         "Sett": {
             "Vida": 00,
             "Classe de Armadura": 13,
             "Força": 16,
             "Destreza": 24,
             "Constituição": 18,
             "Inteligencia": 12,
             "Sabedoria": 12,
             "Carisma": 16,
             },
         "Vayne": {
             "Vida": 00,
             "Classe de Armadura": 13,
             "Força": 14,
             "Destreza": 24,
             "Constituição": 18,
             "Inteligencia": 12,
             "Sabedoria": 12,
             "Carisma": 16,
             },
         "Yasuo": {
             "Vida": 00,
             "Classe de Armadura": 13,
             "Força": 14,
             "Destreza": 24,
             "Constituição": 18,
             "Inteligencia": 12,
             "Sabedoria": 12,
             "Carisma": 16,
             },
         "Jinx": {
             "Vida": 00,
             "Classe de Armadura": 13,
             "Força": 20,
             "Destreza": 24,
             "Constituição": 18,
             "Inteligencia": 12,
             "Sabedoria": 12,
             "Carisma": 14,
             },
}

modificadores = {
    "Akshan": {
        "for": math.floor((jogadores["Akshan"]["Força"]-10)/2/2),
        "des": math.floor((jogadores["Akshan"]["Destreza"]-10)/2/2),
        "con": math.floor((jogadores["Akshan"]["Constituição"]-10)/2/2),
        "int": math.floor((jogadores["Akshan"]["Inteligencia"]-10)/2/2),
        "sab": math.floor((jogadores["Akshan"]["Sabedoria"]-10)/2/2),
        "car": math.floor((jogadores["Akshan"]["Carisma"]-10)/2/2),
        },
    "Lux": {
        "for": math.floor((jogadores["Lux"]["Força"]-10)/2/2),
        "des": math.floor((jogadores["Lux"]["Destreza"]-10)/2/2),
        "con": math.floor((jogadores["Lux"]["Constituição"]-10)/2/2),
        "int": math.floor((jogadores["Lux"]["Inteligencia"]-10)/2/2),
        "sab": math.floor((jogadores["Lux"]["Sabedoria"]-10)/2/2),
        "car": math.floor((jogadores["Lux"]["Carisma"]-10)/2/2),
        },
    "I.A.R.A": {
        "for": math.floor((jogadores["I.A.R.A"]["Força"]-10)/2/2),
        "des": math.floor((jogadores["I.A.R.A"]["Destreza"]-10)/2/2),
        "con": math.floor((jogadores["I.A.R.A"]["Constituição"]-10)/2/2),
        "int": math.floor((jogadores["I.A.R.A"]["Inteligencia"]-10)/2/2),
        "sab": math.floor((jogadores["I.A.R.A"]["Sabedoria"]-10)/2/2),
        "car": math.floor((jogadores["I.A.R.A"]["Carisma"]-10)/2/2),
        },
    "Sett": {
        "for": math.floor((jogadores["Sett"]["Força"]-10)/2/2),
        "des": math.floor((jogadores["Sett"]["Destreza"]-10)/2/2),
        "con": math.floor((jogadores["Sett"]["Constituição"]-10)/2/2),
        "int": math.floor((jogadores["Sett"]["Inteligencia"]-10)/2/2),
        "sab": math.floor((jogadores["Sett"]["Sabedoria"]-10)/2/2),
        "car": math.floor((jogadores["Sett"]["Carisma"]-10)/2/2),
        },
    "Vayne": {
        "for": math.floor((jogadores["Vayne"]["Força"]-10)/2/2),
        "des": math.floor((jogadores["Vayne"]["Destreza"]-10)/2/2),
        "con": math.floor((jogadores["Vayne"]["Constituição"]-10)/2/2),
        "int": math.floor((jogadores["Vayne"]["Inteligencia"]-10)/2/2),
        "sab": math.floor((jogadores["Vayne"]["Sabedoria"]-10)/2/2),
        "car": math.floor((jogadores["Vayne"]["Carisma"]-10)/2/2),
        },
    "Yasuo": {
        "for": math.floor((jogadores["Yasuo"]["Força"]-10)/2/2),
        "des": math.floor((jogadores["Yasuo"]["Destreza"]-10)/2/2),
        "con": math.floor((jogadores["Yasuo"]["Constituição"]-10)/2/2),
        "int": math.floor((jogadores["Yasuo"]["Inteligencia"]-10)/2/2),
        "sab": math.floor((jogadores["Yasuo"]["Sabedoria"]-10)/2/2),
        "car": math.floor((jogadores["Yasuo"]["Carisma"]-10)/2/2),
        },
    "Jinx": {
        "for": math.floor((jogadores["Jinx"]["Força"]-10)/2/2),
        "des": math.floor((jogadores["Jinx"]["Destreza"]-10)/2/2),
        "con": math.floor((jogadores["Jinx"]["Constituição"]-10)/2/2),
        "int": math.floor((jogadores["Jinx"]["Inteligencia"]-10)/2/2),
        "sab": math.floor((jogadores["Jinx"]["Sabedoria"]-10)/2/2),
        "car": math.floor((jogadores["Jinx"]["Carisma"]-10)/2/2),
        },
}

'''print(jogadores["I.A.R.A"]["Sabedoria"])
print(modificadores["I.A.R.A"]["sab"])'''

inimigos = {
        
}

habilidades = {
    "Akshan": {
        "Q" : math.floor((jogadores["Akshan"]["Destreza"]-10)/2/2),
    }
}



'''for c in modificadores["Akshan"]:
    print(c)

print(habilidades["Akshan"]["Q"])'''

jogadores_presentes = int(input("Quantos jogadores irão jogar? "))

tabela = False
contador_inimigos = 0
adicionando_inimigo = True

turnos_participantes = list()
quantidade_inimigos = int(input("Quantos inimigos? "))

turnos = len(turnos_participantes)

for c in range(0, jogadores_presentes+quantidade_inimigos):
    turnos_participantes.append(input(f"{c+1}.Turno joga: "))
print(turnos_participantes)

print("")

while True:
    if ( tabela == True): #tabela
        print("="*30)
        print("Inimigos")
        for contador in range(len(inimigos)):
            print(f"Inimigo {contador}")
            print(f'Nome: {inimigos[f"inimigo{contador}"]["Nome"]}')
            print(f'Vida: {inimigos[f"inimigo{contador}"]["Vida"]}')
            print(f'Classe de Armadura: {inimigos[f"inimigo{contador}"]["Classe de Armadura"]}')
            print("-"*30)

        print("="*30)
        print("")
    escolha = str(input("1.Inimigos \n2.Atacar \n3.Curar \n4.Proteger \n5.CoolDowns \n6.Passar Turno \n---> "))[0]
    if (escolha == "1"): #Inimigos
        cls()
        while True:
            escolha_inimigos =  str(input("1.Adicionar Inimigo \n2.Listar Inimigos \n3.Voltar \n---> "))[0]
            if (escolha_inimigos) == "3":
                cls()
                break
            if (escolha_inimigos == "1"): #Adicionar Inimigo
                while (adicionando_inimigo == True):
                    inimigos[f"inimigo{contador_inimigos}"] = {
                            "Nome": input("Nome do Inimigo: "),
                            "Vida": input("Vida do Inimigo: "),
                            "Classe de Armadura": input("Classe de Armadura: ")
                        }
                    print("\n")
                    contador_inimigos += 1
                    while True:
                        add_inimigo = input("Adicionar mais um inimigo? [S/N] ").lower()[0]
                        if (add_inimigo == "n"):
                            adicionando_inimigo = False
                            print("\n")
                            break
                        elif (add_inimigo == "s"):
                            print("\n")
                            break
                        else:
                            print("Valor incorreto, tente novamente!")
                            print("\n")
                adicionando_inimigo = True
                tabela = True
            elif (escolha_inimigos == "2"): #Listar Inimigos
                cls()
                for contador in range(len(inimigos)):
                    print(f"Inimigo {contador}")
                    print(f'Nome: {inimigos[f"inimigo{contador}"]["Nome"]}')
                    print(f'Vida: {inimigos[f"inimigo{contador}"]["Vida"]}')
                    print(f'Classe de Armadura: {inimigos[f"inimigo{contador}"]["Classe de Armadura"]}')
                    print("")
    elif (escolha == "2"): # Atacar
        cls()
        print("Inimigos vivos:")
        print("")
        for contador in range (len(inimigos)):
            print(f'{contador+1}.{inimigos[f"inimigo{contador}"]["Nome"]}')
        print("")
        print("Jogadores vivos:")
        print("")
        for contador in range (len(jogadores)):
            print(f'{contador+1}.{jogadores[f"id{contador}"]["Nome"]}')
        print("")
        while True:
            atacar = str((input("Selecione um alvo para atacar \n3.Voltar \n---> ")))
            if (atacar == "3"):
                cls()
                break
            if (atacar <= len(inimigos)):
                print("")
                print(f"Atacando {inimigos[f'inimigo{atacar-1}']['Nome']}...")
                print("")
                dano = int(input("Qual foi o dano? "))
                inimigos[f'inimigo{atacar-1}']["Vida"] -= dano
            else:
                print("")
                print("Inimigo inexistente.")
                print("")
    else:
        cls()
        print("")
        print("Opção inválida")
        print("")






#print(len(jogadores))


