# Podemos alinearlos/justificarlos utilizando metodos

mensaje = 'Hola Mundo'

# METODOS
# ljust -> permitirá justificar a la izquierda
# rjust -> permitirá justificar a la derecha
# center -> permitirá centrar el texto

mensaje = mensaje.ljust(20) #El numero hace referencia a la cantidad de espacios


# Justificar a la derecha
mensaje = mensaje.rjust(40) #El numero hace referencia a la cantidad de espacios


# Centrar
mensaje = mensaje.center(40) #El numero hace referencia a la cantidad de espacios

print(mensaje)