# Se solicita un nombre y un número. Si el número es menor que 10, entonces
# se muestra el nombre ese número de veces; sino, muestra el mensaje
# "Muy alto" 3 veces

name = input ("Ingrese su nombre: ")
num = int (input ("Ingrese un número: "))
if num < 10:
    for i in range (0, num):
        print (name)
else:
    for i in range (0,3):
        print ("Muy alto")

        