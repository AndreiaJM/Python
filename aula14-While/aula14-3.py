import os

os.system('cls') #limpar a tela

"""
Looping while: 
inicialização
teste logico
incremento, decremento o controle 

"""
i=0

carros=[]
carro=input("Digite o nome do novo carro:")
while carro!="-1":
    carros.append(carro)
    carro=input("Digite o nome do novo carro:")
print("Fim da execusão do programa")

os.system('cls')

for x in carros:
    print(x)

print("Fim da execusão do programa")