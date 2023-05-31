#Crear tuplas a partir de listas o viceversa

cursos = ['Python', 'Django', 'Flask']
niveles = ('Básico', 'Intermedio', 'Avanzado')

# generamos una tupla a partir de una lista utilizando la funcion tuple
cursos_tupla = tuple(cursos)
print(cursos_tupla)

# Si quisieramos generar una lista a partir de una tupla usamos funcion list

niveles_tupla = list(niveles)
print(niveles_tupla)