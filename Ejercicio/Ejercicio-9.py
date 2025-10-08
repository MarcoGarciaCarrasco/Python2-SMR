numero = int(input("Introduce un número: "))

if numero < 0:

    print("El numero que has introducido es un numero negativo.")

else:

    if numero >= 0:
        rest = numero%2
        if rest == 1:
            print("Tu numero es positivo e impar")
        
        else:
            print("Tu numero es positivo y par")
