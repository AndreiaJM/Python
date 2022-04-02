#bool = True/False

"""Variaveis vazias retornam False inclusive do tipo list

String vazia = retorna False
Inteiros iguais a 0 retonam false

"""

aula=10<15

print(aula)

aula2="CFB cursos"
aula3 = ""

print(bool(aula2))
print(bool(aula3))#strigs vazias retornam falso

if aula2:
    print("possui texto")
else:
    print("Não possui um texto")

aula4=1
aula5=0

print(bool(aula4))
print(bool(aula5))






