import os

os.system("cls")

#array de dictionary

carro1={
        "Fabricante":"Honda",
        "Modelo":"HRV"
}
carro2={
        "Fabricante":"Volks",
        "Modelo":"Golf"
}
carro3={
        "Fabricante":"Ford",
        "Modelo":"Focus"
}

#dictionary com chaves de valor dictionary
carros={
    "c1":carro1,
    "c2":carro2,
    "c3":carro3
}

#imprimindo dictionary com chaves de valor dictionary
print(carros["c1"]["Fabricante"])