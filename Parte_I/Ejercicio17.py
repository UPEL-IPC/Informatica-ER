# Pida un número. Siga preguntando hasta que ingrese un número sobre 5
# y muestre el mensaje "El número ingresado fue [numero]" y pare el programa

num = 0
while num <= 5:
    num = int (input ("Ingrese un número: "))
print ("El último número ingresado fue", num)

