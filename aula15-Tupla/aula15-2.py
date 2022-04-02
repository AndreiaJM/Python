import os

os.system('cls')

#Na lista Tupla usa-se parenteses
#Não da para substituir os itens na lista tipo tupla
#uma vez criada, não altera-se os valores

l_carros=["HRV","Golf","Argo"]
t_carros=("HRV","Golf","Argo")

l_carros=list(t_carros) #casting de tupla para list
l_carros[0]="CARRO"

t_carros=tuple(l_carros) #casting de list para tupla

for x in t_carros:
    print(x)