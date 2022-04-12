#r - read - leitura
#a - append - anexar
#w - write - escrita
#x - create - criar
#t - texto
#b - binario

nome="teste.txt"

#abertura do arquivo para leitura
f=open("C:/Users/andre/OneDrive/Documentos/cursojs/Python/aula42-OperacoesComArquivos/"+nome,"rt")

print(f.read())#sem parametro lê tudo

print(f.read(10))#parametro do read lê a quantidade de caracteres indicado

print(f.readline())#readline lê uma linha por vez, cada vez que é executado lê a proxima linha

#da para ler um readline com um for

f.close()