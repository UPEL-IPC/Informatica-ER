# Asigne 0 a la variable 0 para iniciar. Mientras total sea igual o menor que 50
# pida un número. Agregue el número a total e imprima el mensaje "El total es...[total]"
# Pare el ciclo cuando total sea superior a 50.

total = 0
while total <= 50:
    num = int (input ("Ingrese un número: "))
    total = total + num
    print ("El total es...", total)

    