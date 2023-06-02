# Las funciones son ciudadanos de primera clase
def centigrados_a_farhenheit(grados):
    return grados * 1.8 + 32

"""print(centigrados_a_farhenheit(10))
print(centigrados_a_farhenheit(-10))
print(centigrados_a_farhenheit(8))"""

# podemos saber que vamos a usar una funcion pero no cuando, por eso podemos almacenar una funcion en una variable
my_function = centigrados_a_farhenheit
# una vez la funcion este dentor de la variable, para nosotros poder usarla lo haremos a traves de la variable

print(my_function(10))

# FUNCIONES LAMBDA
# Son funciones anonimas expresadas en una sola linea de codigo y no poseen un nombre porque realizan tareas pequeñas

# lambda <parámetros> : <cuerpo de la función>
funcion_grados = lambda grados: grados * 1.8 + 32
print(funcion_grados(25))

"""
Podemos usar funciones lambda de estas formas tambien

sin_parmetros = lambda : True
parametros_default = lambda p1=20, p2=10, p3=55 : p1 + p2 + p3
asterisco = lambda *args, **kwargs : len(args) + len(kwargs)

"""