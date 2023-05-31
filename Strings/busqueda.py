# Buscar un string dentro de otro string, podemos utilizar el metodo count

titulo_curso = 'Curso profesional de Python'

#Usamos el string donde queremos buscar y recibe de argumento el string que queremos buscar
"""
contador = titulo_curso.count('Python')

print(contador)
"""

#Otra forma de saber si existe un string dentro de un string es con la palabra reservada in. 

print('Python' in titulo_curso)

# El uso de mayúsculas y minúsculas importa, para estandarizar podemos convertir todo a mayuscula o minuscula
# Utilizando Upper o Lower

print('python' in titulo_curso.lower()) #Como buscamos en minuscula, usamos lower

# Tambien podemos negar usando not in

print('codigofacilito' not in titulo_curso.lower()) 

# Utilizando el metodo startswith podemos conocer si un string comienza o no con otro string
# Miremos si titulo_curso empieza con la palabra curso

print(titulo_curso.startswith('Curso'))

#Tambien podemos saber si el string está al final del string con el metodo endswith