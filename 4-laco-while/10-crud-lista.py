import os

numero_serie = []

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
            print('\n== CADASTRO DE NÚMEROS DE SÉRIE ==')

            nome =int(input('Digite o número de série: ')).strip().upper()
            if nome == '':
              print('O número não pode ficar vazio.')
            elif nome in numero_serie:
              print(f'{nome} já está cadastrado.')
            else:
              numero_serie.append(nome)
            print('Produtos cadastrado com secesso!')
            input('Pressione tecla para continuar...')
        case 2:
            print('\n== NUMERO DE SÉRIE ==')
            if len(numero_serie) == 0:
                print('O estoque está vazio.')
            else:
                for i, produto in enumerate(numero_serie):
                  print(f'{i+1}. {produto}')

                print(f'Total de números de séreis {numero_serie}')
                input('Pressione uma tecla para continuar...')

        case 0:
            print('Fim do programa.')
            break
        case _:
            print('Opção invalida!')
            input('Pressione uma tecla para continuar...')
