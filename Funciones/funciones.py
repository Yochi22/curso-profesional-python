# Para crear una funcion tenemos que usar la palabra reservada def
# A la funcion hay que pasar variables, estas variables se llaman parametros. aunque no es necesario

"""
def suma(): 
    numero_uno = int(input('Ingresa el primer número entero: ')) # Recordemos que esto genera un string, necesitamos un entero
    numero_dos = int(input('Ingresa el segundo número entero: '))


    resultado = numero_uno + numero_dos
    print(resultado)

suma()
"""

# En la mayoria de los casos las funciones van a necesitar valores de entrada para su funcionamiento
# estas variables son parametros y se definen dentro del parentesis. Ejemplo

"""
def suma(numero_uno, numero_dos): 
    
    resultado = numero_uno + numero_dos
    print(resultado)

numero_uno = int(input('Ingresa el primer número entero: ')) # Recordemos que esto genera un string, necesitamos un entero
numero_dos = int(input('Ingresa el segundo número entero: '))

suma(numero_uno, numero_dos)
"""

# Las funciones puede retornar un resultado. También puede que queramos almacenar ese valor y no solo imprimirlo

def suma(n1, n2): 
    

    return n1 + n2, 'La función retorna 2 valores'

numero_uno = int(input('Ingresa el primer número entero: ')) # Recordemos que esto genera un string, necesitamos un entero
numero_dos = int(input('Ingresa el segundo número entero: '))

resultado, _ = suma(numero_uno, numero_dos)

print('El resultado es: ', resultado)
