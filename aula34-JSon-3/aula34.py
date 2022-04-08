import json
from shlex import join

"""{
    "nome":"Andreia",
    "time":"aviadores",
    "vivo":"True",
    "energia":100,
    "mochila":["pederneira","corda","linha","arame"],
    "aeronaves":[
        {"tipo":"transporte","habilidade":80},
        {"tipo":"ataque","habilidade":100},
        {"tipo":"reconhecimento","habilidade":50}
    ]
} """

jogador_j='{"nome":"Andreia","time":"aviadores","vivo":"True","energia":100,"mochila":["pederneira","corda","linha","arame"],"aeronaves":[{"tipo":"transporte","habilidade":80},{"tipo":"ataque","habilidade":100}, {"tipo":"reconhecimento","habilidade":50}]}'

jogador=json.loads(jogador_j)

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
