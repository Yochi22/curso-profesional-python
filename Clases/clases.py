# Para crear nuestras clases usaremos la palabra reservada class
# Las clases se usan con CamelCase

class Usuario : 
    pass # Es una palabra reservada que nos permite dejar el bloque vacío

cody = Usuario()
print(cody)

# en python nosotros podremos dividir los atributos en dos tipos
# atributos de clase y atributos de instancia

# Atributos de clase: Son los atributos que le pertenecen a una clase, para usarlos hay que usar la clase
# Atributos de instancia: Son los atributos que le pertenecen a un objeto, para usalros hay que usar el objeto

# A T R I B U T O S  D E  C L A S E
"""

class User:
    username = 'Yochi'
    email = ''

# Modificar un atributo

User.username = 'Yochi22'

print(User.username) 

"""

# A T R I B U T O S  D E  I N S T A N C I A S
class User: 
    username = 'Yochi'
    email = ''

# Creamos un obejto de tipo usuario
# Se verifica si existe dentro del objeto, al no existir se verifica que exista dentro de la clase
# Lo podemos usar pero solo para lectura, no podemos modificar este atributo de clase   
user1 = User()
print(user1.username)    
