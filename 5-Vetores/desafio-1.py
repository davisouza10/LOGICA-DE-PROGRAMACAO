pacientes = []

while True:
    print()
    print('=== HOSPITAL - CADASTRO DE PACIENTES ===')
    print('1. Cadastrar paciente')
    print('2. Listar pacientes')
    print('3. Atualizar paciente')
    print('4. Excluir paciente')
    print('5. Buscar paciente')
    print('0. Sair')

    opcao = input('Opção: ')

    match opcao:
        case '1':
            nome = input('Nome: ')
            sobrenome = input('Sobrenome: ')
            pacientes.append([nome, sobrenome])
            print('Paciente cadastrado!')

        case '2':
            if len(pacientes) == 0:
                print('Nenhum paciente cadastrado.')
            else:
                for i in range(len(pacientes)):
                    print(i + 1, '-', pacientes[i][0], pacientes[i][1])

        case '3':
            if len(pacientes) == 0:
                print('Nenhum paciente cadastrado.')
            else:
                for i in range(len(pacientes)):
                    print(i + 1, '-', pacientes[i][0], pacientes[i][1])

                numero = int(input('Número do paciente: '))
                if numero >= 1 and numero <= len(pacientes):
                    nome = input('Novo nome: ')
                    sobrenome = input('Novo sobrenome: ')
                    pacientes[numero - 1] = [nome, sobrenome]
                    print('Paciente atualizado!')
                else:
                    print('Paciente não encontrado.')

        case '4':
            if len(pacientes) == 0:
                print('Nenhum paciente cadastrado.')
            else:
                for i in range(len(pacientes)):
                    print(i + 1, '-', pacientes[i][0], pacientes[i][1])

                numero = int(input('Número do paciente: '))
                if numero >= 1 and numero <= len(pacientes):
                    pacientes.pop(numero - 1)
                    print('Paciente removido!')
                else:
                    print('Paciente não encontrado.')

        case '5':
            termo = input('Buscar por: ').lower()
            encontrou = False

            for i in range(len(pacientes)):
                nome_completo = pacientes[i][0] + ' ' + pacientes[i][1]
                if termo in nome_completo.lower():
                    print(i + 1, '-', nome_completo)
                    encontrou = True

            if encontrou == False:
                print('Nenhum paciente encontrado.')

        case '0':
            print('Saindo do programa...')
            break

        case _:
            print('Opção inválida!')