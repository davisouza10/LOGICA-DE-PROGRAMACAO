import os
import time

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# 1. TELA DE CADASTRO
limpar_tela()
print('=== CADASTRO ===')
login_correto = input('Crie seu login: ').strip()
senha_correta = input('Crie sua senha: ').strip()

print('\n✅ Cadastro realizado com sucesso!')
time.sleep(1.5)

# 2. TELA DE LOGIN (Repete limpando a tela a cada tentativa)
while True:
    limpar_tela()  # Limpa a tela para a nova tentativa de login
    print('=== LOGIN ===')
    login = input('Digite seu login: ').strip()
    senha = input('Digite sua senha: ').strip()

    # VERIFICAÇÃO
    if login == login_correto and senha == senha_correta:
        limpar_tela()  # Limpa a tela antes da mensagem de boas-vindas
        print('====================================')
        print('  ✅ Login Realizado com sucesso!')
        print('  🎉 Bem-vindo ao sistema!')
        print('====================================')
        break  # Sai do loop e entra no programa
    else:
        print('\n❌ Login ou senha incorretos!')
        time.sleep(1.5)  # Aguarda 1.5s para o usuário ler o aviso antes de limpar