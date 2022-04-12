#file = f
import os

os.system("cls")
nome="textes.txt"
f=open("C:/Users/andre/OneDrive/Documentos/cursojs/Python/aula40-OperacoesComArquivos/"+nome,"wt")

txt=input("Digite um texto: \n")

f.write(txt)

while txt != "sair":
    txt=input("Digite um texto: \n")
    f.write(txt)


f.close() #fecha o arquivo aberto


#r = read - Leitura
#a = append - Anexar
#w = write - Escrita
#x = create - criar
#b = binary - binario
#t = text - texto


#caso o arquivo não exista para leitura ou escrita ele é criado