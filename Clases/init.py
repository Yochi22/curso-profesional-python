# Para definir e inicializar atributos a un objeto al momento de crearlo haremos uso del metodo  init

 # El método init también permite inicializarlos, a través de parámetros
class Usuario:
    def __init__(self, username, password):
        self.username = username
        self.password = password

user1 = Usuario('user1', 'password1')
user2 = Usuario('user2', 'password2')

print(user1.__dict__)
print(user2.__dict__)
