import json
import os

#criando arquivos json
#json é praticamente um dictionary, manipulado da mesma forma

#colocar apostrofo para diferencias de dictionary
carros_json='{"marca":"honda","modelo":"HRV","cor":"prata"}'

#json.loads = transforma o json em um elemento do python
carros=json.loads(carros_json)

print(carros["marca"])

for x in carros.items(): #impressão dos itens(chave valor) ao inves de apenas as chaves
    print(x)

os.system("pause")

for k,v in carros.items():
    print(k+"-----"+v)