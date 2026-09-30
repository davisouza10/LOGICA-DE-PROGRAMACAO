import os
os.system('cls')
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# --- ETAPA 1: CADASTRO
limpar_tela()
print('=== CADASTRO DE USUÁRIO ===')
cadastrado_login = input('Crie seu login: ')
cadastrado_senha = input('Crie sua senha: ')

print('\nCadastro realizado com sucesso!')
input('Pressione ENTER para ir para a tela de login...')
# --- ETAPA 2: LOGIN
while True:
    limpar_tela()
    print("=== TELA DE LOGIN ===")
    login = input("Digite seu login: ")
    senha = input("Digite sua senha: ")

    # Verifica se os dados digitados batem com os cadastrados
    if login == cadastrado_login and senha == cadastrado_senha:
        print("\nLogin realizado com sucesso! Bem-vindo.")
        break  # Interrompe o loop
    else:
        print("\nLogin ou senha incorretos! Tente novamente.")
        input("Pressione ENTER para tentar novamente...")


