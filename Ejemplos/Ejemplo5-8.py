#Ejemplo de listas.

lista = ["Pepe","Maria","Luis","Moises"]

lista.append("Raul")
lista.insert(0,"Juan")
lista[0] = "Elias"

lista.remove("Luis")

print(f"Valores de la lista: {lista}")

cont = 0

for i in lista:

    print (f"El valor del indice {cont} es: {i}")

    cont = cont + 1