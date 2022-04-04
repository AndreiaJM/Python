def carros(c):
    print("Modelo "+c)

carros("HRV")

#####################################
#conseguimos definir um valor padrão para o parametro da função
def carros(c="Golf"):
    print("Modelo "+c)

carros() #quando imprimimos sem nada é impresso o valor padrão