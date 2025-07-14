# Pida en qué dirección desea contar el usuario (hacia arriba o abajo). 
# Si dicen arriba, entonces pida en número máximo y cuente desde el 1
# hasta ese número. Si seleccionan hacia abajo, pida un número inferior a 20
# y cuente hacia abajo desde 20 hasta ese número. Si ingresó algo
# distinto a arriba o abajo, mostrar el mensaje "No entiendo"

direction = input ("¿Quiere contar hacia arriba o hacia abajo? (ar/ab)")
if direction == "ar":
    num = int ( input ("Ingrese el número máximo: "))
    for i in range (1, num + 1):
        print (i)
elif direction == "ab":
    num = int (input ("ingrese un número menor a 20: "))
    for i in range (20, num-1, -1):
        print (i)
else:
    print ("No entiendo")

    