def todo():
    while True:
        try:
            menu = int(input('1| Inserir\n2| Visualizar\n3| Sair\nOpção: '))
        except ValueError:
            print('Opção Inválida...\n')
            
        match menu:
            case 1:
                try:
                    with open('./lista/to-do.txt', 'a', encoding='utf8') as arquivo:
                        while True:
                            tarefa = str(input('Digite uma Tarefa ou S para sair: '))

                            if tarefa.lower() != 's':
                                arquivo.write(f'{tarefa}\n')
                            else:
                                break


                except FileNotFoundError:
                    print('Não encontrado...')
            case 2:
                try:
                    with open('./lista/to-do.txt', 'r', encoding='utf8') as arquivo:
                        print(arquivo.read())
                except FileNotFoundError:
                    print('Não encontrado...')
            case 3:
                break
            case _:
                print('Opção Invalida')


print(todo())
