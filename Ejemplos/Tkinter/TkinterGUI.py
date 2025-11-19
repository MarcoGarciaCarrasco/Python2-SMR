
from tkinter import *

from tkinter import messagebox

"""Inicializo variables """

letras="TRWAGMYFPDXBNJZSQVHLCKEO"

ventana = Tk()
ventana.geometry("370x200")
ventana.config(bg="#E8773F")
ventana.title("Bienvenido al Sistema")
ventana.iconbitmap('Images/DNIElectronico.png')

etiqueta1 = Label(ventana,text="Bienvenido ", font=("Arial Bold", 16),bg="#E8773F", fg="#FEFEFE")
etiqueta2 = Label(ventana,text="Nombre: ", font=("Arial ", 14),bg="#E8773F", fg="#FEFEFE")
etiqueta3 = Label(ventana,text="DNI: ", font=("Arial ", 14), bg="#E8773F", fg="#FEFEFE")

etiqueta1.grid(column=1, row=0)
etiqueta2.grid(column=0, row=1)
etiqueta3.grid(column=0, row=2)

cajaNombre = Entry(ventana, width=10)
cajaNombre.grid(column=1, row=1)

cajaDNI = Entry(ventana, width=10)
cajaDNI.grid(column=1, row=2)


def Pulsar():

	nombre = "Bienvenido al sistema " + cajaNombre.get()

	dni = cajaDNI.get()

	ind = int(len(dni))
	letra = dni[ind-1] # sería igual a decor: dni[-1]
	print("DNI: ",dni)
	print("Tamaño", ind)
	print("Letra", letra)

	numeros = int(dni[0:ind-1]) #sería igual a decir: int(dni[0:-1])

	indCorrecto = numeros % 23

	letraCorrecta = letras[indCorrecto]

	if (letraCorrecta == letra):
		
		print ("DNI correcto")
		messagebox.showinfo("Sistema 2SMR", nombre)

	else:
		print ("DNI incorrecto")
		messagebox.showerror("Sistema 2SMR","DNI Incorrecto")

boton = Button(ventana,text="Púlsame", command=Pulsar)

boton.grid(column=1,row=3)

imagen = PhotoImage(file="dni.png")
fondo = Label(ventana, image= imagen).place(x=220,y=10)

ventana.mainloop()
