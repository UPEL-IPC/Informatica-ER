# Ejemplo 4.14

# Una empresa les paga a sus empleados con base en las horas trabajadas en
# la semana. Realice un programa para determinar el sueldo semanal de N
# trabajadores y, además, calcule cuánto pagó la empresa por los N empleados.


# ALGORITMO

# Variable      Descripción                     Tipo
#   N           Número de trabajadores          Entero
#   HT          Horas trabajadas                Real
#   PH          Pago por hora                   Real
#   SS          Sueldo semanal                  Real
#   I           Contador del ciclo de empleado  Entero

# Inicio
# Leer N
# Desde I = 1 hasta I = N
#   Leer HT, PH
#   Hacer SS = HT * PH
#   Escribir "El sueldo de trabajador", I, " es ", SS
#   Hacer TOT = TOT + SS
# Fin desde
# Escribir "Pago total es: ", TOT
# Fin

