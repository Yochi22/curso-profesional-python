# Aprenderemos a eliminar elementos del diccionario

diccionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Eliminar con del

del diccionario['a']
print(diccionario)

# Eliminar con metodo pop

valor = diccionario.pop('b')
print(valor)
print(diccionario)

# Para eliminar todos los elementos del diccionario usaremos clear
diccionario.clear()
print(diccionario)