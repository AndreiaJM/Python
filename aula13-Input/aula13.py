# coletar dados do usuario = input()
#Tudo que entra pelo input é do tipo string
#Sendo necessario o casting para trabalhar com outro tipo de #dado

"""
Limpar a tela no windows: 

import os

os.system('cls')
"""

import os
A
os.system('cls')

nome=input("Digite o seu nome: ")

print("Ola "+nome)

num1=input("Digite o primeiro valor: ") #string
num2=input("Digite o primeiro valor: ") #string
#res=(num1)+num2 #concatenação de strings
res=int(num1)+int(num2) #casting para transformar em numeros
print(res)

num1=int(input("Digite o primeiro valor: ")) #casting no input
num2=int(input("Digite o primeiro valor: ")) #string
#res=(num1)+num2 #concatenação de strings
res=num1+num2
print(res)
