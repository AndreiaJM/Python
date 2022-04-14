import sqlite3
from sqlite3 import Error

#C:\Users\andre\OneDrive\Documentos\cursojs\Python\Banco

#o commit é usado apenas quando é feito alteração na tabela

######Criar conexão######
def conexaoBanco():
    caminho="C:\\Users\\andre\\OneDrive\\Documentos\\cursojs\\Python\\Banco\\agenda_db.db"
    con=None
    try:
        con=sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con

vcon=conexaoBanco()

######Inserir conteudo na tabela######
def inserir(conexao,sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        #para haver a persistencia de dados no banco é preciso executar o commit
        conexao.commit()
        print("registro inserido")
    except Error as ex:
        print(ex)

"""nome=input("Digite o nome: ")
telefone=input("Digite o telefone: ")
email=input("Digite o email: ")
vsql="INSERT INTO tb_contatos(T_NOMECONTATO,T_TEEFONECONTATO,T_EMAILCONTATO)VALUES('"+nome+"','"+telefone+"','"+email+"')"

#inserir(vcon,vsql)"""

######deletar conteudo na tabela######
def deletar(conexao,sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        #para haver a persistencia de dados no banco é preciso executar o commit
        conexao.commit()
        print("registro deletado")
    except Error as ex:
        print(ex)

vsql="DELETE FROM tb_contatos WHERE N_IDCONTATO=2"
#deletar(vcon,vsql)

######atualizar dados na tabela######
def atualizar(conexao,sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        #para haver a persistencia de dados no banco é preciso executar o commit
        conexao.commit()
        print("registro atualizado")
    except Error as ex:
        print(ex)

vsql="UPDATE tb_contatos SET T_NOMECONTATO='PITUCHA' WHERE N_IDCONTATO=4"
#atualizar(vcon,vsql)

######consultando os dados na tabela######
def consulta(conexao,sql):
        c=conexao.cursor()
        c.execute(sql)
        resultado=c.fetchall()
        return resultado

vsql="select * FROM tb_contatos"

res=consulta(vcon,vsql)

for x in res:
    print(x)

vcon.close()

