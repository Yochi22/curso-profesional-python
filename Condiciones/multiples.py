# Si queremos validar multiples condiciones para asi ejecutar diferentes bloques haremos uso de elif

calificacion = 10

"""
if calificacion == 10:
    print('Felicitaciones, obtuviste la nota máxima')
else:
    print('Aprobaste pero puedes hacerlo mejor')
"""

# Si queremos que Python evalue otras condiciones haremos uso de elif, irá después de if y antes de else

if calificacion == 10:
    print('Felicitaciones, obtuviste la nota máxima')
elif calificacion == 9 or calificacion == 8:
    print('Aprobaste pero puedes hacerlo mejor')
elif calificacion == 7 or calificacion == 6:
    print('Aprobaste')
else:
    print("Debes cursar nuevamente la materia")