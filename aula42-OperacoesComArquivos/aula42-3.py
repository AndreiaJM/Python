#r - read - leitura
#a - append - anexar
#w - write - escrita
#x - create - criar
#t - texto
#b - binario

nome="teste.txt"

#abertura do arquivo para leitura
f=open("C:/Users/andre/OneDrive/Documentos/cursojs/Python/aula42-OperacoesComArquivos/"+nome,"rt")

#da para ler um readline com um for
for x in f:
    print(x)

f.close()