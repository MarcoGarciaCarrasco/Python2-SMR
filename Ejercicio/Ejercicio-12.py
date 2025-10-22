#Ejercicio de suma de pares e inmpares en python


num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))

totalpar = 0
totalimpar = 0
contador = num1

while( contador < num2):

    if(contador%2 == 0): 
    
        totalpar = contador + totalpar
    else:
        totalimpar = contador + totalimpar
    
    contador = contador + 1 

else:

    print (f"El sumatorio de los pares entre {num1} y {num2} es de {totalpar} y el sumatorio de los impares es {totalimpar}" )