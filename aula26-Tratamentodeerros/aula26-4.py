#Tratamento de erros
#Bloco try/except/finally
#Não imprime a mensagem padrão do sistema

"""Gerando um erro, palavra chave: raise e if else"""


num=1 #String

if not type(num) is int:
    raise Exception("Somente numeros inteiros")
else:
    print(num)



