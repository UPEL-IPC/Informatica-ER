# Asigne 0 a total. Pida al usuario que ingrese 5 números y después de cada
# número pida si quiere incluir ese número. Si dicen que sí, entonces
# agregue el número al total. Si no quieren, no lo agregue al total.
# Al final debe mostrar el total

total = 0
for i in range (0,5):
    num = int(input ("Ingrese un número: "))
    ans = input ("¿Desea agregar el número? (s/n)")
    if ans == "s":
        total = total + num
print (total)


