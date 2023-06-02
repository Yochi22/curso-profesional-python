# consiste en que una clase hija pueda modificar los comportamientos de metodos de la clase padre
# para que se adecue a las necesidades de la clase hija

class Animal():
    def comer(self):
        print('el animal come')


    def dormir (self):
        print('el animal duerme')

class Mascota(Animal): #Clase padre
    # Acá vamos a sobreescribir el método comer, basta con volverlo a definir
    def comer(self):
        print('La mascota es carnivora')
   

class Felino:

    def cazar(self):
        print('El gato caza ratones')


class Gato(Mascota, Felino):
    
    def __init__(self, nombre):
        self.nombre = nombre
        #Acá vamos a sobreescribir comer y dormir para gato

    def comer(self):
        print(f'{self.nombre} come')

    def dormir(self):
        print(f'{self.nombre} duerme')
        # Si aqui quisieramos usar ejecutar metodo de neustra clase padre utilizamos super()
        super().comer()

Limon = Gato('Limón')
Limon.comer()
Limon.dormir()
Limon.cazar()

# Habrá ocasiones que aunque ya hayamos sobreescrito los metodos, tengamos que ejecutarlos
# utilizaremos la funcion super. Nos permite acceder a la clase padre inmediata para ejecutar sus metodos