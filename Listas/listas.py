#Hay dos formas de crear listas, diciendole a la variable que será una lista con la palabra list() o con []
#LAs posiciones son como en los arrays de JavaScript
#           0      1     2     3
lista = ['String', 10, 15.6, True]

#Las listas nos permiten almacenar distintos tipos de valores pero es recomendable almacenar solo un tipo de dato

lista_string = ["Hola", "Joselin"]

lista_enteros = [19, 20, -17]

lista_floats = [1.55, -2.457, 5.5]

lista_booleanos = [90 > 1, True, False, 25 == 25, 12 != 12]
print(lista)

#Usaremos el indice o posicion de cada elemento para obtenerlo
#                 -5        -4          -3          -2       -1
#                  0         1           2           3        4  

lista_cursos = ['Python', 'Django', 'JavaScript', 'Ruby', 'Java']

lista_cursos[4] = 'C++'

print(lista_cursos)

#Python nos da la posibilidad de crear sublistas
sub_lista = lista_cursos[0:3] #Aquí no se tomaría JavaScript, únicamente sería 0, 1 y 2
print(sub_lista)