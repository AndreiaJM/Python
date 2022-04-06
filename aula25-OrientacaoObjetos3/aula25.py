"""
Herança em python: classe que herda outra classe
"""
import os

class NPC: #Superclasse
    def __init__(self,nome,time,forca,municao):
        self.nome=nome
        self.time=time
        self.forca=forca
        self.municao=municao
        self.vivo=True
        self.energia=100
    def info(self):
        print("Nome: "+self.nome)
        print("Time: "+str(self.time))
        print("Forca: "+str(self.forca))
        print("Municao: "+str(self.municao))
        print("Vivo: sim" if self.vivo else "Vivo: não")
        print("Energia: "+str(self.energia))
        print("-----------------------------------------")

#Herança é passado pelo parenteses da outra classe
#classe filho

class Soldado(NPC):
    #O construtor da classe filho sobrescreve o da classe pai
    def __init__(self,nome,time):
        self.forca=200
        self.municao=200
        super().__init__(nome,time,self.forca,self.municao)

class Guarda(NPC):
    def __init__(self,nome,time):
        self.forca=100
        self.municao=20
        super().__init__(nome,time,self.forca,self.municao)

class Elite(NPC):
    def __init__(self,nome,time):
        self.forca=100
        self.municao=20
        super().__init__(nome,time,self.forca,self.municao)
        def info():
            super().info()

s1=Guarda("Olho vivo",1)
s2=Soldado("Bala na agulha",1)
s3=Elite("Ninja",1)
s4=Guarda("Super atento",2)
s5=Soldado("Tiro certo",2)
s6=Elite("Samurai",2)

s1.vivo=False

s1.info()
s2.info()
s3.info()
s4.info()
s5.info()
s6.info()

