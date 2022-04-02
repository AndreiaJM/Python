"""
Metodos para string: 

strip()
len()
lower()
upper()
replace()
split()
"""


curso="Curso de Python "

#Uma String é um array de caracteres ex: print(curso[0])

print(curso.strip())#metodo strip remove os espaços no começo e final da string


print(curso[0])
print(curso[0:4]) #intervalo de impressão o array de string
print("Tamanho: "+ str(len(curso))) #Tamanho da stirng = len()
print(curso.lower().strip())
print(curso.upper().strip())
print(curso.replace("Python","Java")) #substitui strings
a=curso.split(" ") #corta a partir do caracter ou espaço indicado e coloca em um array os cortes, retorna um list
print(a[0])


