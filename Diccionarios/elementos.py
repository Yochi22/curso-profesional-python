# Obtener elementos de un diccionario

diccionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Es importante recordar que obtendremos el valor de una llave siempre y cuando la llave exista o dará error

"""
valor = diccionario['d']
print(valor)
"""

# Si queremos evitar ese error, podemos hacer uso de la palabra reservada in
"""
print('a' in diccionario)
"""

# Utilizando el metodo get del diccionario, podremos obtener el valor de una llave de forma segura
# sin arriesgarnos a que el programa falle si la llave no existe

valor = diccionario.get('d')
print(valor)
# Si buscamos una llave que no existe, nos retornara none, es simplemente la ausencia de un valor
#No habrá un error. También podemos dejar un mensaje

valor = diccionario.get('z', 'La llave solicitada no existe')
print(valor)

# Podemos buscar una llave, si esta no existe, podemos proceder a crearla
valor = diccionario.setdefault('x', 25)
print(valor)
print(diccionario)