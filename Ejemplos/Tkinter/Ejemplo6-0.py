# Mi primer ejemplo de Tkinter

from tkinter import *

window = Tk()

window.title("Bienvenido a mi App")

window.geometry("550x300")

contador = 0

def renombrar():

    global contador
    contador +=1
    lb.configure(text=contador)

lb = Label(window,text = "Mi primer Label", font=("Arial", 25))

lb.grid(column=0,row=0)

bt = Button(window,text="Púlsame", comman=renombrar)
bt.grid(column=0, row=1)

window.mainloop()