import os

numero_serie = []

while True:
    os.system('cls' if os.name == 'nt' else 'clear')

    print('''
=== MERCADINHO DENDEZEIROS ===
1 - Cadastrar produtos
2 - Listar produtos
0 - Sair
''')

    opcao = input('Escolha uma opção: ').strip()

    match opcao:
        case '1':
            print('\n== CADASTRO DE NÚMEROS DE SÉRIE ==')
            nome = input('Digite o número de série: ').strip().upper()
            
            if nome == '':
                print('O número não pode ficar vazio.')
            elif nome in numero_serie:
                print(f'{nome} já está cadastrado.')
            else:
                numero_serie.append(nome)
                print('Produto cadastrado com sucesso!')
            
            input('\nPressione ENTER para continuar...')

        case '2':
            print('\n== NÚMEROS DE SÉRIE ==')
            if not numero_serie:
                print('O estoque está vazio.')
            else:
                for i, produto in enumerate(numero_serie, start=1):
                    print(f'{i}. {produto}')
                print(f'\nTotal de números de série: {len(numero_serie)}')
            
            input('\nPressione ENTER para continuar...')

        case '0':
            print('\nSaindo do programa...')
            break

        case _:
            print('Opção inválida!')
            input('\nPressione ENTER para continuar...')