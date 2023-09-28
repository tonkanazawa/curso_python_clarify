"""
Uma classe é um modelo ou blueprint que descreve os atributos (variáveis) 
e comportamentos (métodos) comuns a um grupo de objetos relacionados. 

No contexto da orientação a objetos, uma classe funciona como uma base 
para criar instâncias, chamadas de objetos. Cada objeto criado a partir 
de uma classe possui os atributos e métodos definidos pela classe, 
mas com valores e estados específicos. 
"""

# Criar uma classe cliente   
# Molde, método construtor.
'''
class Cliente:
    def __init__(self, nome, cpf, email):
        self._nome = nome
        self._cpf = cpf
        self._email = email
    
    def getNome(self):
        return self._nome


cliente1 = Cliente('Léo', 123, 'leo@gmail.com')
print(cliente1.getNome())

'''
'''
#__________________________________________
# Classe Funcionáro (nome, cpf, matricula)



class Funcionario:
    def __init__(self, nome, cpf, matricula):
        self._nome = nome
        self._cpf = cpf
        self._matricula = matricula
    
    def getNome(self):
        return self._nome

    def getCpf(self):
        return self._cpf
   
    def getMatricula(self):
        return self._matricula
    
func1 = Funcionario('Ton', 234, 'CA22')
print(func1.getNome())
print(func1.getCpf())
print(func1.getMatricula())

#__________________________________________
'''


