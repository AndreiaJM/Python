"""
Em python a estrutura Senão se se resume em: Elif 

if = se
elif = senão se
else = senão

"""

a=10
b=5
op="a"
res=0

if op=="+":
    res=a+b
elif op=="-":
    res=a-b
elif op=="*":
    res=a*b
elif op=="/":
    res=a/b
else:
    print("Nenhuma das alternativas anteriores")

print("O valor de "+str(a)+" "+op+ str(b)+" "+ "é igual a: "+ str(res))