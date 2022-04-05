"""
Contrutores em python
"""
import os

class Carro:
    velMax=0
    ligado=False
    cor=""

    #Construto em python __init__
    #self seria o this em outras linguagens
    def __init__(self,vm,li,c):
        self.velMax=vm
        self.ligado=li
        self.cor=c

    def mostrar(self):
        print("Velocidade maxima: "+str(self.velMax))
        print("Cor do carro: "+self.cor)
        estado="sim" if self.ligado else "não"
        print("Esta ligado: "+estado)
        print("--------------------------------------")

    def ligar(self):
        self.ligado=True

    def andar(self):
        if self.ligado:
            print("Andando")
        else:
            print("Carro Desligado")

os.system("cls")

c1=Carro(200,False,"Preto") #instanciado objeto 
c2=Carro(20,False,"Branco")
c3=Carro(350,False,"Cinza")

"""
c1.velMax=200
c1.cor="Preto"
c1.ligado=False"""

c1.ligar()
c1.mostrar()

c2.mostrar()

c3.mostrar()

c1.andar()
c2.andar()

