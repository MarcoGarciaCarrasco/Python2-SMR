import random

adivina = random.randint(1,100)
intentos = 0

while (intentos <10):

    numeroAdivina = int(input("Introduce número del 1 al 100: "))

    if (numeroAdivina == adivina):

        print(f"Has adivinado el número!!!!")
        break
    elif (numeroAdivina<adivina):
        print(f"El número es menor")
        intentos = intentos + +1