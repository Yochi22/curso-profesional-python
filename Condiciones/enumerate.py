#La funcion enumarate nos permite enumerar cada uno de los elementos dentro de una coleccion

numeros = [10, 20, 30, 40, 50]

for indice, numero in enumerate(numeros):
    print(indice, numero)

#Igualmente podemos decir desde que indice queremos comenzar, esto pasando el número como argumento pero esto
# no es común y realmente no se usa
for indice, numero in enumerate(numeros, 2):
    print(indice, numero)