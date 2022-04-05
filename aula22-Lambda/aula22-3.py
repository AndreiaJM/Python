#Funções lambda permitem que seja passado funções como parametros


"""Na função abaixo estamos recebendo como parametro o valor de x e uma função. Iremos somar o valor de x + função que por sua vez recebera o valor de x como parametro"""
r=lambda x,func:x+func(x)

print(r(2,lambda x:x*x)) #resultado 6