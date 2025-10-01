frase = input("Introduce una frase: ")
letra_buscar = input("Introduce la letra a cambiar: ")
letra_nueva = input("Introduce la letra a nueva: ")

repeticion = frase.count(letra_buscar)

frase_nueva = frase.replace(letra_buscar, letra_nueva)

print(f"Número de apariciones de {letra_buscar} es {repeticion}, frase final será: {frase_nueva}")