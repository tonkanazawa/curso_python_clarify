"""
Primeiro passo para leitura, é abrir o arquivo, para isto usamos
a função OPEN(nomeArquivo).
O parâmetro é o nome ou caminho do arquivo.

O arquivo deve existir, caso contrário retornará erro FileNotFound.

Open apenas abre o arquivo, para ler seu conteúdo é necessário usarmos
a função nomeArquivo.read()
Por padrão o Open abre com o parâmetro r(read)
"""

# criando um arquivo txt
# a -> adc w -> sub r -> leitura (pode ser suprimido)
# tratamento de erro

# Exercício de aula: criar um todo (lista de tarefas)


# with open('./base/teste.txt', 'a', encoding='utf8') as arquivo:
#     arquivo.write('\nEstou só testando...')


# print(arquivo)

def todo():

    menu = int(input('1| Inserir\n2| Visualizar\n3| Sair\nOpção: '))

    match menu:
        case 1:
            with open('./lista/to-do.txt', 'a', encoding='utf8') as arquivo:
            tarefa = str(input('Digite uma Tarefa: '))
            arquivo.write(f'{tarefa}\n')

print(arquivo())

    # with open('./base/todo.txt', 'a', encoding='utf8') as todo:
    #     todo.write('Treinamento Clarify')