import re #RegEx

#search = não retorna coleção, retorna a posição da primeira ocorrencia


texto="Cursos de Python do CFB Cursos, canal no Youtube"

res=re.split("\s", texto)#retona  uma coleção dividida pelo pelo valor informado

print(res)

for x in res:
    print(x)


