titulo_curso = 'Curso profesional de Python'

for caracter in titulo_curso:

    if caracter == 'P':
        continue

    print(caracter)

# El uso de continue hará que el ciclo salte a la siguiente iteracion, por lo cual el código que esté despues
# de esta palabra, no será ejecutado, se salta
