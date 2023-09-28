"""
Agora vamos finalizar o IMC gerando uma saída
personalizada para o usuário de acordo com a
tabela:
______________________________________________
| Menor que 18.5      | Abaixo do peso       |
| Entre 18.5 - 24.9   | Peso Normal          |
| Entre 25.0 - 29.9   | Excesso de peso      |
| Entre 30.0 - 34.9   | Obesidade classe I   |
| Entre 35.0 - 39.9   | Obesidade classe II  |
| Maior ou igual 40.0 | Obesidade classe III |
----------------------------------------------

Mostre também a data deste resultado.
"""

nome = str(input('Qual o seu nome: ')).title()
idade = int(input('Qual a sua Idade: '))
peso = float(input('Qual é os eu peso: '))
altura = float(input('Qual é a sua altura: '))

import datetime

IMC = float(peso/altura**2)
# print(nome)
# print(idade)
# print(peso)
# print(altura)



# print(f'{nome}, baseado na sua Altura {altura} e o seu Peso {peso}, o seu IMC é {IMC:.2f}')
print(f'{nome}, baseado na sua Altura {altura} e o seu Peso {peso}, o seu IMC é {round(IMC,2)}')

if IMC < 18.5:
      (print('Você está Abaixo do peso'))
elif IMC >= 18.5 and IMC < 25:
      print('Você está no Peso Normal')
elif IMC >= 25 and IMC < 30:
      print('Você está com Excesso de peso')
elif IMC >= 30 and IMC < 35:
      print('Você está com Obesidade classe I')
elif IMC >= 35 and IMC < 40:
      print('Você está com Obesidade classe II')
elif IMC >= 40:
      print('Você está com Obesidade classe III')

data_atual = datetime.date.today()
print(data_atual)