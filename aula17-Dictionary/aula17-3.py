import os

os.system("cls")

#array de dictionary
carro={
    "carro1":{
        "Fabricante":"Honda",
        "Modelo":"HRV"
    },
    "carro2":{
        "Fabricante":"Volks",
        "Modelo":"Golf"
    },
    "carro3":{
        "Fabricante":"Ford",
        "Modelo":"Focus"
    }
}

#imprimindo chave valor no array dictionary
print(carro["carro1"]["Fabricante"])