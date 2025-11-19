from tkinter import *

window = Tk()

window.title("Bienvenido a mi App")

window.geometry("550x300")

def renombrar():
    resultado = "Bienvenido " + txt.get()
    lb2.configure(text=resultado)


lb = Label(window, text="Introduce un valor: " ,font=("Arial", 16))
lb.grid(column=0,row=0)

lb2 = Label(window, text=" " ,font=("Arial", 16))
lb2.grid(column=0,row=2)

txt = Entry(window, width=10)
txt.grid(column=2, row=0)

bt = Button(window,text = "Pulsame", command=renombrar)
bt.grid(column=0,row=1)


window.mainloop(), 