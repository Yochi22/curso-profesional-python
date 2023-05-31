# Los strings en Python son inmutables
# Pero podemos generar strings a partir de otros

nombre = 'Joselin'
apellido = 'Lozada'

"""
nombre_completo = nombre + ' ' + apellido
print(nombre_completo)

Esta es una forma de concatenar usando el + """

#Esta es otra forma de concatenar utilizando porcentaje s
"""
nombre_completo = 'Ms . %s %s.' %(nombre, apellido)
print(nombre_completo)
"""
# Aquí se sustituyen los porcentajes por los argumentos dados

# Método Format. Aquí utilizamos {} que serán sustituidos por los argumentos de las variables y utilizamos el metodo .format
"""
nombre_completo = 'Ms. {} {} {}.'.format(nombre, apellido, 'Mendoza')
print(nombre_completo)
"""

#También podemos nombrar directamente a los placeholder, aquí usariamos parametros
"""
nombre_completo = 'Ms. {nombre} {primer_apellido} {segundo_apellido}'.format(
    nombre = nombre,
    primer_apellido = apellido,
    segundo_apellido = 'Mendoza'
)
print(nombre_completo)
"""

#Los FStrings Nos permiten generar nuevos strings a partir de otros utilizando interpolacion
"""
nombre = 'Joselin'
apellido = 'Lozada'
"""
# Antes del string base hay que interponer la f, para que Python analice que vamos a usar interpolacion
"""
nombre_completo = f'Ms. {nombre} {apellido} {"Mendoza"}' 
print(nombre_completo)
"""



