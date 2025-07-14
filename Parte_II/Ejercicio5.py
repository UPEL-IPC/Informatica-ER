# Ejemplo 4.5

# Se requiere un programa para obtener la estatura promedio de un grupo
# de personas, cuyo número de miembros se desconoce, el ciclo debe
# efectuarse siempre y cuando se tenga una estatura registrada.

# ALGORITMO

# Variable      Descripción                 Tipo
#   C           Contador de personas        Entero
#   ES          Estatura de cada persona    Real
#   SU          Suma de las estaturas       Real
#   PR          Estatura promedio           Real

# Inicio
# Hacer SU = 0
# Leer ES
# Hacer C = 0
# Mientras ES > 0
#   Hacer SU = SU + ES
#   Leer ES
#   Hacer C = C + 1
# Fin mientras
# Si c = 0
#   Entonces
#       Escribir "No hay estaturas"
#   Si no
#       Hacer PR = SU / C
# Fin compara
# Escribir PR
# Fin

