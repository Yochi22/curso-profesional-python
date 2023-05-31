# Para crear condiciones haremos uso de la palabra reservada if

resultado = 50
# Crearemos una condición que muestre un mensaje si y solo si es mayor que 10

"""
resultado = resultado > 10 
if resultado: 
    print('La variable cumple con la condición.')
"""

# Pero para optimizar podemos hacerlo así
if resultado > 10 and resultado < 20:
    print('La variable cumple con la condición')

# Si queremos que se ejecute otro bloque porque no se cumple la condicion, usamos la palabra reservada else

else: 
    print('La condición no se cumple')
