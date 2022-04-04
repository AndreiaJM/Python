carros=[
    ["Modelo","HRV"],
    ["Fabricante","Honda"],
    ["Ano","2016"]] #caso numero seja do tipo inteiro é preciso fazer o casting com str()

carros[2][1]="2022" #mudando valor na matriz

#imprimindo a matriz com o for
for l,c in carros:
    print("["+l+"-"+c+"]")
    