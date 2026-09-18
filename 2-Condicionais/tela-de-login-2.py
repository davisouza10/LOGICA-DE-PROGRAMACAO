import os
os.system('cls')

# CADASTRO.
print('=== CADASTRO ===')

login_correto = input('Crie seu login: ')
senha_correta = input('Crie sua senha: ')
# LOGIN.
print()
print('=== LOGIN ===')

login = input('Digite seu login: ')
senha = input('Digite sua senha: ')
# VERIFICAR.
if login == login_correto and senha == senha_correta:
    print('Login realizado com sucesso!')
    print('Bem-vindo!')
else:
    print('Login ou senha Incorretos!')