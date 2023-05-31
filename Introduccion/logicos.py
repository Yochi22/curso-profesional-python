# and, or y not 
# Estos operadores nos permiten comparar tipos booleanos y obtendremos como resultado un valor booleano

#and compara valores booleanos, las comparaciones deben ser verdaderas para que el resultado sea verdadero

resultado_final = True and True and 100 > 20
print(resultado_final)

#or una de las comparaciones debe ser verdadera para que el resultado sea verdadero
resultado = True or False or False
print(resultado)
#Si usamos paréntesis es posible combinar los operadores lógicos, por ejemplo

resultado_prueba = True and (False or 50 > 10)
print(resultado_prueba)

#not permite negar un valor booleano, convierte True a Falsa y viceversa
prueba = not True 
print(prueba)