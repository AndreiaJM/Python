"""Iterator serve para percorrer listas para frente"""

carros=["HRV","Polo","Jetta","Cruze","Fusion"]
#com o iterator podemos colocar mais itens sem a necessidade de contolar o tamanho da lista.

itCarros=iter(carros)

#while com iterator
while itCarros:
    try:
        print(next(itCarros))
    except StopIteration:
        print("Fim da lista")
        break