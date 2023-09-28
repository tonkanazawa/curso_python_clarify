while True:
    menu = int(input('[1]SOMAR\n[2]SUBTRAIR\n[3]SAIR\nOpção: '))

    if menu == 1 or menu == 2:
        n1 = int(input('Valor 1: '))
        n2 = int(input('Valor 2: '))

    match menu:
        case 1: print(f'Resultado da adição: {n1 + n2}')
        case 2: print(f'Resultado da subtração: {n1 - n2}')
        case 3: break
        case _: print('Opção Inválida...\n')
        

