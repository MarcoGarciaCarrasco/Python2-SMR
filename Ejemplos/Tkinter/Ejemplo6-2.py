import tkinter as tk

ventana = tk.Tk()
ventana.title("Consulta tu DNI")
ventana.geometry("550x300")

imagen = tk.PhotoImage(file='C:\Users\mgarcar0106\Desktop\Python-Tema1\Ejemplos\Tkinter\DNIElectronico.png')
imagenPeq = imagen.subsample(4,4)

lblImage = tk.Label(ventana, image=imagen)

lblImage.grid(column=0,row=0)

ventana.mainloop()