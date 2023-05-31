lista = [0, 20, 15, 2335, 45, 26, 8, -496]

#Si queremos ordenar la lista podemos utilizar el método sort

lista.sort() #Al dejar eso de forma default, lo ordenará de forma ascendente
print(lista)

lista.sort(reverse=True) #Aquí lo hariamos de forma descendente
print(lista)

#Si queremos obtener el numero mayor y menor de la lista podemos organizarla de forma ascendente y luego obtenerlos por sus indices
lista.sort()
print(lista[0])
print(lista[7])

# Pero hay una mejor forma con funciones min y max sin necesidad de ordenar la lista
print(min(lista))
print(max(lista))

# Si queremos conocer si un elemento se encuentra o no dentro de nuestra lista utilizamos in 
#Si queremos saber si el elemento no se encuentra en la lista utilizamos not

print(10 in lista)
print('Joselin' not in lista)

# Si después de verificar que un elemento se enuentra en la lista queremos saber su indice, podemos usar index
print(15 in lista)

index = lista.index(15)
print(lista)
print(index)