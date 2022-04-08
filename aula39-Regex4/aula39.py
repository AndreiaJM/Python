import re #RegEx

#search = não retorna coleção, retorna a posição da primeira ocorrencia


texto="Cursos de Python, do CFB Cursos, canal no Youtube"

res=re.sub(",",".", texto)#substitui algum carater ou espaço
#neste caso substituimos a vígula pelo ponto

print(res)




