import os
os.system('cls')

# ENTRADA.
print('=' * 35)
print('          TELA DE LOGIN')
print('=' * 35)
login = input('Digite seu login: ')
senha = input('Digite sua senha: ')
# PROCESSAMENTO.
login_correto = 'Joao123'
senha_correta = '1234'
# SAIDA.
print()

if login == login_correto and senha == senha_correta:
    print('=' * 35)
    print('       LOGIN REALIZADO')
    print('       Bem-vindo ao sistema!')
    print('=' * 35)
else:
    print('=' * 35)
    print('       LOGIN OU SENHA INCORRETOS!')
    print('=' * 35)