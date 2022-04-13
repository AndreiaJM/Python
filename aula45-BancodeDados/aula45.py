
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

######Criar tabela######
vsql="""CREATE TABLE tb_contatos(
        N_IDCONTATO INTEGER PRIMARY KEY AUTOINCREMENT,
        T_NOMECONTATO VARCHAR(30),
        T_TEEFONECONTATO VARCHAR(14),
        T_EMAILCONTATO VARCHAR(30)
        );"""

def criarTabela(conexao,sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        print("Tabela criada")
    except Error as ex:
        print(ex)

criarTabela(vcon,vsql)


vcon.close()

