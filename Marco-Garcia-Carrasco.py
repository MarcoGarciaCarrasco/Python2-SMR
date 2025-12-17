#------------------------------------------------
#           PARTE 1 - Datos del alumno
#------------------------------------------------

nombre = input("Introduce tu nombre: ")
edad = int(input("Introduce tu edad: "))

print(f"Bienvenido/a {nombre} edad: {edad} años.")

#------------------------------------------------
#           PARTE 2 - Introducción de notas
#------------------------------------------------

notas = []
datos = 0
notas_introducidas = int(input("Cuantas notas quieres introducir? "))

for i in range(0, notas_introducidas):
    datos = int(input("Introduce tus notas: "))
    notas.append(datos)
    notas_introducidas = notas_introducidas - 1
print(notas)

#------------------------------------------------
#           PARTE 3 - Procesamiento de datos
#------------------------------------------------

valor_inicio = 0

for valor_inicio in notas:
    valor_inicio + 1
print(f"Has introducido {valor_inicio} notas")

nota_max = notas[0]

for i in notas:
    if i > nota_max :
        nota_max = i
print(f"La nota mas alta es: {nota_max}")

nota_min = notas[0]

for i in notas:
    if i < nota_min :
        nota_min = i
print(f"La nota mas baja es: {nota_min}")

# nota_final = notas[0]

# for i in notas:
#     nota_final = i + i
# nota_media = nota_final / notas_totales

# print(f"La nota media es: {nota_media}")





#------------------------------------------------
#           PARTE 4 - Funciones
#------------------------------------------------

def es_par():
    global edad , nombre
    if edad % 2 == 0:
        print(f"{edad}(par)")
    else:
        print(f"{edad}(impar)")
    
es_par()


#------------------------------------------------
#           PARTE 5 - Analisis de notas
#------------------------------------------------

for i in notas:
    if i < 5:
        notas.remove(i)
print(notas)


#------------------------------------------------
#           PARTE 6 - Resultado final 
#------------------------------------------------

print(f"Alumno: {nombre}")

print(f"Edad: {edad}")

print(f"Has introducido: {valor_inicio} notas")

print(f"Nota media: ")

if 3 < 5:
    print(f"Estado: APROBADO")
else:
    print(f"Estado: SUSPENSO")

#------------------------------------------------
#           PARTE 7 - Visualización con tkinter
#------------------------------------------------

