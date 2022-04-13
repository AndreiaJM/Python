import re
import os

nome="text.txt"
caminho="C:/Users/andre/Desktop/Python/aula43-OperacoescomArquivos/"
#f=open(caminho+nome,"x") #x retorna erro caso o programa ja exista
#f.close()

#deletando arquivos:
#os.remove(caminho+nome)#arquivo excluido

#verificando se o arquivo ja existe
if os.path.exists(caminho+nome):
    print("Arquivo existente")
else:
    f=open(caminho+nome,"x")
    f.close()
