from tkinter import *

app=Tk()

app.title("CFB Cursos")
app.geometry("500x300")
app.configure(background="#dde")

#anchor posiciona o conteudo dentro da label
#anchor => N=norte, S=sul, E=leste, W=oeste
#NE=nordeste, SE=Sudeste, SO=sudoeste, NO=Noroeste
Label(app,text="Nome",background="#dde",foreground="#009",anchor=W).place(x=10,y=10,width=100,height=20)
#componente de texto: Entry()
vnome=Entry(app)
vnome.place(x=10,y=30,width=200,height=20)

Label(app,text="Telefone",background="#dde",foreground="#009",anchor=W).place(x=10,y=60,width=100,height=20)
vfone=Entry(app)
vfone.place(x=10,y=80,width=100,height=20)

Label(app,text="E-mail",background="#dde",foreground="#009",anchor=W).place(x=10,y=110,width=100,height=20)
vmail=Entry(app)
vmail.place(x=10,y=130,width=300,height=20)

Label(app,text="OBS",background="#dde",foreground="#009",anchor=W).place(x=10,y=160,width=100,height=20)
vfone=Text(app)
vfone.place(x=10,y=180,width=300,height=80)

app.mainloop()