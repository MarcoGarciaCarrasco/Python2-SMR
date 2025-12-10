import random
total = 0
partidasGanadas = 0

def juegoDados():
    global total, partidasGanadas
    total += 1
    dadohumano = random.randint(1,6)
    dadopc = random.randint(1,6)

    if dadohumano > dadopc:
        print("Has ganado!!")
    else:
        print("Has perdido")

while True:
    continuar = input("Bienvenido al juego de los dados. ¿Desea jugar una partida? (S/N)")

    if (continuar == "S"):

        juegoDados()

    elif (continuar == "N"):

        print(f"Gracias por jugar, partidas jugadas {total}, ganadas: {partidasGanadas} de ellas")
        break
    else:
        print("Por favor, introduce 'S' para sí o 'N' para no.")