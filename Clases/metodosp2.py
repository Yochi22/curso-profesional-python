# al igual que con los atributos, a los metodos podemos clasificarlos en dos tipos
# metodos de instancias y metodos de clase

# M E T O D O S  D E  C L A S E
class Circulo:
    pi = 3.141592

    @classmethod
    def area(cls, radio): #Este parametro hace referencia a la clase perse
        return cls.pi * (radio ** 2)

resultado = Circulo.area(14)
print(resultado)