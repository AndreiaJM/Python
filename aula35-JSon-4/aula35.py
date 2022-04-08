#Usando json de arquivo externo

import json

#caminho do arquivo externo
with open ('C:/Users/andre/OneDrive/Documentos/cursojs/Python/aula35-JSon-4/jogador.json') as f:
    jogador=json.load(f)

#impressão das chaves:
for c in jogador:
    print(c)

print("====================================")
#impressão dos itens:
for i in jogador.items():
    print(i)

print("====================================")

#valores
for i in jogador.values():
    print(i)

print("====================================")

#valor especifico
print(jogador["nome"])

print("====================================")

#items da mochila
for j in jogador["mochila"]:
    print(j)

print("====================================")

#aeronaves
for a in jogador["aeronaves"]:
    print(a)

print("====================================")

#aeronaves tipos 
for a in jogador["aeronaves"]:
    print(a["tipo"])

print("====================================")

#aeronaves habilidades 
for a in jogador["aeronaves"]:
    print(a["habilidade"])

print("====================================")

#aeronaves tipos + habilidades
for a in jogador["aeronaves"]:
    print(a["tipo"]+" - "+str(a["habilidade"]))

