# Necesitamos colocar en una pagina web la calificación de un alumno, la calificacion será de color verde
# si y solo si el alumno aprueba 
# en caso de que el alumno no apruebe, la califacion sera color rojo

"""calificacion = 10   
color = None"""

#Esta es una buena solución pero son muchas líneas de código para un problema tan sencillo
"""
if calificacion >= 7:
    color = 'Verde'
else: 
    color = 'Rojo'

print(calificacion, color)
"""

# Podemos usar el operador ternario

calificacion = 10
color = 'Verde' if calificacion >= 7 else 'Rojo'
print(calificacion, color)