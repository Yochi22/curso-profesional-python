# Podemos crear funciones que reciban n cantidad de argumentos que deseemos/necesitemos
# Crearemos una funcion que permita calcular el promedio de un listado de numeros enteros

"""
def promedio (listado):
    return sum(listado) / len(listado)

resultado = promedio (10, 10, 25, 80, 14, 15.5, 69)

print(resultado)
"""

#Esto nos genera un error porque estamos pasando 7 argumentos y la función solo recibe 1 (listado)
# para esto, podemos encerrar los argumentos en una lista ([]) o podemos anteponer un asterisco al parámetro

"""
def promedio (*listado): #Esto convierte al parámetro en una tupla
    return sum(listado) / len(listado)

resultado = promedio (10, 10, 25, 80, 14, 15.5, 69)

print(resultado)
"""

#Por convención, todos estos parámetros que tengan el * deben ser nombrados args
# def promedio (*args)

# El uso del asterisco no limita para utilizar otros parámetros

def combinacion(p1, p2, *args, p4=5000):
    print(p1)
    print(p2)
    print(args)
    print(p4)

combinacion(25, 4, 8, 548, 2120)

# Otra forma de pasar valores al utilizar una funcion es con **, pero aqui ya no trabajaremos con tuplas
# trabajaremos con diccionarios

def promedio(*args):
     return sum(args) / len(args)



def usuarios(**kwargs): #Este nombre es por convención
    print(kwargs)
    print(type(kwargs))

usuarios(eduardo=[10, 10, 8], fernando=[6, 9, 5], Tania=[9, 9, 10])
    



 
