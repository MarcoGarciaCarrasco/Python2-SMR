nombre = input("Introduce tu nombre: ")

edad = int(input(f"Hola, {nombre} introduce tu edad: "))

ganancias = int(input("Ahora introduce su nomina: "))

if (edad >= 18 and ganancias <1000):

    print(f"{nombre} ,estas capacitado para adquirir el descuento")

else:

    print(f" {nombre} ,no estas capacitado para recibir el descuento")