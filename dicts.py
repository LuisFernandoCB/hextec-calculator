lista = list()

lista2 = ["A", "B", "C"]

print(lista, "-", lista2)


dicto = dict()

dicto2 = {
    "P": "Fósforo",
    "Cu": {
        "eletrons": 15,
        "Nome": "Cobre",
        },
    "H": "Hidrogênio",
    }

print(dicto, dicto2)

print(f" Numero de eletrons: {dicto2['Cu']['eletrons']} ")
