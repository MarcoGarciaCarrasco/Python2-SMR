#Ejercicio de suma cosmica en python


num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))

total = 0
contador = num1

while( contador <= num2):

    total = contador + total
    
    contador = contador + 1 

else:

    print (f"El sumatorio de {num1} y {num2} es: {total}")