#Ejemplo de FOR in range ()

max = 0
numbers = [12,34,23,56,78,56,90,67,45,57,23,1,34,5]
for num in numbers:
    if(num > max):
        max = num
else:
    print(f"El valor mayor introducido es {max}")