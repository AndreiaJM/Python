#Escopo de variáveis
#variáveis globais podem ser acessadas dentro de funções 
"""As variaveis declaradas dentro das funções possuem escopo local
A palavra chave "global" muda o escopo desta varival para global
"""

num1=num2=res=0


def cn():
    global canal 
    canal= "CFB Cursos" 
cn() #chamada da função para inicializar a variavel
print(canal)

