#Ejemplo adviina el número con introducción a los bucles.

adivina = 5
intentos = 0

while (intentos < 3):
    numero_adivina = int(input("Introduce un número entre el 1 y el 10: "))
    if(numero_adivina == adivina):
        print(f"Has adivinado el número")
        break
    elif (numero_adivina<adivina):
        print(f"El número es mayor")
    else:
        print(f"El número es menor")
        intentos = intentos+1
else:
    print(f"No te quedan intentos, ¡Has perdido!")
