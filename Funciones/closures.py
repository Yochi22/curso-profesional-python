# Se encuentra fuertemente relacionado con funciones anidadas y alcances de las variables
def saludar():
    def mostrar_mensaje():
        print('Hola, nos encontramos en el curso de Python')

    return mostrar_mensaje

respuesta = saludar()
 
respuesta() #Aquí usamos la variable 