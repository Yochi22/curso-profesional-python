 # Una buena practica de crear  funciones es que siempre quie podamos las documentemos
# Para ello nos apoyaremos del docstring
# El docstring será almacenado en el atributo __doc__ (Modulos, clases, metodos, funciones)    


def suma(numero_uno, numero_dos):
    """
    La función suma 2 numeros enteros

    Argumentos:
    numero_uno(int)
    numero_dos(int)

    Se retorna la suma de los parámetros

    #testear funcion se hace dentro del docstring

    Simulamos lo que hace la función, simulando una consola

    >>> suma(10, 20)
    30

    >>> suma(100, 200)
    300

    #En la terminal utilizaremos el siguiente comando python -m doctest documentar.py

    """
    return numero_uno + numero_dos

print(suma.__doc__)

# con el docstring podemos testear funciones
