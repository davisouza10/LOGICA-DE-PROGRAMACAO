import os

# Cada paciente é uma lista [nome, sobrenome] dentro da lista principal
pacientes = []


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


def pedir_posicao():
    """Pede o número do paciente e devolve a posição na lista (ou None)."""
    entrada = input('Número do paciente: ').strip()

    if not entrada.isdigit():
        print('Digite um número válido.')
        return None

    numero = int(entrada)
    if numero < 1 or numero > len(pacientes):
        print('Paciente não encontrado.')
        return None

    return numero - 1


def cadastrar():
    print('\n== CADASTRAR PACIENTE ==')
    nome = pedir_texto('Nome: ')
    sobrenome = pedir_texto('Sobrenome: ')
    pacientes.append([nome, sobrenome])
    print('Paciente cadastrado!')


def listar():
    print('\n== PACIENTES ==')
    if len(pacientes) == 0:
        print('Nenhum paciente cadastrado.')
        return

    for i in range(len(pacientes)):
        print(f'{i + 1}. {pacientes[i][0]} {pacientes[i][1]}')


def atualizar():
    listar()
    if len(pacientes) == 0:
        return

    print()
    posicao = pedir_posicao()
    if posicao is None:  # não use "if not posicao": a posição 0 também é falsa
        return

    nome = pedir_texto('Novo nome: ')
    sobrenome = pedir_texto('Novo sobrenome: ')
    pacientes[posicao] = [nome, sobrenome]
    print('Paciente atualizado!')


def excluir():
    listar()
    if len(pacientes) == 0:
        return

    print()
    posicao = pedir_posicao()
    if posicao is None:
        return

    removido = pacientes.pop(posicao)
    print(f'Paciente {removido[0]} {removido[1]} removido!')


def buscar():
    print('\n== BUSCAR PACIENTE ==')
    termo = pedir_texto('Buscar por: ').lower()

    encontrou = False
    for i in range(len(pacientes)):
        nome_completo = f'{pacientes[i][0]} {pacientes[i][1]}'
        if termo in nome_completo.lower():
            print(f'{i + 1}. {nome_completo}')
            encontrou = True

    if not encontrou:
        print('Nenhum paciente encontrado.')


while True:
    limpar_tela()
    print('''
=== HOSPITAL - CADASTRO DE PACIENTES ===
1. Cadastrar paciente
2. Listar pacientes
3. Atualizar paciente
4. Excluir paciente
5. Buscar paciente
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
        case '5':
            buscar()
        case '0':
            print('\nSaindo do programa...')
            break
        case _:
            print('Opção inválida!')

    pausar()