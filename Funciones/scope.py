# Veremos como se comportan las variables tanto fuera como dentro de las funciones

animal = 'Leon' #Esta variable es una variable global, al no ser creada dentro de un bloque

def imprimir_animal():
    animal = 'Ballena' # Esta variable al ser creada dentro de la funcion, es una variable local
    print(id(animal)) # Esto imprime ballena

imprimir_animal()

print (animal) # Esto imprime Leon
#Esto significa que las dos variables son totalmente distintas
# la va<riable global puede ser utilizada en cualquier bloque, la local no. Unícamente dentro del bloque donde se creo
# Si queremos verificar esto, podemos hacerlo mediante el id del elemento

print(id(animal))

# Si queremos modificar una variable global dentro de un bloque tenemos que usar la palabra reservada global
#  con eso le indicamos a python que no crearemos una variable nueva sino que usaremos la global

"""
global animal

animal = 'perro'

"""