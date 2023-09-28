qtd_notas = 0
soma_notas = 0

while True:
    nota = float(input(f'Digite a {qtd_notas+1}ª nota: '))
    if nota >= 0 and nota <= 10:
        soma_notas += nota
        qtd_notas += 1
    else:
        print('Nota Inválida. Digite Novamente')
    if qtd_notas == 4:
        break
    
media = soma_notas / qtd_notas

print(f'A média do aluno é: {media}')

if media >= 7 and media <= 10:
    print('Aluno Aprovado!')
elif media >= 5 and media < 7:
    print('Aluno de Recuperação')
else:
    print('Aluno Reprovado') 