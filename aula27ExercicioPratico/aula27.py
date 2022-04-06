from distutils.log import info
import imp


import os

carros=[]

class Carro:
    nome=""
    potencia=0
    velMax=0
    ligado=False

    def __init__(self,nome,potencia):
        self.nome=nome
        self.potencia=potencia
        self.velMax=int(potencia)*2
        self.ligado=False

    def ligar(self):
        self.ligado=True

    def desligar(self):
        self.ligado=False

    def info(self):
        print("Nome: .............."+self.nome)
        print("Potencia: .........."+str(self.potencia))
        print("Velocidade maxima:.."+str(self.velMax))
        estado= "sim................" if self.ligado==True else "não................"
        print("Ligado: ................"+ estado)

def Menu():
    os.system("cls") or None
    print("1 - Novo Carro")
    print("2 - Informações do carro")
    print("3 - Excluir Carro")
    print("4 - Ligar Carro")
    print("5 - Desligar Carro")
    print("6 - Listar Carros")
    print("7 - Sair do menu")
    print("Quantidade de carros: "+str(len(carros)))
    opc=input("Digite uma opção")
    return opc

def NovoCarro():
    os.system("cls")
    n=input("Nome do carro: ")
    p=input("Potencia do carro: ")
    car=Carro(n,p)
    carros.append(car)
    print("Carro criado")
    os.system("pause")

def informacoes():
    os.system("cls") or None
    n = input("Informe o numero do carro que deseja informação:")
    try:
        carros[int(n)].info()
        os.system("pause")
    except:
        print("Carro não existe na lista")
        os.system("pause")
        

def excluirCarro():
    os.system("cls") or None
    n = input("Informe o numero do carro que deseja excluir:")
    try:
        del carros[int(n)]
        print("Carro"+str(n)+" excluído")
        os.system("pause")
    except:
        print("Carro não existe na lista")
        os.system("cls")

def ligar():
    os.system("cls") or None
    n = input("Informe o numero do carro que deseja ligar:")
    try:
        carros[int(n)].ligar()
        print("Carro ligado")
        os.system("pause")
    except:
        print("Carro não existe na lista")
        os.system("cls")

def desligar():
    os.system("cls") or None
    n = input("Informe o numero do carro que deseja desligar:")
    try:
        carros[int(n)].desligar()
        print("Carro desligado")
        os.system("pause")
    except:
        print("Carro não existe na lista")
        os.system("cls")

def listar():
    os.system("cls") or None
    p=0
    for c in carros:
        print(str(p)+" - "+c.nome)
    os.system("pause")
ret=Menu()

while(ret<"7"):
    if ret=="1":
        NovoCarro()
    elif ret=="2":
        informacoes()
    elif ret=="3":
        excluirCarro()
    elif ret=="4":
        ligar()
    elif ret=="5":
        desligar()
    elif ret=="6":
        listar()
    ret=Menu()

os.system("cls")
print("Programa finalizado")
        
    











