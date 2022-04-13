import sqlite3
from sqlite3 import Error

#C:\Users\andre\OneDrive\Documentos\cursojs\Python\Banco

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

nome=input("Digite o nome: ")
telefone=input("Digite o telefone: ")
email=input("Digite o email: ")

######Inserir conteudo na tabela######
vsql="INSERT INTO tb_contatos(T_NOMECONTATO,T_TEEFONECONTATO,T_EMAILCONTATO)VALUES('"+nome+"','"+telefone+"','"+email+"')"

def inserir(conexao,sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        #para haver a persistencia de dados no banco é preciso executar o commit
        conexao.commit()
        print("registro inserido")
    except Error as ex:
        print(ex)

inserir(vcon,vsql)


vcon.close()

