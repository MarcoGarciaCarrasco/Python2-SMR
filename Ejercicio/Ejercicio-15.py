max = 0
exit = True
while (exit == True):

    value = input("Introduce un número:")

    if (value == "fin"):
        
        exit = False
    else:

        num = int(value)

        if(num> max):
            max = num

else:
    print(f"El valor mayor introducido es {max}")