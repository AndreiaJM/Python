carros=["HRV","Polo","Jetta","Cruze","Fusion"]

cont=0
#impressão sem o iterator
while cont<len(carros):
    for x in carros:
        print(x)
        cont+=1 #se não incrementado vira um looping infinito
    