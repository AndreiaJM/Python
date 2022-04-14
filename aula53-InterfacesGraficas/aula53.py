#Trabalhando com interfaces graficas#

"""
Tkinter usa a classe TK, é um conjunto de ferramentas de interface grafica que é nativo do python

Usa a classe TK para disponibilizar o widgets (botões,caixas de textos,labels,janelas)

Tkinter não é a biblioteca mais completa, porem é uma interface facil, rapida e nativa do java

"""

from cProfile import label
from cgitb import text
from tkinter import *

app=Tk() #metodo da classe tkinter(janela)

app.title("CFB cursos") #titulo da janela
app.geometry("500x300") #configura do tamanho da janela
app.configure(background="#008")#configura a cor da janela com codigo rgb

#alguns metodos possuem inicial maiuscula como o Label
#é preciso indicar o elemento pai do label e apos isso suas configurações
txt1=Label(app,text="Curso de python",background="#008",foreground="#fff")
txt1.place(x=10,y=10,width=150,height=30)#para a label aparecer é reciso posicionar e expecificar seu tamanho atraves do place

vtxt="Modulo Tkinter"
vgb="#ff0"
vfg="#000"
txt2=Label(app,text=vtxt,bg=vgb,fg=vfg)
txt2.pack(ipadx=20,ipady=20,padx=5,pady=5,side="top",fill=X,expand=True)# pack éadequado para situações de containeer

app.mainloop() #executa o programa

"""
Propriedades: 

padx: padding - espaçamento interno em x
pady: padding - espaçamento interno em y

side="top": Posição, porem quando há outro elemento ele não ocupa o topo por exemplo

fill=X: Expanção da tela no eixo indicado


"""