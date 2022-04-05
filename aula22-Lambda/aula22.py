"""
Lambida são funções simples e anonimas
simples: possui apenas uma expressão
anonima: não tem nome

Não é preciso colocar o return pois ela retorna o rsultado

sintaxe: lambda arg:expr
palavra lambda
argumentos de entrada(parametros)
expressão= corpo da função
"""

#Atribuindo uma função lambda a uma variavel

soma=lambda a,b:a+b
mul=lambda a,b,c:(a+b)*c
print(soma(1,2)) #variável associada passando 2 valores 
print(mul(2,5,3)) #variável associada passando 3 valores 

