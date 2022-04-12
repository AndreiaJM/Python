#r - read - leitura
#a - append - anexar
#w - write - escrita
#x - create - criar
#t - texto
#b - binario

import re

"Usando o readline com regex"

from asyncore import read

nome="teste.txt"

#abertura do arquivo para leitura
f=open("C:/Users/andre/OneDrive/Documentos/cursojs/Python/aula42-OperacoesComArquivos/"+nome,"rt")

#usando o regex com readline
#substituindo os espaços por traços
res=re.sub("\s","-",f.readline())
print(res)
f.close()

#Abirndo o arquivo novamente porem para escrita
f=open("C:/Users/andre/OneDrive/Documentos/cursojs/Python/aula42-OperacoesComArquivos/"+nome,"wt")

f.write(res)

f.close()