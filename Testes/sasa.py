import os

jogadores = []
def cadastrar():
    nome = input('Escreva o nome do jogador(a): ')
    posicao = input('Escreva a posição do jogador(a): ')
    numero = int(input('Escreva o número da camisa: '))
    jogador = [nome, posicao, numero]
    jogadores.append(jogador)
    print('Jogador cadastrado!')
    
def listar():
    if len(jogadores) == 0:
        print('Nenhum jogador encontrado.')
    else:
        for i in range(len(jogadores)):
            print(f'{i + 1}. {jogadores[i][0]} | {jogadores[i][2]}')

while True:
    os.system('cls')
    
    print('''
== LISTA DE JOGADORES ==
1 - Cadastrar jogador
2 - Listar jogadores
3 - Atualizar jogador
4 - Excluir jogador
0 - Sair
''')
    opcao = input('Escolha o número das opções: ').strip()
    match opcao:
        case '1':
            cadastrar()
        case'2':
            listar()
        case '3':
            print('Atualizar')
        case '4':
            print('Excluir')
        case '0':
            print('O programa Acabou!')
            break
        case _:
            print('Opção Inválida!')
    input('Pressione ENTER para continuar...')