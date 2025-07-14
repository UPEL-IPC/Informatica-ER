# Este programa solicita un número que se agregará al total. Esto sucederá
# mientras total sea menor que 100

total = 0
while total < 100:
    num = int (input ("Ingrese un número: "))
    total = total + num
print ("El total es", total)

