numInput = int(input("Introduce un número del 1 al 20:"))

lista = [6,14,11,3,2,1,15,19]

def validaInput (num):

    if (num >=1) and (num <=20):
        return True
    else:
        return False
def validaLista ( num, lista):

    for i in lista:

        if i == num:
            return True
        else:
            return False
if validaInput (numInput) and validaLista(numInput,lista):

