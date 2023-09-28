"""
FUNÇÔES
Uma forma de organizar o código e garantir que ele 
possa ser reutilizado. Ideal que cada função seja 
responsável por uma tarefa...
"""

# Função diz oi

def diz_oi():
    print('Oi')

# diz_oi()

# Função canta parabéns

def canta_parabens():
    print('Parabéns pra você...')

# canta_parabens()

# # Função soma 2 valores

# def soma():
#     n1 = int(input('Digite o primeiro valor: '))
#     n2 = int(input('Digite o segundo valor: '))
#     print(f'A soma dos valores é: {n1 + n2}')

# soma()

# Todas as funções juntas

def soma():
    diz_oi()
    canta_parabens()
    n1 = int(input('Digite o primeiro valor: '))
    n2 = int(input('Digite o segundo valor: '))
    print(f'A soma dos valores é: {n1 + n2}')

soma()