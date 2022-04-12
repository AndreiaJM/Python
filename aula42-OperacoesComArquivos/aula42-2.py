#r - read - leitura
#a - append - anexar
#w - write - escrita
#x - create - criar
#t - texto
#b - binario

from asyncore import read



nome="teste.txt"

#abertura do arquivo para leitura
f=open("C:/Users/andre/OneDrive/Documentos/cursojs/Python/aula42-OperacoesComArquivos/"+nome,"rt")

print(f.readline())#readline lê uma linha por vez, cada vez que é executado lê a proxima linha

#da para ler um readline com um for

#o resultado do readline é uma string, poder ser manipulado como ja aprendemos
res=f.readline()
print("Impressão do readline pela variavel: "+res) #imprimindo o resultado do readline


f.close()