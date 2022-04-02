#Comandos de decisão If
# = atribuição
# == comparação

"""a=True

if a: #começa a execusão com dois pontos
   print("CFB Cursos")
    
retorno CFB Cursos, if é executado se o valor for verdadeiro"""

a=10
b=5
res=0
op="+"

"""
if a>b: #executa o bloco pois a expressão é verdadeira
    print("Valor de a é maior que b")"""

"""
if a<b:#retorno é false é o bloco else é executado
    print("a é maior do que b")
else:
    print("b é maior que a")"""

if op=="+":
    res=a+b
    print("Resultado da operação "+ op+ " é igual a: "+ str(res))