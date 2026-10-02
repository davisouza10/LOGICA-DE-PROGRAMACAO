import os
import random
import time

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def desenhar_forca(erros):
    estagios = [
        """
           +---+
           |   |
               |
               |
               |
               |
         =========""",
        """
           +---+
           |   |
           O   |
               |
               |
               |
         =========""",
        """
           +---+
           |   |
           O   |
           |   |
               |
               |
         =========""",
        """
           +---+
           |   |
           O   |
          /|   |
               |
               |
         =========""",
        """
           +---+
           |   |
           O   |
          /|\\  |
               |
               |
         =========""",
        """
           +---+
           |   |
           O   |
          /|\\  |
          /    |
               |
         =========""",
        """
           +---+
           |   |
           O   |
          /|\\  |
          / \\  |
               |
         ========="""
    ]
    return estagios[erros]

# Ordem de preferência de chutes (Vogais primeiro)
ALFABETO = ['A', 'E', 'O', 'I', 'U', 'S', 'R', 'N', 'D', 'M', 'T', 'C', 'L', 'P', 'V', 'G', 'B', 'F', 'Q', 'H', 'Z', 'J', 'X', 'K', 'W', 'Y']

while True:
    limpar_tela()
    print("==========================================")
    print("   JOGO DA FORCA: MÁQUINA ADIVINHA! 🤖   ")
    print("==========================================\n")

    tema = input("Digite o TEMA da palavra: ").strip().upper()
    
    tamanho = 0
    while tamanho <= 0:
        try:
            tamanho = int(input("Quantas LETRAS tem a sua palavra? ").strip())
        except ValueError:
            print("⚠️️ Digite um número válido!")

    letras_descobertas = ['_'] * tamanho
    letras_tentadas = []
    erros = 0
    max_erros = 6

    while erros < max_erros and '_' in letras_descobertas:
        limpar_tela()
        print(f"📌 TEMA: {tema}")
        print(desenhar_forca(erros))
        print(f"\nEstado da Palavra: {' '.join(letras_descobertas)}")
        print(f"Letras testadas: {', '.join(letras_tentadas)}")
        print(f"Erros da máquina: {erros}/{max_erros}\n")

        # --- TENTATIVA DE CHUTE DA PALAVRA COMPLETA ---
        # Se restarem apenas 2 ou menos letras ocultas, a máquina tenta arriscar a palavra inteira
        faltam = letras_descobertas.count('_')
        if faltam <= 2 and faltam > 0:
            print("🤖 A máquina acha que já sabe a palavra!")
            chute_palavra = input("🤖 MÁQUINA: 'Posso tentar arriscar a palavra inteira? Digite a palavra que você pensou para eu conferir': ").strip().upper()
            
            if len(chute_palavra) == tamanho:
                acertou_palavra = input(f"A palavra secreta é '{chute_palavra}'? (s/n): ").strip().lower()
                if acertou_palavra == 's':
                    letras_descobertas = list(chute_palavra)
                    print("\n🎉 MÁQUINA: 'Eba! Acertei a palavra inteira!'")
                    time.sleep(2)
                    break
                else:
                    print("\n❌ MÁQUINA: 'Ah não, errei o chute da palavra!'")
                    erros += 1
                    time.sleep(1.5)
                    continue

        # --- CHUTE DE LETRA NORMAL ---
        chute = None
        for l in ALFABETO:
            if l not in letras_tentadas:
                chute = l
                break

        letras_tentadas.append(chute)
        print(f"👉 A máquina pergunta: A palavra tem a letra [{chute}]?")
        
        resposta = ""
        while resposta not in ['s', 'n']:
            resposta = input("Sua resposta (s = sim / n = não): ").strip().lower()

        if resposta == 's':
            print(f"\nEm quais posições de 1 a {tamanho} a letra [{chute}] aparece?")
            print("Exemplo: se a palavra for 'BANANA' e a letra for 'A', digite: 2 4 6")
            
            posicoes_validas = False
            while not posicoes_validas:
                try:
                    posicoes = input("Digite as posições separadas por espaço: ").strip().split()
                    for pos in posicoes:
                        idx = int(pos) - 1
                        if 0 <= idx < tamanho:
                            letras_descobertas[idx] = chute
                    posicoes_validas = True
                except ValueError:
                    print("⚠️ Digite números válidos correspondentes às posições!")
        else:
            print(f"❌ Letra [{chute}] anotada como erro.")
            erros += 1

        time.sleep(1)

    # --- FIM DA PARTIDA ---
    limpar_tela()
    print(f"📌 TEMA: {tema}")
    print(desenhar_forca(erros))
    print(f"\nResultado final: {' '.join(letras_descobertas)}\n")

    if '_' not in letras_descobertas:
        print("🎉 A MÁQUINA VENCEU! Conseguiu descobrir todas as letras!")
    else:
        print("💥 A MÁQUINA FOI ENFORCADA! Você venceu a partida!")

    print("\n------------------------------------------")
    novo_jogo = input("Quer jogar novamente? (s/n): ").strip().lower()
    if novo_jogo != 's':
        print("\nObrigado por jogar! Até a próxima! 👋")
        break