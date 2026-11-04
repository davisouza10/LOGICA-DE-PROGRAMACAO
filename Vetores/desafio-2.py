jogadores = []

while True:
    print()
    print('=== GERENCIAMENTO DO ELENCO ===')
    print('1. Cadastrar jogador')
    print('2. Listar jogadores')
    print('3. Atualizar jogador')
    print('4. Excluir jogador')
    print('0. Sair')

    opcao = input('Opção: ')

    match opcao:
        case '1':
            nome = input('Nome: ')
            posicao = input('Posição: ')
            camisa = input('Camisa: ')
            jogadores.append([nome, posicao, camisa])
            print('Jogador cadastrado!')

        case '2':
            if len(jogadores) == 0:
                print('O elenco está vazio.')
            else:
                for i in range(len(jogadores)):
                    print(i + 1, '-', jogadores[i][0], '|', jogadores[i][1], '| #' + jogadores[i][2])

        case '3':
            if len(jogadores) == 0:
                print('O elenco está vazio.')
            else:
                for i in range(len(jogadores)):
                    print(i + 1, '-', jogadores[i][0], '|', jogadores[i][1], '| #' + jogadores[i][2])

                numero = int(input('Número do jogador: '))
                if numero >= 1 and numero <= len(jogadores):
                    nome = input('Novo nome: ')
                    posicao = input('Nova posição: ')
                    camisa = input('Nova camisa: ')
                    jogadores[numero - 1] = [nome, posicao, camisa]
                    print('Jogador atualizado!')
                else:
                    print('Jogador não encontrado.')

        case '4':
            if len(jogadores) == 0:
                print('O elenco está vazio.')
            else:
                for i in range(len(jogadores)):
                    print(i + 1, '-', jogadores[i][0], '|', jogadores[i][1], '| #' + jogadores[i][2])

                numero = int(input('Número do jogador: '))
                if numero >= 1 and numero <= len(jogadores):
                    jogadores.pop(numero - 1)
                    print('Jogador removido!')
                else:
                    print('Jogador não encontrado.')

        case '0':
            print('Saindo do programa...')
            break

        case _:
            print('Opção inválida!')