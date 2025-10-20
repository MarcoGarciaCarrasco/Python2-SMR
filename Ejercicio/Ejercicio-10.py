nombre = input ("Introduce tu Nombre: ")

clave = input ("Introduce la Clave: ")

usuarioSistema = "Marco"

claveSistema = "1234"

if (clave == claveSistema) and (nombre == usuarioSistema):

    print(f"Bienvenido al sistema {nombre}")

elif (nombre == usuarioSistema):
    print(f" La clave es incorrecta")

elif (clave ==claveSistema):
    print(f"El nombre es incorrecto")

else:
    print(f" La clave y el nombre son incorrectos")



#elif claveSistema (clave == claveSistema) and (nombre != usuarioSistema):

    #print("Su usuario es incorrecto")#