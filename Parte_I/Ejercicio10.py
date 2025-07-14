# Este programa pide un número menor a 50 y entonces cuenta desde 50
# hasta ese número. Muestra el número que se ingresó

num = int ( input ("Ingrese un número menor que 50: "))
for i in range (50, num-1, -1):
    print (i)

    