import os
os.system('cls')

# FAÇA UM PROGRAMA QUE SOLICITE:
# - NOME, EMAIL E TELEFONE

# O PROGRAMA DEVE MANTER NA TELA A LOGO:
# =================
#   SENAI - BAHIA
# =================
# O LOGO DEVE SER EXIBIDO USANDO FUNÇÃO:
# logo_senai()

# OS DADOS DEVERÃO SER APRESENTADOS POR MEIO
# DE UMA FUNÇÃO COM PARAMETROS CHAMADA:
# mostrar_dados(nome, email, telefone)

def logo_senai():
    print(' \n==================== ')
    print('=   SENAI - BAHIA  =')
    print(' ==================== ')

def mostrar_dados(nome, email, telefone):
    print(f'Seu nome: {nome}')
    print(f'Seu email: {email}')
    print(f'Seu telefone é: {telefone}')

logo_senai()
print('= SOLICITANDO DADOS =')
nome = input('Digite seu nome: ')

logo_senai()
email = input('Digite seu email: ')

logo_senai()
telefone = input('Digite seu número de telefone: ')

logo_senai()
print('\n= EXIBINDO DADOS =')
mostrar_dados(nome, email, telefone)