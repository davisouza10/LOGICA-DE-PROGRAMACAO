import os
os.system('cls')

# FAÇA UM PROGRAMA COM MATCH CASE.
# 1 - CADASTRAR CLIENTE
# 2 - MOSTRAR DADOS DO CLIENTE
# 3 - SAIR

# FAÇA A FUNÇÃO PARA CADASTRAR SER USADA NO CASE 1:
# FAÇA A FUNÇÃO PARA MOSTRAR DADOS DO CLIENTE SER USADA NO CASE 2:
# CASE 3 USE A FUNÇÃO exit() para sair
# CASE _: PARA OPÇÕES INCORRETAS

def logo_senai():
    os.system('cls')
    print('\n=================')
    print('   SENAI - BAHIA')
    print('=================')
   
def mostrar_dados(nome, email, telefone):
    print(f'Nome: {nome}')
    print(f'E-mail: {email}')
    print(f'Telefone: {telefone}')


while True:
    logo_senai()
    print('''
1 - CADASTRAR CLIENTE
2 - MOSTRAR DADOS DO CLIENTE
3 - SAIR
    ''')
    opcao = int(input('Digite a opção desejada: '))
   
    match opcao:
        case 1:
            logo_senai()
            print('= SOLICITANDO DADOS =')
            nome = input('Digite seu nome: ')

            logo_senai()
            email = input('Digite seu email: ')

            logo_senai()
            telefone = input('Digite seu telefone: ')
           
        case 2:
            logo_senai()
            print('\n= EXIBINDO DADOS =')
            mostrar_dados(nome, email, telefone)
           
        case 3:
            print('\nSaindo do programa...')
            exit()
           
        case _:
            print('\nOpção inválida, tente novamente...')
           
    input('Pressione uma tecla para continuar...')