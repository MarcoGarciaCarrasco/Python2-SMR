#Ejercicio 4

frase = input("Introduce una frase: ")
principio = int(input("Introduce el valor inicial: "))
longitud = int(input("Introduce el valor final: "))

final = principio + longitud

subcadena = frase[principio:final]

print(f"La subcadena es: {subcadena}")