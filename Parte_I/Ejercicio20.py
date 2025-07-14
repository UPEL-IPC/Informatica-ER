# Crear un variable llamada compnum y asignarle el valor 50. Pedir al
# usuario que ingrese un número. Mientras no adivine el número almacenado
# en compnum, dígale que es muy bajo o muy alto. Si ingresa adivina
# en número de compnum, mostrar el mensaje "Bien hecho, te tomó [count] intentos"

compnum = 50
guess = int (input ("PUedes adivinar el número en el que estoy pensando: "))
count = 1
while guess != compnum:
    if guess < compnum:
        print ("Muy bajo")
    else:
        print ("Muy alto")
    count = count + 1
    guess = int (input ("Inténtalo otra vez: "))
print ("Bien hecho, te tomó", count, "intentos")

