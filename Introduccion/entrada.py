#Aprenderemos a obtener valores que el usuario ha ingresado a través de su teclado

#Si queremos cambiar el tipo de valor string a entero podemos usar la palabra reservada int, ejemplo


nombre_completo = input('Por favor, ingresa tu nombre completo: ')

edad = int(input ('Ingresa tu edad: '))


#Aquí cambiaremos string a decimal
altura = float(input('Ingresa tu altura: '))


#Aquí obtendremos un tipo booleano a partir de lo que el usuario ingrese en el teclado
autorizacion = input('¿Autorizas el tratamiento de datos? (si/no) ') == 'si'

print(nombre_completo)
print(edad)
print(altura)
print(autorizacion)