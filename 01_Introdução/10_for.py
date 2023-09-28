# """
# For >>> Utilizada quando se sabe a quantidade de repetições,
# de forma que é obrigatório determinar o final da execução do laço.

# Sintaxe:
# for item in iteravel:
#     bloco que será executado

# * Range -> inicio, fim, passo
# * Enumerate -> Permite acesso ao índice
# """

# # sintaxe

# for item in range:
    
# # range(inicio, fim, passo)
# # range(1,10,1)

# soma = 0

# for contador in range(5):
#     print(soma)
#     num = int(input('Digite um valor: '))
#     soma += num

# print(soma)


# '''
# Desafio de aula: Crie um sistema que receba 4 notas 
# e calcule a média, ao fim apresente a média e situção
# do aluno, sendo:
# >7 aprovado, >5 em recuperação e <5 reprovado.
# '''

# nota1 = float(input('Digite a 1º nota: '))
# nota2 = float(input('Digite a 2º nota: '))
# nota3 = float(input('Digite a 3º nota: '))
# nota4 = float(input('Digite a 4º nota: '))

# media = (nota1 + nota2 + nota3 + nota4) / 4

# print(media)

# if media >= 7 and media <= 10:
#     print('Aluno Aprovado!')
# elif media <= 5 and media < 7:
#     print('Aluno de Recuperação')
# else:
#     print('Aluno Reprovado') 

notas = 0

for n in range(1,5):
    nota = float(input(f'Digite a {n}ª nota: '))
    notas += nota

media = notas / n

print(f'A média do aluno é: {media}')

if media >= 7 and media <= 10:
    print('Aluno Aprovado!')
elif media >= 5 and media < 7:
    print('Aluno de Recuperação')
else:
    print('Aluno Reprovado') 



# for contador in range(0,101,10):
# #     print(contador, end=' ')

# nome = 'Leonardo'
# print(nome[0:8])
# print(nome[0:7])

