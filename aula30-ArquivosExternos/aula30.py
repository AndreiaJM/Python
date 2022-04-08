#chamando funções de outros arquivos

#arquivo importado para uso da função
import canal as cn #cn apelido para o arquivo importado
#from canal import jogador = importado apenas uma coisa do arquivo

#função canal_nome() que esta no arquivo canal
cn.canal_nome()
print(cn.jogador["nome"])

#verificando  o que tem dentro do arquivo:
"""
res=dir(canal)
for x in res:
    print(x)"""