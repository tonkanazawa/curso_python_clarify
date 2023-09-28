"""
 Faça um programa que leia ano de nascimento de 5 pessoas e no final
 mostre quantas pessoas já atingiram a maioridade e para aquelas que
 ainda atingiram, mostre a média em anos que faltam para chegarem a maior idade.
"""
n = 1
maior = 2005
menor = 0
menores = 0

for n in range(5):
    n += 1
    ano = float(input(f'Digite o ano da {n}ª pessoa: '))
        
    if ano <= 2005:
        print('Maior de Idade')
    else:
        print('Menor de Idade')
        menor += 1
        menores += ano

print(f'Temos {menor} pessoas menores de Idade e {5-menor} maiores')
print(f'A média de idade faltante para chegarem a maioridade é: {(menores / menor)-(maior)} Anos.)') 