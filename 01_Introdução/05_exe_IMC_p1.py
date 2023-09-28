"""
Vamos iniciar um programa que receba:
 nome = str(input('Qual o seu nome: ')).title()
 idade = int(input('Qual a sua Idade: '))
 peso = float(input('Qual é os eu peso: '))
 altura = float(input('Qual é a sua altura: '))

Retorne o IMC do usuário.

IMC =   Peso
      --------
       Altura²
"""

nome = str(input('Qual o seu nome: ')).title()
idade = int(input('Qual a sua Idade: '))
peso = float(input('Qual é os eu peso: '))
altura = float(input('Qual é a sua altura: '))


IMC = float(peso/altura**2)
print(nome)
print(idade)
print(peso)
print(altura)


print(f'{nome}, baseado na sua Altura {altura} e o seu Peso {peso}, o seu IMC é {IMC:.2f}')
print(f'{nome}, baseado na sua Altura {altura} e o seu Peso {peso}, o seu IMC é {round(IMC,2)}')

if IMC <= 18.5:
      (print('VOCÊ ESTÁ ABAIXO DO PESO'))
else:
      (print('VOCÊ ESTÁ ACIMA DO PESO'))
