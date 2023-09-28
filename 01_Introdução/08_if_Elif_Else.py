"""
IF, ELSE, ELIF
Permite que o código siga por caminhos diferentes
de acordo com resultado de análises, equações e etc.

Sintaxe:

if (teste):
    Bloco que será executado se o teste retornar True
"""

'''
Exemplo de aplicação: 
Inserindo uma nota e testando as seguintes condições.
Se a nota for maior ou igual a 7 >>> O aluno está APROVADO.
Se a nota for menor que 7 e maior ou igual a 5 >>> o aluno está em RECUPERAÇÃO.
Se a nota for menor que 5 >>> o aluno está REPROVADO.
'''
# if 10 > 4:
#     print('Ok, é maior ')

# Condição simples
# n_aluno = input('Qual o nome do Aluno? ')
# nota = float(input('Qual foi a nota do Aluno? '))

# if nota >= 7:
#     print(f'O Aluno {n_aluno} foi Aprovado com a nota {nota}!')
# # else:
# #     print(f'O Aluno {n_aluno} foi Reprovado com a nota {nota}!')

# # Condição composta
# n_aluno = input('Qual o nome do Aluno? ').title()
# nota = float(input('Qual foi a nota do Aluno? '))

# if nota >= 7 and nota <= 10:
#      print(f'O Aluno {n_aluno} foi Aprovado com a nota {nota}!')
# elif nota >= 5 and nota < 7:
#      print(f'O Aluno {n_aluno} esta de recuperação com a nota {nota}!')
# elif nota >= 0 and nota < 5:
#      print(f'O Aluno {n_aluno} foi Reprovado com a nota {nota}!')
# else:
#      print('Nota Inválida')


# Condição aninhada
''' Vamos criar um sistema para validadar se o cliente
pode ou não ter uma Habilitação de acordo com a idade 
que irá informar.
'''

nome = input('Qual o Nome da pessoa? ').title()
idade = int(input('Qual a idade da pessoa?'))

if idade >= 18 and idade <= 130:
    print(f'{nome}, pode iniciar o processo de Habilitação:')
elif idade >= 16 and idade <18:
    resp = str(input('Tem autorização? [ S | N ]')).lower().strip()
    if resp == 's':
            print(f'{nome}, pode iniciar o processo de Habilitação:')
    elif resp == 'n':
        print(f'{nome}, NÃO pode iniciar o processo de Habilitação:')
    else:
         print('Resposta Inválida:')          
elif idade >= 0 and idade <16:
    print(f'{nome}, NÃO pode iniciar o processo de Habilitação:')
else:
    print('Idade iválida:')


# Operadores unitários >>> Dependem de um único valor >>> not, is
# Operadores binários >>> Dependem de mais que 1 valor >>> and, or



