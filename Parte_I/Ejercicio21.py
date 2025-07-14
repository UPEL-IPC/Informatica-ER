# Pida que ingrese un número entre 10 y 20. Si ingresa un valor mejor a 10
# mostrar el mensaje "Muy bajo" y pedir que lo intente nuevamente. Si
# ingresa un número superior a 20, mostrar el mensaje "Muy alto" y
# pedir que lo intente de nuevo. Repita esto hasta que ingrese un 
# número entre 10 y 20, entonces muestre el mensaje "Gracias"

num = int ( input ("Ingrese un número entre 10 y 20: "))
while num < 10 or num > 20:
    if num < 10:
        print ("Muy bajo")
    else:
        print ("Muy alto")
    num = int (input ("Intente de nuevo: "))
print ("Gracias")

