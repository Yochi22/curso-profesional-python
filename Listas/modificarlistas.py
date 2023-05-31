listas_cursos = ['Python', 'Django', 'JavaScript', 'Ruby', 'C++', 'Java', 'Rust']

print(len(listas_cursos)) #Utilizamos len para saber la longitud de la lista

listas_cursos.append('MongoDB')


#Si queremos añadir un elemento en la lista en un indice en concreto utilizamos insert
listas_cursos.insert(2, "React")
print(listas_cursos)

#Podemos extender una lista a partir de otra utilizando el metodo extend
lista_cursos_2 = ['CSS', 'HTML', 'Figma', 'Tailwind']

listas_cursos.extend(lista_cursos_2)
print(listas_cursos)

# Si queremos eliminar un elemento de la lista utilizamos el método remove, que recibe como argumento el nombre del elemento
listas_cursos.remove('Rust')
print(listas_cursos)

#Si quremos eliminar un elemento por su indice, utilizamos la palabra reservada del
del listas_cursos[7]
print(listas_cursos)

# Para eliminar todos los elementos de la lista usamos el metodo clear()
listas_cursos.clear()
print(len(listas_cursos))