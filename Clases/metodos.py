# Para evitar conflictos hay que estandarizar atributos y nombres que va a poseer un objeto

class User: 
    def inicializar(self, username, password): #Obligatoriamente debe tener un parametro y por convencion seria self
    #añadimos atributos al objeto, self hace referencia al objeto perse
        self.username = username
        self.password = password
#En tiempo de ejecucion se van a añadir estos dos atributos a los dos objetos
user1 = User()
user2 = User()

user1.inicializar('User1', 'password1') # Se añaden al utilizar el metodo inicializar
user2.inicializar('User2', 'password2')

print(user1.__dict__)
print(user2.__dict__)

# PEro esta no es la mejor forma para inicializar atributos. Para eso está el metodo init