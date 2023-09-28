"""
While >>> Utilizada quando se sabe a quantidade de repetições e
quando não se sabe.
* Necessário atentar para o critério de parada.

Sintaxe >>>  while expressão_bool:
                    Execução.

Expressão será executada enquanto for verdadeira.
Expressão Booleana >>> Toda expressão onde o resultado
for Verdadeiro ou Falso.

Ex.
resposta = ''
    while resposta != 'SIM':
            resposta = 'input'
"""

# repetindo um texto 5 vezes com for
# for n in range(5):
#     print('batata')



# repetindo um texto 5 vezes com while
# numero = 0
# while numero < 5:
#     print(f'Digite um valor: {numero}')
#     numero += 1



# validando uma senha de forma simples
# senha_cadastrada = str(input('Cadastre uma senha: ')).lower()
# senha = ''

# while senha != senha_cadastrada:
#     senha = str(input('Digite sua senha para entrar: ')).lower()
#     if senha != senha_cadastrada:
#         print('\033[31m Senha Incorreta!!! \033[m')

# print('\033[32m\nAcesso permitido...\033[m')

# sem o if
# senha_cadastrada = str(input('Cadastre uma senha: ')).lower()
# senha = ''

# while senha != senha_cadastrada:
#     senha = str(input('Digite sua senha para entrar: ')).lower()
#     print('\033[31m Senha Incorreta!!! \033[m')

# print('\033[32m\nAcesso permitido...\033[m')

qtd_notas = 1
soma_notas = 0
while qtd_notas <= 4:
    nota = float(input(f'Digite a {qtd_notas}ª nota: '))
    if nota >= 0 and nota <= 10:
        soma_notas += nota
        qtd_notas += 1
    else:
        print('Nota Inválida. Digite Novamente')


media = soma_notas / qtd_notas + 1

print(f'A média do aluno é: {media}')

if media >= 7 and media <= 10:
    print('Aluno Aprovado!')
elif media >= 5 and media < 7:
    print('Aluno de Recuperação')
else:
    print('Aluno Reprovado') 
