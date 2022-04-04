import random
import os

erros=0
sorteio=random.randrange(0,100)
jogador=int(input("Digite o numero a ser sorteado: "))

while(sorteio!=jogador):
    if(sorteio>jogador):
        print("Numero sorteado é maior")
    elif(sorteio<jogador):
        print("Numero sorteado é menor")
    jogador=int(input("Errou, tente novamente digite o numero a ser sorteado: "))
    erros+=1
print("Acertou!!! o numero sorteado foi o: "+ str(sorteio)+ "Erros: "+ str(erros))

