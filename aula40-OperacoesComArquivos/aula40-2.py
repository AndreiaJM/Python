#file = f
import os

os.system("cls")
nome="textes.txt"
f=open("C:/Users/andre/OneDrive/Documentos/cursojs/Python/aula40-OperacoesComArquivos/"+nome,"at")

#Escrevendo dentro do arquivo
#Abrindo o arquivo em modo w ele sobrescreve o que foi escrito antes
#Abrindo em modo a - append ele grava e não Sobrescreve
f.write("Curso de python \n")#\n para pular linha no arquivo
f.write("Estudando")

#Conseguimos excrever um input

txt = input("Escreva um texto: ")
f.write(txt+"\n")


f.close() #fecha o arquivo aberto


#r = read - Leitura
#a = append - Anexar
#w = write - Escrita
#x = create - criar
#b = binary - binario
#t = text - texto


#caso o arquivo não exista para leitura ou escrita ele é criado