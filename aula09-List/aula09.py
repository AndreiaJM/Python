"""
append = adiciona item a lista
len(carros) = tamanho da lista
remove()=remove item da lista
pop() = remove o ultimo item da lista
clear() = lispa toda a lista

del carros[2] = tambem remove o item do indice indicado

"""

carros=["HRV","Golf","Argo","Focus"]
#carros[3]="Fusion" #indice 3 substituido

carros.append("Fit")
carros.append("Fusion")
carros.append("Polo")

carros.remove("Fusion")
carros.pop()

del carros[2]

carros2=list(carros)

print(carros) #impressão da direita para esquerda
print(len(carros))
print(carros2)

carro2=["147", "brasilia", "celta"]
carro3=carros+carro2 #concatenando duas listas

print(carro3)

