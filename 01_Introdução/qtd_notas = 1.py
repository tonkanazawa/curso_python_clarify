qtd_notas = 
soma_notas = 0
while qtd_notas <= 4:
    nota = float(input(f'Digite a {qtd_notas}ª nota: '))
    if nota >= 0 and nota <= 10:
        qtd_notas += 1
        soma_notas += nota
    else:
        print('Nota Inválida. Digite Novamente')

media = soma_notas / qtd_notas

print(f'A média do aluno é: {media}')

if media >= 7 and media <= 10:
    print('Aluno Aprovado!')
elif media >= 5 and media < 7:
    print('Aluno de Recuperação')
else:
    print('Aluno Reprovado') 