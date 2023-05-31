# Metodos mas utilizados al momento de usar strings, no son los únicos pero si mas usados
#el metodo split permite generar una lista a partir de un string
# Join permite generar un string a partir de una lista
"""
lenguajes = 'Python Ruby Java Rust C++ C' # Los espacios serían la coma
listado_lenguajes = lenguajes.split()
print(listado_lenguajes)

lenguajes = 'Python-Ruby-Java-Rust-C++-C'
listado_lenguajes = lenguajes.split('-') # Aquí le especificamos que el espaciado se dará con el guion
print(listado_lenguajes)
"""
#Aquí convertiremos una lista en un string
lenguajes = ['Python', 'Ruby', 'Java', 'Rust']

string_lenguajes = ' '.join(lenguajes) # Si dentro de '' colocamos / dividiriamos las palabras con el simbolo
print(string_lenguajes)

