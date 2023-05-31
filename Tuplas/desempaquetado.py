#Anterirmente aprendimos a crear y definir variables en una sola linea de código
#Ahora haremos lo mismo utilizando tuplas

numeros = (1, 2, 3, 4)
uno, dos, tres, cuatro = numeros #Se asignan los valores en orden

# Si en dado caso nosotros no conocemos de antemano la cantidad de elementos que posee nuestra tupla
#Tiene 6 elemento y nosotros estamos asignando 5 variables, qué pasa? se obtendría un error
# En ese caso reemplazariamos la variable 5 por *resto_valores, aqui le indicamos a python que almacene el resto a partir del 4 valor

numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
uno, dos, tres, cuatro, *resto_valores = numeros
#Aqui se crearia una lista a partir de los valores que no fueron desempaquetados
print(resto_valores)

#Si simplemente quisiera omitir esos valores ponemos *_ indicando que es una lista, si solo queremos omitir usamos _
#Pero, si quisieramos obtener los numeros del 1 al 4 y omitir 5, 6 y 7 pero obtener 9 y 10
# Seria       asi numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
#             uno, dos, tres, cuatro, *_, nueve, diez = numeros