class Animal():
    def comer(self):
        print('el animal come')


    def dormir (self):
        print('el animal duerme')

class Mascota(Animal): #Clase padre
    pass
   

class Felino:

    def cazar(self):
        print('El gato caza ratones')


class Perro(Mascota): #Clase hija
    pass

duke = Perro()
duke.comer()
duke.dormir()

# A dif de otros lenguajes de programación, python permite la herencia multiple, clases pueden heredar de
# multiples clases 

# La clase gato heredará de la clae mascota y clase felino
class Gato(Mascota, Felino):
    pass

limon = Gato()
limon.comer()
limon.dormir()
limon.cazar()

