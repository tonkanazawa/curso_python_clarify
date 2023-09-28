"""
Estrutura condicionais mais utilizada em menus,
funciona semelhante ao escolhaCaso do portugol
e switch case no java por exemplo...
"""
# Calculadora
menu = int(input('[1]SOMAR\n[2]SUBTRAIR\n[3]MULTIPLICAR\n[4]DIVIDIR\n[5]RESTO DA DIVISÃO\nDigite a Opção: '))

if menu >=1 and menu <= 5:
    n1 = float(input('Digite o Primeiro Valor: '))
    n2 = float(input('Digite o Segundo Valor: '))
    match menu:
        case 1:
            print(f'Soma = {n1+n2}')
        case 2:
            print(f'Sub = {n1-n2}')
        case 3:
            print(f'Mult = {n1*n2}')
        case 4:
            print(f'Div = {n1/n2}')
        case 5:
            print(f'Rest = {n1%n2}')
        case _:
            print('opção Inválida')
else:
    print('Valor Inválido')

''' 
Conclua o exemplo inserindo: 
    multiplicar, dividir e resto da divisão.
'''
