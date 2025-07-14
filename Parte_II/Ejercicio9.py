# Ejemplo 4.10

# Una empresa tiene el registro de las horas que trabaja diariamente un
# empleado durante la semana (seis días) y requiere determinar el total
# de éstas, así como el sueldo que recibirá por las horas trabajadas.

# ALGORITMO

# Variable      Descripción                     Tipo
#   D           Contador del ciclo de días      Entero
#   PH          Pago por hora                   Real
#   SH          Horas trabajadas en la semana   Entero
#   HT          Horas trabajadas por día        Entero
#   SU          Sueldo semanal                  Real

# Inicio
# Hacer SH = 0
# Leer PH
# Hacer D = 1
# Mientras D <= 6
#   Leer HT
#   Hacer SH = SH + HT
#   Hacer D = D + 1
# Fin mientras
# SU = SH * PH
# Escribir "Las horas laboradas son = ", SH
# Escribir "El sueldo es= ", SU
# Fin

