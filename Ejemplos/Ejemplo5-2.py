numero = int(input("Introduce un numero entre el 0 y el 10 :"))

adivina = 7

if (numero > adivina):

    input(f"El número {numero} es mayor")

elif (numero == adivina):
    print(f" Has adivinado el número!!!")

else:
    print(f" El número {numero} es menor")