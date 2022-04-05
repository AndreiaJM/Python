"""
Uma função em python é definida pelo def+nome da função
"""
import os
#função com passagem de parametros e ARGUMENTOS ARBITRARIOS
#*t quantidade de argumentos indefinidos
def textos(*t): #t é um array de parametros
    for x in t:
        print(x)

textos("aulas1","aulas2","aulas3","aulas4","aulas5")

def soma(*s): #função para somar quantidade de numeros indefinidos
    r=0
    for x in s:
        r+=x
        print(r)
soma(1,1,1,1,1,1,1,1,1,1)

#################################################

valores=[1,5,3,2]

def somar(num):
    r=0
    for x in num:
        r+=x
        print(r)
#passando um list como valor do parametro ao invés de um argumento arbitrario. 1 lista = 1 variavel
somar(valores) 


