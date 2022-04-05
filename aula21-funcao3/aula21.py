valores=[1,5,3,2]

def somar(num):
    r=0
    for n in num:
        r+=n
    return r #função com retorno

def valorlista(lista):
    for x in lista:
        print(x)

valorlista(valores)
print("Soma dos valores: "+str(somar(valores)))
