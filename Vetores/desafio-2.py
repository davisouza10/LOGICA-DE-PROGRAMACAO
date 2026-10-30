import os

# Cada jogador é uma lista [nome, posicao, camisa] dentro da lista principal
jogadores = []


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def pausar():
    input('\nPressione ENTER para continuar...')


def pedir_texto(mensagem):
    texto = input(mensagem).strip()
    while texto == '':
        print('O campo não pode ficar em branco.')
        texto = input(mensagem).strip()
    return texto


def camisa_em_uso(camisa, ignorar=-1):
    """Diz se outro jogador já usa essa camisa (ignora a posição indicada)."""
    for i in range(len(jogadores)):
        if i != ignorar and jogadores[i][2] == camisa:
            return True
    return False


def pedir_camisa(ignorar=-1):
    """Pede a camisa até ser um inteiro positivo e que ninguém use."""
    while True:
        entrada = input('Camisa: ').strip()

        if not entrada.isdigit() or int(entrada) < 1:
            print('A camisa deve ser um número inteiro positivo.')
        elif camisa_em_uso(int(entrada), ignorar):
            print(f'A camisa {int(entrada)} já está em uso.')
        else:
            return int(entrada)


def pedir_posicao():
    """Pede o número do jogador e devolve a posição na lista (ou None)."""
    entrada = input('Número do jogador: ').strip()

    if not entrada.isdigit():
        print('Digite um número válido.')
        return None

    numero = int(entrada)
    if numero < 1 or numero > len(jogadores):
        print('Jogador não encontrado.')
        return None

    return numero - 1


def cadastrar():
    print('\n== CADASTRAR JOGADOR ==')
    nome = pedir_texto('Nome: ')
    posicao = pedir_texto('Posição: ')
    camisa = pedir_camisa()
    jogadores.append([nome, posicao, camisa])
    print('Jogador cadastrado!')


def listar():
    print('\n== ELENCO ==')
    if len(jogadores) == 0:
        print('O elenco está vazio.')
        return

    for i in range(len(jogadores)):
        nome = jogadores[i][0]
        posicao = jogadores[i][1]
        camisa = jogadores[i][2]
        print(f'{i + 1}. {nome} | {posicao} | #{camisa}')


def atualizar():
    listar()
    if len(jogadores) == 0:
        return

    print()
    indice = pedir_posicao()
    if indice is None:  # não use "if not indice": a posição 0 também é falsa
        return

    nome = pedir_texto('Novo nome: ')
    posicao = pedir_texto('Nova posição: ')
    camisa = pedir_camisa(indice)  # permite manter a própria camisa
    jogadores[indice] = [nome, posicao, camisa]
    print('Jogador atualizado!')


def excluir():
    listar()
    if len(jogadores) == 0:
        return

    print()
    indice = pedir_posicao()
    if indice is None:
        return

    removido = jogadores.pop(indice)
    print(f'Jogador {removido[0]} removido!')


while True:
    limpar_tela()
    print('''
=== GERENCIAMENTO DO ELENCO ===
1. Cadastrar jogador
2. Listar jogadores
3. Atualizar jogador
4. Excluir jogador
0. Sair
''')

    opcao = input('Opção: ').strip()

    match opcao:
        case '1':
            cadastrar()
        case '2':
            listar()
        case '3':
            atualizar()
        case '4':
            excluir()
        case '0':
            print('\nSaindo do programa...')
            break
        case _:
            print('Opção inválida!')

    pausar()