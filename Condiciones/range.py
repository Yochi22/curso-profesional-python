#Utilizando esta funcion podremos crear una secuencia de numeros enteros, los cuales se pueden iterar
# ejemplo, rago de 0 a 10
# Automaticamente empezará en 0 y el numero del argumento no será tomado en cuenta
rango = range(11) # 0 - 10

for valor in rango:
    print(valor)

#Si queremos comenzar desde otro número que no sea cero
for valor in range (5, 21):
    print(valor)

#Podemos usar un tercer argumento, en este caso significaría los saltos, por ejemplo
#Rango del 5 al 21 (21 no es tomado en cuenta) con saltos de dos en dos

for valor in range (5, 21, 2):
    print(valor)
