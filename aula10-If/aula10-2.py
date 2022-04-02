a=10
b=5
op="*"
res=0

if op=="+":
    res=a+b
if op=="-":
    res=a-b
if op=="*":
    res=a*b
if op=="/":
    res=a/b

print("O valor de "+str(a)+" "+op+ str(b)+" "+ "é igual a: "+ str(res))