"""
Cadastre 3 produtos no estoque, cada produto precisa ter:
- nome
- preço
- data e hora que foi cadastrado
- Nome do Funcionário

Em seguida, permita que os produtos sejam visualizados.
"""


# estoque = []

# for cont in range(3):

#     produto = dict(
#     nome = str(input('Nome do Produto: ')),
#     preco = float(input('Preço do Produto: '))

#     )
#     estoque.append(produto)

# for produto in estoque:
#     for chave, valor in produto.items():
#         print(f'{chave} | {valor}')
#     print()



# for produto in estoque:
#     print(estoque)



# def cadastrar_produto():
#     produto = dict(
#         nome_produto = str(input('Nome: ')).title(),
#         preco = float(input('Preço: R$ ')),
#         nome_funcionario = str(input('Funcionário: ')).title(),
#         dt_cadastro = datetime.now().strf.time("%d.%m.%Y | %H:%M")
#                 )

from datetime import datetime

estoque = []

while True:

    menu = int(input('1| Cadastrar\n2| Visualizar\n3| Sair\nOpção: '))
    

    match menu: 
        
        case 1: #cadastrando produto
            produto = dict(
                nome_produto = str(input('Nome: ')).title(),
                preco = float(input('Preço: R$ ')),
                nome_funcionario = str(input('Funcionário: ')).title(),
                dt_cadastro = datetime.now().strftime("%d.%m.%Y | %H:%M")
                    )
            estoque.append(produto)
        case 2:
            for i, p in enumerate(estoque):
                print(f'n\Produto: {i+1}')
                for chave, valor in p.items():
                    print(f'{chave} → {valor}')
            print()

        case 3:
            break
        case _:
            print('Opção Inválida\n')


