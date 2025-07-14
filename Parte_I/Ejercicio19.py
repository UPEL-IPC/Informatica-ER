# Pida el nombre de alguien que quiere invitar a una fiesta. Luego,
# muestre el mensaje "[nombre] ha sido invitado" y sume 1 a la cuenta.
# Preguntar si desea invitar a alguien más. Repetir el procedimiento
# hasta que se responda que no se desea invitar a nadie más. Mostrar
# al final cuántas personas vendrán a la fiesta.

again = "s"
count = 0
while again == "s":
    name = input ("Ingrese el nombre del invitado: ")
    print (name, "ha sido invitado")
    count = count + 1
    again = input ("¿Desea invitar a alguien más? (s/n)")
print ("Usted ha invitado a", count, "personas a la fiesta")

