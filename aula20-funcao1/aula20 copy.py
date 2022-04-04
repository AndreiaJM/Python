"""
Uma função em python é definida pelo def+nome da função
"""
from statistics import multimode

import os

n1=2
n2=3
sinal="+"

#variavies globais podem ser acessadas dentro de funções
#função sem parametro e sem retorno com variaveis globais
def somar():
    r=n1+n2
    sinal="+"
    print("A soma de: "+str(n1)+sinal+str(n2)+" é igual a:"+str(r))
    print("https://github.com/")

def subtrair():
    r=n1-n2
    sinal="-"
    print("A soma de: "+str(n1)+sinal+str(n2)+" é igual a:"+str(r))
    print("https://github.com/")

def dividir():
    r=n1/n2
    sinal="/"
    print("A soma de: "+str(n1)+sinal+str(n2)+" é igual a:"+str(r))
    print("https://github.com/")

def multiplicar():
    r=n1*n2
    sinal="*"
    print("A soma de: "+str(n1)+sinal+str(n2)+" é igual a:"+str(r))
    print("https://github.com/")

os.system("cls")
somar()
subtrair()
dividir()
multiplicar()
