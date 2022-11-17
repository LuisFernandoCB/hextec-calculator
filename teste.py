jogadores = {
    }
inimigos = {
        
    }
while True:
    escolha = str(input("1.Jogadores \n2.Inimigos \n3.Atacar \n4.Curar \n5.Proteger \n6.CoolDowns \n7.Passar Turno \n---> "))[0]
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
        print(inimigos)
        print("Inimigos vivos:")
        print("")
        for contador in range (len(inimigos)):
            print("\n")
            print(f'{contador+1} . {inimigos["Nome"]}')
            print(f' Vida: {inimigos["Vida"]}')
            print(f' Classe de Armadura: {inimigos["Classe de Armadura"]}')
            #print(f'{contador}.{inimigos[f"{inimigos{contador}}"]["Nome"]}')
        print("")
        print("Jogadores vivos:")
        print("")
        for contador in range (len(jogadores)):
            print('Parte em produção')
            #print(f'{contador+1}.{jogadores[f"id{contador+1}"]["Nome"]}')
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
