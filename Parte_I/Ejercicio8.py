# Modifica el programa anterior para pedir un número. Muestra su nombre
# una letra a la vez en cada línea y repite esto en número de veces
# ingresado.

num = int ( input ("Ingrese un número: "))
name = input ("Ingrese su nombre: ")
for x in range (0, num):
    for i in name:
        print (i)