import os

os.system('cls') #limpar a tela

"""
Looping while: 
inicialização
teste logico
incremento, decremento o controle 

"""
i=0

carros=["HRV","Golf","Argo","Onix","Focus"]
tam=len(carros)

while i<tam:
    print(carros[i])
    i+=1
    if i>=5:
        break
print("Fim do looping")