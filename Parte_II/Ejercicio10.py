# Ejemplo 4.11

# Una persona se encuentra en el kilómetro 70 de la carretera Aguascalientes-
# Zacatecas, otra se encuentra en el km 150 de la misma carretera, la
# primera viaja en dirección a Zacatecas, mientras que la segunda
# se dirige a Aguascalientes, a la misma velocidad. Realice un programa
# para determinar en qué kilómetro de esa carretera se encontrarán.

# ALGORITMO

# Variable      Descripción                     Tipo
#   KA          Primer punto en la carretera    Real
#   KB          Segundo punto en la carretera   Real
#   R           Distancia entre los puntos      Entero

# Inicio
# Hacer KA = 70
# Hacer KB = 150
# Hacer R = KB - KA
# Mientras R > 0
#   Hacer KA = KA + 1
#   Hacer KB = KB - 1
#   Hacer R = KB = KA
# Fin mientras
# Si R = 0
#   Entonces
#       Hacer KA = KB
#   Si no
#       Hacer KA = KA - 0.5
# Fin compara
# Escribir "Punto de encuentro= ", KA
# Fin

