nombre = input("Introduce tu nombre: ")

edad = int(input(f"Hola, {nombre} introduce tu edad: "))

ganancias = int(input("Ahora introduce su nomina: "))

if edad >= 18:

    if ganancias < 1000:

        print(f"{nombre} ,si estas capacitado para adquirir el descuento")

    else:

        print(f"{nombre} ,no tienes descuento, tu salario es mayor.")

elif ganancias > 1000 :

    print(f"{nombre} ,no estas capacitado para recibir el descuento ya que no cuentas con los requisito de edad minimos para este descuento.")

else:
    print(f"{nombre} ,no estas capacitado para recibir el descuento ya que no cumples los requisitos de edad minimos.")

