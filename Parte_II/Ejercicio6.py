# Ejemplo 4.6

# Se requiere un programa para determinar cuánto ahorrará una persona en
# un año, si al final de cada mes deposita variables cantidades de dinero;
# además, se requiere saber cuánto lleva ahorrado cada mes.

# ALGORITMO

# Variable      Descripción                 Tipo
#   AH          Ahorro mensual              Real
#   M           Contador del mes            Entero
#   CA          Cantidad que se va ahorrar  Entero

# Inicio
# Hacer AH = 0
# Hacer M = 1
# Mientras M <= 12
#   Leer CA
#   Hacer AH = AH + CA
#   Hacer M = M + 1
#   Escribir "El ahorro del mes: ", M, "es", AH
# Fin mientras
# Escribir "El ahorro final es: ", AH
# Fin

