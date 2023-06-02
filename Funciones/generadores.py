"""
Imagina que tienes una máquina de hacer cupcakes. Esta máquina no produce todos los cupcakes a la vez,
 sino que los hace uno por uno a medida que los necesitas.
  Cada vez que necesitas un cupcake, la máquina produce uno y te lo entrega.
   ¡Los generadores son como esa máquina!

"""

def pares():
    for numero in range(0, 100, 2):
        """return numero""" # Aquí no podemos usar return porque la funcion dejaría de ejecutarse en la primera
        # iteración, es decir en 0, no seguriria. Por eso para que sea una función generadora usamos yield
        yield numero

for par in pares():
    print(par)

# La palabra reservada yield retorna valores sin que la función finalice. Pausa su ejecución y se
# reanuda desde donde quedo