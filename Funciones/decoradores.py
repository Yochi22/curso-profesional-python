# Reduciremos lineas de codigo duplicadas para que neustro código sea mas legible y facil de testear y mantener

#Los decoradores son funciones que toman como input una funcion y retornan una funcion 
"""
a -> funcion principal (decorador)
b -> funcion a decorar 
c -> funcion decorada

a (b) -> c
"""
# Podemos usar decoradores para extender funcionalidades a ua funcion, porque la funcion no puede ser
# modificada o no queramos hacerlo

# Estructura básica de los decoradores

def funcion_a(funcion_b):


    def funcion_C():
        print('Esto es un mensaje antes del llamado de la función')

        funcion_b()

        print('Esto es un mensaje después del llamado de la función')


    return funcion_C


@funcion_a
def saludar():
    print('Hola, esto es una función')

saludar()