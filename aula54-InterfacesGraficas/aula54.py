from tkinter import *
from turtle import title


aplicativo=Tk()

aplicativo.title("titulo da caixa")
aplicativo.geometry("600x600")
aplicativo.configure(background="#f00")

txt1=Label(aplicativo,text="aqui tem um texto",foreground="#fff",background="#008")

txt1.place(x=10,y=10,width=150,height=30)


txt2=Label(aplicativo,text="texto numero 2", background="#00f",foreground="#aaa")

txt2.place()

aplicativo.mainloop()
