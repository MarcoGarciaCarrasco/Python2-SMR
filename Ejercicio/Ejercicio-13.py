count = 3

while (count > 0):

    name = input("Introduce el nombre de usuario: ")
    password = input("Introduce la contraseña: ")

    if (name == "root") and (password == "toor"):

        print("bievenido al sistema")
        break
    else:
        count = count - 1
        print(f"Nombre o contraseña incorrectas, le quedan {count} intentos")

else:
    print("Has agotado el número de intentos")


