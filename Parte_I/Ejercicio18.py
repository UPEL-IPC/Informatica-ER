# Pida un número y luego otro número. Sume esos 2 números y pregunte
# si quiere agregar otro número. Si responde "s", pida otro número 
# y siga sumando hasta que no responda "s". Cuando se detenga el ciclo,
# muestre el total

num1 = int( input ("Ingrese un número: "))
total = num1
again = "s"
while again == "s":
    num2 = int (input ("Ingrese otro número: "))
    total = total + num2
    again = input ("¿Quiere agregar otro número? (s/n)")
print ("El total es", total)
