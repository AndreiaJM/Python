"""
Classe é a especificação de objetos
Objetos é a instacia de uma classe

python não trabalha com encapsulamento
"""

class Carro:
    velMax=0
    ligado=False
    cor=""

c1=Carro() #instanciado objeto 
c2=Carro()
c3=Carro()

c1.velMax=200
c1.cor="Preto"
c1.ligado=False

print("Velocidade maxima: "+str(c1.velMax))
print("Cor do carro: "+c1.cor)
estado="sim" if c1.ligado else "não"
print("Esta ligado: "+estado)

