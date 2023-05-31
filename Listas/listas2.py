lista_cursos = ['Python', 'Django', 'JavaScript', 'Ruby', 'Java']

#Python nos da la posibilidad de crear sublistas
sub_lista = lista_cursos[0:3] #Aquí no se tomaría JavaScript, únicamente sería 0, 1 y 2
print(sub_lista)

#[start:end] le damos un numero inicial y un numero final, sabiendo qwue esté ultimo no cuenta
# [start:] obtenemos los ultimos elementos de la lista a partir del indice que se indica ejemp [1:]
# [:end] obtenemos los primeros elementos de la lista, omitimos el indice inicial ejemp [:4] 
# [start:end:skio] aquí podemos hacer un salto de lista
sub_lista = lista_cursos[1:5:2] #aquí le decimos que nos traiga del indice 1 al 05, haciendo saltos de 02
print(sub_lista)