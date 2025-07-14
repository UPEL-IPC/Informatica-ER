# Ejemplo 4.15

# Una empresa les paga a sus empleados con base a las horas trabajadas en
# la semana. Para esto, se registran los días que laboró y las horas de cada
# día. Realice un programa para determinar el sueldo semnal de N trabajadores
# y además calcule cuánto pagó la empresa por los N empleados.

# ALGORITMO

# Variable      Descripción                     Tipo
#   N           Número de trabajadores          Entero
#   HT          Horas trabajadas                Real
#   PH          Pago por hora                   Real
#   SH          Suma de horas semanales         Entero
#   DT          Días laborados                  Entero
#   SS          Sueldo semanal                  Real
#   I           Contador del ciclo de empleado  Entero
#   D           Contador del ciclo de días      Entero

# Inicio
# Leer N
# Desde I = 1 hasta N
#   Leer DT, PH
#   Hacer SH = 0
#   Desde D = 1 hasta DT
#       Leer HT
#       Hacer SH = SH + HT
#   Fin desde
#   Hacer SS = SH * PH
#   Escribir "El sueldo del trabajador", I, " es ", SS
#   Hacer TOT = TOT + SS
# Fin desde
# Escribir "El total que se pagó es ", TOT
# Fin

