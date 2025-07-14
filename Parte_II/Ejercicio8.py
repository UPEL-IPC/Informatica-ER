# Ejemplo 4.9

# Realice un programa para generar N elementos de la suceción de Fibonacci
# (0,1,1,2,3,5,8,13,...). 

# El planteamiento del algoritmo correspondiente se hace a partir del 
# análisis de la sucesión, en la que se puede observar que un tercer
# valor de la serie está dado por la suma de los dos valores previos,
# de aquí que se asignan los dos valores para sumar (0, 1), que dan
# la base para obtener el siguiente elemento que se busca, además,
# implica que el ciclo se efectue dos veces al menos.

# ALGORITMO

# Variable      Descripción                         Tipo
#   A, B        Valores iniciales o previos         Entero
#   C           Valor generado                      Entero
#   M           Contador del ciclo                  Entero
#   N           Número de elementos de la serie     Entero

# Inicio
# Leer N
# Hacer A = 0
# Hacer B = 1
# Escribir A, B
# Hacer M = 1
# Mientras M <= (N-2)
#   Hacer C = A + B
#   Escribir C
#   Hacer A = B
#   Hacer B = C
#   Hacer M = M + 1
# Fin mientras
# Fin

