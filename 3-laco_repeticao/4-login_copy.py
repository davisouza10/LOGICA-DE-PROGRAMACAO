import os
os.system('cls')

# MANTENDO DADOS.
login_salvo = 'Marta'
senha_salva = '1234'
tentativas = 1

while True:
    print(f'Tentativa: {tentativas}:')
    login = input('Digite o login: ')
    senha = input('Digite a senha: ')
    tentativas += 1

    if login == login_salvo and senha == senha_salva:
        print('Bem-vindo!')
        break
    else:
        print('\nLogin ou senha inválidos.')
        print('Tente novamente! \n')
        input('Pressione uma tecla para continuar...')
        os.system('cls')
else:
    print('= FIM =')
    break

