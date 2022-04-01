#tipos de variáveis numericas
#python não concatena inteiro com string, a função str() faz o casting
#python não concatena typo com string, a função str() faz o casting

import random

num_i=10
num_f=5.2
num_c=1j #numero complexo

#array de numeros aleatórios, no python chama-se list
num_r=[
    random.randrange(0,59), #numeros aleatórios,
    random.randrange(0,59),
    random.randrange(0,59),
    random.randrange(0,59),
    random.randrange(0,59),
    random.randrange(0,59),
]

x=num_r



print("Valor" + str(x)+ "- Tipo"+ str(type(x))) #type informa o tipo da variável

print("Valor 0: " + str(num_r[0]))
print("Valor 1: " + str(num_r[1]))
print("Valor 2: " + str(num_r[2]))
print("Valor 3: " + str(num_r[3]))
print("Valor 4: " + str(num_r[4]))
print("Valor 5: " + str(num_r[5]))
print("Valor 6: " + str(num_r[6]))