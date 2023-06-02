# Las funciones en python tambien pueden ser anidadas, es decir funciones pueden poseer otras funciones

"""
def operacion():

    def deposito(cantidad, balance):
        return cantidad + balance




    def retiro(cantidad, balance):
        if cantidad <= balance:
            return balance - cantidad    
        else:
            return None



    print(deposito(10, 20))
    print(retiro(13, 7))
operacion()
"""

# Ahora hagamos un refacto de todo

def operacion(cantidad, balance, tipo='deposito'):

    def deposito(cantidad, balance):
        return cantidad + balance




    def retiro(cantidad, balance):

        if cantidad <= balance:
            return balance - cantidad    
        else:
            return None

    if tipo == 'deposito':
        return deposito(cantidad, balance)
    elif tipo == 'retiro':
        return retiro(cantidad, balance)


resultado = operacion(10, 30)
print(resultado)
