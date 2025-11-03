contador = 1
maxnumber = int()


while(contador <= 5):
    number = int(input(f"Introduce el {contador} número - "))
    contador = contador + 1
    if number > maxnumber:
        maxnumber = number

else:
    print(f"El número mas grande es {maxnumber}")