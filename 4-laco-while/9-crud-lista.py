import os

lista_produtos = []

while True:
    os.system('cls')

    print('''
=== MERCADINHO DENDEZEIROS ==
1 - Cadastrar produtos
2 - Lista produtos
0 - Sair)
''')

    opcao = int(input('Escolha uma opção: '))

    match opcao:
        case 1:
            print('\n== CADASTRO DE PRODUTOS ==')

            nome = input('Nome do novo produto: ').strip().upper()
            if nome == '':
              print('O nome não pode ficar vazio.')
            elif nome in lista_produtos:
              print(f'{nome} já está cadastrado.')
            else:
              lista_produtos.append(nome)
            print('Produtos cadastrado com secesso!')
            input('Pressione tecla para continuar...')
        case 2:
            print('\n== PRODUTOS NO ESTOQUE ==')
            if len(lista_produtos) == 0:
                print('O estoque está vazio.')
            else:
                for i, produto in enumerate(lista_produtos):
                  print(f'{i+1}. {produto}')

                print(f'Total de produtos: {len(lista_produtos)}')
                input('Pressione uma tecla para continuar...')

        case 0:
            print('Fim do programa.')
            break
        case _:
            print('Opção invalida!')
            input('Pressione uma tecla para continuar...')

