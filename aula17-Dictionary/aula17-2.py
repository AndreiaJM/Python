import os

os.system("cls")

carro={
    "Fabricante":"Honda",
    "Modelo":"HRV",
    "Ano":"2016",
    "Cor":"Prata"
}
#carro.clear() função limpa todo o dictionary

#adicionando nova chave valor
carro["Cambio"]="automatico"

#removendo chave valor com metodo pop("chave")
carro.pop("Cambio")
del(carro["Fabricante"])

#procurando chave dentro do dictionary

if "Modelo" in carro:
    print("Possui modelo")

#Quantidade de conjuntos do dictionary 
print(len(carro)) #4 conjuntos