#podemos asignar valores a nuestras variables con los operadores logicos
#Python analiza de izq a derecha y asignará el primer valor verdadero, en este caso Cody


variable = 'Cody' or 'Codigofacilito'
print(variable)

# Ejemplo, en este caso listado es false
listado = []
nombre = 'Cody'

variable_2 = listado or nombre
print(variable_2)