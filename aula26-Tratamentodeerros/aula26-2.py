#Tratamento de erros
#Bloco try/except/finally
#Não imprime a mensagem padrão do sistema

"""Exemplo com erro conhecido:
try: #
    print(x)
except NameError: #erro conhecido
    print("x não inicializado")
except: #erro conhecido
    print("erro descohecido") """

try: 
    print(x)
except: #erro conhecido
    print("Erro no programa")
else: #caso não seja capturado a exceção
    print("Tudo certo")
finally: #executado ao final do tratamento do
    print("fim do tratamento")

