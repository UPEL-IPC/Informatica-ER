# Pida el número de invitados a una fiesta. Si se ingresó un número inferior
# a 10, pregunte por los nombres de cada persona y después de cada nombre,
# mostrar "[nombre] ha sido invitado". Si ingresó un número igual o mayor
# a 10, mostrar el mensaje "Mucha gente"

num = int (input ("Cuántos amigos invitará a la fiesta: "))
if num < 10:
    for i in range (0, num):
        name = input ("Ingrese el nombre")
        print (name, "ha sido invitado")
else:
    print ("Mucha gente")

    