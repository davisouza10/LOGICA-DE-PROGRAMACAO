import os
os.system('cls')

LOGIN_CORRETO = 'luna123'
SENHA_CORRETA = '1234'

while True:
    login = input('Digite o login: ')
    senha = input('Digite a senha: ')

    if login == LOGIN_CORRETO and SENHA_CORRETA:
        print('\nLogin realizado com sucesso! Bem-vindo.')
        break
    else:
        print('\nLogin  ou senha incorretos! Tente novamente.')
        input('Pressione ENTER para continuar...')
