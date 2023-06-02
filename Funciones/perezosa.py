# Distribución perezosa
"""
Imagina que tienes una caja de caramelos, pero no quieres sacar todos los caramelos al mismo tiempo.
 En lugar de eso, quieres tomarlos uno por uno, solo cuando realmente los necesitas.
Esto es similar a lo que sucede con la distribución perezosa.

En Python, la distribución perezosa se refiere a la idea de que los elementos de una secuencia (como una lista o un rango) no se generan todos de una vez, 
sino que se generan a medida que los necesitas.

Vamos a poner un ejemplo con una lista de números:
"""
numeros = [1, 2, 3, 4, 5]

""" Si queremos recorrer esta lista de números y multiplicar cada número por 2,
 podemos hacerlo usando un bucle for de esta manera: """

for numero in numeros:
    resultado = numero * 2
    print(resultado)

#Ejemplo
def pares():
    for numero in range(0, 100, 2):
        """return numero""" # Aquí no podemos usar return porque la funcion dejaría de ejecutarse en la primera
        # iteración, es decir en 0, no seguriria. Por eso para que sea una función generadora usamos yield
        yield numero
        print('Se reanuda la ejecución')

generador = pares()
print(next(generador)) #Hacemos uso de la palabra reservada next. Aquí se utilizará la función cada vez que la llamemos

print(next(generador))

print(next(generador))

print(next(generador))