import os
os.system('cls')
# ENTRADA
login = input('Digite seu Login: ')
senha = input('Digite sua Senha: ')

# PROCESSAMENTO.
login_salvo = 'marta'
senha_salva = '123@'

login_esta_correto = login == login_salvo
senha_esta_correta = senha == senha_salva

# SAIDA.
if login_esta_correto and senha_esta_correta:
    print('Bem-vindo!')
else:
    print('login ou senha inválidos')