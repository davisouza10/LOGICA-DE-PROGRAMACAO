import os

numero_produto = []

while True:
    os.system('cls')

    print('''
=== MERCADINHO DENDEZEIROS ===
1 - Cadastrar nome dos produtos
2 - Listar numero de produtos
3 - Atualizar produto
4 - Remover produto
5 - Buscar produto
0 - Sair
''')

    opcao = int(input('Escolha uma opção: '))

    if opcao == 1:
        nome = input('Digite o nome do produto: ').strip()
        if nome == '':
            print('O nome do produto não pode ser vazio.')
        elif nome.lower() in [p.lower() for p in numero_produto]:
            print('Produto já cadastrado.')
        else:
            numero_produto.append(nome)
            print('Produto cadastrado com sucesso!')

    elif opcao == 2:
        if len(numero_produto) == 0:
            print('Nenhum produto cadastrado.')
        else:
            print(f'Total de produtos: {len(numero_produto)}')
            for i, produto in enumerate(numero_produto, start=1):
                print(f'{i} - {produto}')

    elif opcao == 3:
        antigo = input('Digite o nome do produto que deseja atualizar: ').strip()
        if antigo in numero_produto:
            novo = input('Digite o novo nome: ').strip()
            if novo == '':
                print('O novo nome não pode ser vazio.')
            else:
                posicao = numero_produto.index(antigo)
                numero_produto[posicao] = novo
                print('Produto atualizado com sucesso!')
        else:
            print('Produto não encontrado.')

    elif opcao == 4:
        nome = input('Digite o nome do produto que deseja remover: ').strip()
        if nome in numero_produto:
            numero_produto.remove(nome)
            print('Produto removido com sucesso!')
        else:
            print('Produto não encontrado.')

    elif opcao == 5:
        nome = input('Digite o nome do produto que deseja buscar: ').strip()
        if nome in numero_produto:
            posicao = numero_produto.index(nome)
            print(f'Produto "{nome}" encontrado na posição {posicao + 1}.')
        else:
            print('Produto não encontrado.')

    elif opcao == 0:
        print('Saindo do sistema... Até logo!')
        break

    else:
        print('Opção inválida! Tente novamente.')

    input('\nPressione Enter para continuar...')
