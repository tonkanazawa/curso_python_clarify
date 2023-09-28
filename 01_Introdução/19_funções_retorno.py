# Com retorno
# com mais de 1 retorno
# Desafio de aula: Cara ou Coroa


# Função diz oi

# def diz_oi():
#     return 'Oi'

# print(diz_oi())

# Função canta parabéns

# def canta_parabens():
    # return 'Parabéns pra você...'

# print(canta_parabens())

# # Função soma 2 valores

# def soma():
#     a = 10
#     b = 5
#     return a + b

# print(soma() * 10)


# Desafio de aula: Cara ou Coroa

from random import random, randint
# print(random())
# print(randint(1,10))


def caracoroa():
    a = randint(1,2)
    print(a)

    if a == 1:
        return 'Cara'
    else:
        return 'Coroa'
    
 
print(f'O resultado deu {caracoroa()}')
