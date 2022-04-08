#Regex = expressões regulares em python
#expressões regulares = mini linguagem de programação
# findall = regex que pesquisa todas as ocorrencias de uma 
# determinada string retornando uma coleção 

import re #RegEx

texto="Cursos de Python do CFB Cursos, canal no Youtube"

pesq=input("Pesquisar: ")
res=re.findall(pesq,texto)
#res tera o valor de uma coleção

print(res)
qtd=len(res) #Qauntidade de elementos
print("Qtde: "+str(qtd))

for x in res: #imprimindo um por um
    print(x)