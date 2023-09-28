"""
Python possui o que chamamos de tipagem fraca.

STRING por padrão, sempre estará entre
    ' ' aspas simples
    " " aspas duplas
    ''' ''' aspas simples triplas
    E aspas duplas trilas, como esta que cerca este comentário.
"""
# Fatiamento de String
# Metodos (podem ser utilizados na mesma construção.)
# Número inteiro - int | ex: 123 65 98 90
# Float >>> Números reais/ decimais separados por . e não ,
# correto
# errado
# Booleano >>> 2 constantes - Verdadeiro (True) e falso (false).

# dado = 'Milton'
# print(type(dado))

dado = str(input('Digite seu nome: '))


print(dado)
print(dado.lower()) # letras minúsculas
print(dado.upper()) # letras maiúsculas
print(dado.title()) # 1ª letra maiúscula em cada palavra
print(dado.capitalize()) # 1ª letra maiúscula em só uma palavra

print(len(dado))
print(len(dado.strip()))
print(dado.lower().count('a'))      
print(dado.strip().count(' '))              

# Inteiro 
numero = 10
prin(numero * 100)

# Float
altura = 1.83

# Booleano 
status = True
status = False
