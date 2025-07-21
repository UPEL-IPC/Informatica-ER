# Ejemplo 4.12

# Un empleado de la tienda "Tiki Taka" realiza N ventas durante el día,
# se requiere saber cuántas de ellas fueron mayores a $1000, cuántas
# fueron menores o iguales a $500. Además, se requiere saber el monto
# de lo vendido en cada categoría y de forma global. Realice un programa
# que permita determinar lo anterior.

# ALGORITMO

# Variable      Descripción                     Tipo
#   N           Número de ventas                Real
#   CN          Contador de las ventas          Real
#   A           Ventas mayores a mil            Entero
#   B           Ventas mayores a 500 pero       
#               menores o iguales a 1000        Entero
#   C           Ventas menores o iguales a 500  Entero
#   V           Monto de la venta               Real
#   T1          Total de lsa ventas tipo A      Real
#   T2          Total de las ventas tipo B      Real
#   T3          Total de las ventas tipo C      Real
#   TT          Total de las ventas             Real

# Inicio
# Leer N
# Hacer A = 0, B = 0, C = 0
# Hacer T1 = 0, T2 = 0, T3 = 0
# Hacer TT = 0
# Hacer CN = 1
# Mientras CN <= N
#   Leer V
#   Si V > 1000
#       Entonces
#           Hacer A = A + 1
#           Hacer T1 = T1 + V
#       Si no
#           Si V > 500
#               Entonces
#                   Hacer B = B + 1
#                   Hacer T2 = T2 + V
#               Si no
#                   Hacer C = C + 1
#                   Hacer T3 = T3 + V
#           Fin compara
#   Fin compara
#   Hacer TT = TT + V
#   Hacer CN = CN + 1
# Fin mientras
# Escribir "Las ventas y el total de ventas 1 es: ", A, T1
# Escribir "Las ventas y el total de ventas 2 es: ", B, T2
# Escribir "Las ventas y el total de ventas 3 es: ", C, T3
# Escribir "El total de ventas es: ", TT
# Fin

