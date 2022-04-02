"""
Metodos para String

in
not in

"""

curso="Curso de Python"
palavra="python"

res="Python" in curso #procurando se há a palavra na string
res2=palavra.upper() in curso.upper() #usando a variavel com a palavra
res3="Python" not in curso #Retorna Boolean
res4=palavra not in curso  #usando a variavel com a palavra

print(res)
print(res2)
print(res3)
print(res4)

