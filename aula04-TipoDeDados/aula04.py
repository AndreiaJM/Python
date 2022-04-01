x=1 # tipo int
x="CFB Cursos" #tipo string
x = 15.6 #tipo float
x= False #tipo boolean em python escrito com letra maiuscula
n1=5;n2=2;x=complex(n1,n2) #numero inteiro com parte imaginaria(numero complexo)

#print(x.real) #parte real do numero complexo
#print(x.imag) #parte imaginaria do numero complexo

"""Coleções - List"""

#list
#x=["carro", "avião","navio",1,True] pode ser colocado tipos diferentes no python
#x[0]="onibus"

"""Coleções - Tupla

A coleção tupla é referenciada com parenteses() aonde
NÃO é possivel substituir e conteudo das posições 

"""

x=("carro", "avião","navio",1,True)
#x[0]="onibus" não e possivel substituir

"""Coleções - Range

Cri uma lista grande de forma facil
"""

x=range(0,100) #array com 100 posições 


"""Coleções - Dictionary

Dictionary é referenciada com chaves{}, funciona com chave: valor
"""

x={ #Dict
    "canal":"CFB Cursos",
    "curso":"Curso de Python",
    "nome": "Andreia"
}

#print("Valor da variavel: "+x["canal"]) #para imprimir coloca-se o nome da chave


"""Coleções - Set

A coleção set não repete valores
"""

x={3,3,4,5,6,6,7,8} #set, sem repetição de valores
x=frozenset({3,3,4,5,6,6,7,8}) #função que congela os valores do set ou seja não pode ser alterados

print("Valor da variavel: "+str(x))
print("Tipo da variavel: "+ str(type(x)))