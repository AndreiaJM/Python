carros=["HRV","Golf","Argo","Focus","Fit","Fusion","Focus"]

"""Array no escopo do for, sem estar salvo em uma variável"""

for x in carros:
    print(x)
    if x=="Fit": #imprime o Fit depois para
        break

for x in carros:
    if x=="Fit": #para antes de imprimir o fit
        break
    print(x)

print("Fim do programa")
        