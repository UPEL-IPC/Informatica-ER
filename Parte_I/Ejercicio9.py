# Este programa pide un número entre 1 y 12 y muestra la tabla de multiplicar
# de ese número

num = int (input ("Ingrese un número entre 1 y 12: "))
for i in range(1, 13):
    answer = i * num
    print (i, "x", num, "=", answer)
    