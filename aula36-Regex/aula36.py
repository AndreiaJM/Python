#Regex = expressões regulares em python
#expressões regulares = mini linguagem de programação
# findall = regex que pesquisa todas as ocorrencias de uma 
# determinada string retornando uma coleção 

import re #RegEx

texto="Cursos de Python do CFB Cursos, canal no Youtube"

res=re.findall("Python",texto)
#res tera o valor de uma coleção

print(res)