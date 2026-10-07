import os
os.system('cls')

soma = 0
quantidade = 0

while True:
    numero = int(input("Digite um valor inteiro positivo (ou um negativo para sair): "))
    
    # Se o número for negativo, encerra a leitura
    if numero < 0:
        break
    
    # Soma o valor e incrementa a quantidade
    soma += numero
    quantidade += 1

# Exibe a média se pelo menos um número válido tiver sido inserido
if quantidade > 0:
    media = soma / quantidade
    print(f"\nForam informados {quantidade} número(s) positivo(s).")
    print(f"A média aritmética é: {media:.2f}")
else:
    print("\nNenhum número positivo foi informado.")