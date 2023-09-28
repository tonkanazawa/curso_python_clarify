"""  
HERANÇA é um tipo de relacionamento entre classes 
que significa que uma classe é outra.

POLIMORFISMO é a capacidade que uma subclasse tem de 
ter métodos com o mesmo nome de sua superclasse, e o 
programa saber qual método deve ser invocado, 
especificamente (da super ou sub). 
"""
class Pessoa:

    def __int__(self, nome, cpf):
        self._nome = nome
        self._cpf = cpf

    def getNome(self):
        return self._nome
    



class Cliente(Pessoa):
    def __init__(self, nome, cpf, email):
        super().__init__(self, nome, cpf)
        self._email = email
    
    def getNome(self):
        return self._email


# Classe Funcionáro (nome, cpf, matricula)

class Funcionario(Pessoa):

    def __init__(self, nome, cpf, matricula):
        Pessoa().__init__(self, nome, cpf)
        self._matricula = matricula
    
    def getNome(self):
        return self._Matricula


cliente1 = Cliente('Léo', 123, 'leo@gmail.com')
print(cliente1.getNome())

func1 = Funcionario('Ton', 234, 'CA22')
print(func1.getNome())
