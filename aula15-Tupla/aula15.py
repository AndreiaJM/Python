import os

os.system('cls')

#Na lista Tupla usa-se parenteses
#Não da para substituir os itens na lista tipo tupla
#uma vez criada, não altera-se os valores

l_carros=["HRV","Golf","Argo"]
t_carros=("HRV","Golf","Argo")

t_carros[1]="CARRO" #Erro ao tentar adicionar item na tupla

for x in l_carros:
    print(x)