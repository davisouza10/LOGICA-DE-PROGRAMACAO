import os

pratos_escolhidos = []
precos_escolhidos = []

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("=== CARDÁPIO DO RESTAURANTE ===")
    print("1 - Picanha             - R$ 25.00")
    print("2 - Lasanha             - R$ 20.00")
    print("3 - Strogonoff          - R$ 18.00")
    print("4 - Bife-Acebolado      - R$ 15.00")
    print("5 - Pão com ovo         - R$  5.00")
    print("===============================")
    
    opcao = input("Digite o número do prato desejado: ")
    
    if opcao == '1':
        pratos_escolhidos.append("Picanha")
        precos_escolhidos.append(25.00)
        print("\n-> Picanha adicionada ao pedido!")
    elif opcao == '2':
        pratos_escolhidos.append("Lasanha")
        precos_escolhidos.append(20.00)
        print("\n-> Lasanha adicionada ao pedido!")
    elif opcao == '3':
        pratos_escolhidos.append("Strogonoff")
        precos_escolhidos.append(18.00)
        print("\n-> Strogonoff adicionado ao pedido!")
    elif opcao == '4':
        pratos_escolhidos.append("Bife-Acebolado")
        precos_escolhidos.append(15.00)
        print("\n-> Bife-Acebolado adicionado ao pedido!")
    elif opcao == '5':
        pratos_escolhidos.append("Pão com ovo")
        precos_escolhidos.append(5.00)
        print("\n-> Pão com ovo adicionado ao pedido!")
    else:
        print("\nOpção inválida! Nenhum item foi adicionado.")

    resposta = input("\nDeseja escolher outro prato? (s/n): ").strip().lower()
    if resposta != 's':
        break

# Resumo final (sem limpar a tela abruptamente)
os.system('cls' if os.name == 'nt' else 'clear')
print("=== RESUMO DO PEDIDO ===")

if len(pratos_escolhidos) == 0:
    print("Nenhum pedido foi realizado.")
else:
    total_conta = 0
    for i in range(len(pratos_escolhidos)):
        nome = pratos_escolhidos[i]
        preco = precos_escolhidos[i]
        print(f"- {nome}: R$ {preco:.2f}")
        total_conta += preco
        
    print("------------------------")
    print(f"VALOR TOTAL DA CONTA: R$ {total_conta:.2f}")

# Pausa no final para não fechar nem cortar o resumo
input("\nPressione ENTER para sair...")