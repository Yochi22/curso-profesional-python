# Permite ejecutar N veces un bloque de codigo hasta que una condicion se cumpla

"""
contador = 1 

while contador <= 10: #Este bloque se ejecutará siempre y cuando el valor sea igual o menor a 10
    print(contador)


    contador = contador + 1
    """

# Cuando contador valga 11, la condición deja de cumplirse
# El ciclo while se usará cuando no sepamos la cantidad de iteraciones, como en este caso sabemos que son 10
# Hay un mejor ejemplo para esto

#Imprimamos en consola la cantidad de digitos que posee un numero entero

numero = 123456789
#Nuestro contador de digitos empieza en 0
contador_digitos = 0

while numero >= 1: #La condición se rompe cuando el numero queda en 0,1

    contador_digitos = contador_digitos + 1 # Aqui aumenta el contador, segun la division de digitos

    numero = numero / 10 #Aqui dividimos nuestro numero en digitos

print(contador_digitos)

