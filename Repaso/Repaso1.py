import random
total = 0
partidasGanadas = 0
partidasPerdidas = 0
partidasEmpatadas = 0


def juegoDados():
    global total, partidasGanadas, partidasPerdidas, partidasEmpatadas
    total = total + 1
    dadohumano = random.randint(1,6)
    dadopc = random.randint(1,6)

    if dadohumano > dadopc:
        print(f"Has obtenido {dadohumano} y tu contrincante ha obtenido un {dadopc}, asi que has ganado!!!!")
        partidasGanadas = partidasGanadas + 1
    elif dadohumano == dadopc:
        print(f"Has obtenido {dadohumano} y tu contrincante ha obtenido un {dadopc}, habeis empatado.")
        partidasEmpatadas = partidasEmpatadas + 1
    else:
        print(f"Has obtenido {dadohumano} y tu contrincante ha obtenido un {dadopc}, has perdido")
        partidasPerdidas = partidasPerdidas + 1

while True:
    continuar = input("Bienvenido al juego de los dados. ¿Desea jugar una partida? (S/N): ")

    if (continuar == "S"):

        juegoDados()

    elif (continuar == "N"):

        print(f"Gracias por jugar, partidas jugadas {total}.")
        print(f"Has perdido {partidasPerdidas}")
        print(f"Has ganado {partidasGanadas}")
        print(f"Has emptado {partidasEmpatadas}")
        break
    else:
        print("Por favor, introduce 'S' para sí o 'N' para no.")