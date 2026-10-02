import os
import random
import time

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_tabuleiro(t):
    print(f" {t[0]} | {t[1]} | {t[2]} ")
    print("---|---|---")
    print(f" {t[3]} | {t[4]} | {t[5]} ")
    print("---|---|---")
    print(f" {t[6]} | {t[7]} | {t[8]} \n")

def checar_vitoria(t, simbolo):
    vitorias = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Linhas
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Colunas
        [0, 4, 8], [2, 4, 6]              # Diagonais
    ]
    for v in vitorias:
        if t[v[0]] == t[v[1]] == t[v[2]] == simbolo:
            return True
    return False

def encontrar_jogada_estratagema(t, simbolo):
    vitorias = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for v in vitorias:
        valores = [t[v[0]], t[v[1]], t[v[2]]]
        if valores.count(simbolo) == 2:
            for idx in v:
                if t[idx] not in ['X', 'O']:
                    return t[idx]
    return None

# ==================================================
# LOOP PRINCIPAL DO PROGRAMA (PERMITE REINICIAR O JOGO)
# ==================================================
while True:
    # 1. TELA INICIAL: ESCOLHA DE DIFICULDADE
    dificuldade = ""
    while dificuldade not in ['1', '2', '3']:
        limpar_tela()
        print("==========================================")
        print("    JOGO DA VELHA: VOCÊ (X) VS MÁQUINA (O) ")
        print("==========================================")
        print(" DIFICULDADES:")
        print(" [1] Fácil   (Máquina joga totalmente aleatório)")
        print(" [2] Médio   (Máquina bloqueia suas vitórias)")
        print(" [3] Difícil (Máquina joga com estratégia imbatível)")
        print("==========================================\n")
        
        dificuldade = input("Escolha o nível (1, 2 ou 3): ").strip()
        
        if dificuldade not in ['1', '2', '3']:
            print("\n⚠️ Opção inválida! Digite apenas 1, 2 ou 3.")
            time.sleep(1.2)

    nomes_dificuldade = {'1': 'FÁCIL', '2': 'MÉDIO', '3': 'DIFÍCIL'}
    nivel_escolhido = nomes_dificuldade[dificuldade]

    # 2. INICIALIZA O TABULEIRO ZERADO
    tabuleiro = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    # 3. LOOP DA PARTIDA
    while True:
        limpar_tela()
        print(f"=== MODO: {nivel_escolhido} ===\n")
        mostrar_tabuleiro(tabuleiro)

        # --- JOGADA DO HUMANO (X) ---
        escolha = input("Sua vez! Escolha uma casa livre (1-9): ").strip()

        if escolha not in tabuleiro or escolha in ['X', 'O']:
            print("⚠️ Posição inválida ou já ocupada!")
            time.sleep(1)
            continue

        idx = int(escolha) - 1
        tabuleiro[idx] = 'X'

        if checar_vitoria(tabuleiro, 'X'):
            limpar_tela()
            mostrar_tabuleiro(tabuleiro)
            print("🎉 PARABÉNS! Você venceu a máquina!")
            break

        casas_livres = [c for c in tabuleiro if c not in ['X', 'O']]
        if not casas_livres:
            limpar_tela()
            mostrar_tabuleiro(tabuleiro)
            print("🤝 DEU VELHA! Empate.")
            break

        # --- JOGADA DA MÁQUINA (O) ---
        limpar_tela()
        print(f"=== MODO: {nivel_escolhido} ===\n")
        mostrar_tabuleiro(tabuleiro)
        print("🤖 Máquina (O) pensando...")
        time.sleep(1)

        jogada_maquina = None

        # Difícil: Tenta ganhar primeiro
        if dificuldade == '3':
            jogada_maquina = encontrar_jogada_estratagema(tabuleiro, 'O')

        # Médio e Difícil: Bloqueia a vitória do jogador
        if not jogada_maquina and dificuldade in ['2', '3']:
            jogada_maquina = encontrar_jogada_estratagema(tabuleiro, 'X')

        # Difícil: Dá preferência ao centro
        if not jogada_maquina and dificuldade == '3':
            if '5' in casas_livres:
                jogada_maquina = '5'

        # Jogada aleatória (Fácil ou fallback)
        if not jogada_maquina:
            jogada_maquina = random.choice(casas_livres)

        idx_m = int(jogada_maquina) - 1
        tabuleiro[idx_m] = 'O'

        if checar_vitoria(tabuleiro, 'O'):
            limpar_tela()
            mostrar_tabuleiro(tabuleiro)
            print("💻 A MÁQUINA VENCEU!")
            break

    # 4. PERGUNTA SE QUER JOGAR NOVAMENTE
    print("\n------------------------------------------")
    novo_jogo = input("Deseja jogar novamente? (s/n): ").strip().lower()
    if novo_jogo != 's':
        print("\nObrigado por jogar! Até a próxima! 👋")
        break