#Comprimir elementos para generar tuplas

lista = [1, 2, 3, 4, 5]
tupla = (10, 20, 30, 40, 50)

#con la funcion zip() podemos combinar valores de la tupla y lista

resultado = zip(tupla, lista) #Esto retorna un dato tipo zip
resultado = tuple(resultado) #Con la palabra tuple, generamos la tupla
print(resultado)