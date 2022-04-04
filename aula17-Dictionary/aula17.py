#A lista do tipo dictionary é definida com chaves{}
#funciona com a declaração da chave(como se fosse nome de #variavel) dois pontos e seu valor

carro={
    "Fabricante":"Honda",
    "Modelo":"HRV",
    "Ano":"2016",
    "Cor":"Prata"
}
print(carro) #imprime tudo
#apontando para chave ele retona o valor
print(carro["Fabricante"])
fab = carro["Modelo"] #pode ser guardado em uma variável
print(fab)
print(carro.get("Cor")) #pode ser usado o metodo get

carro["Cor"]="rosa" #Alterando valores
print(carro["Cor"])

#dentro do for
for x in carro:
    #print(x) imprime chaves
    print(carro[x]) #imprime valores

#dentro do for imprimindo chave e itens
for c,v in carro.items():
    print("chave: "+ c+ " Valor: "+ v)


