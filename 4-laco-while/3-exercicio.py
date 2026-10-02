import os

os.system('cls')

# Preços dos produtos
iphone = 3000
samsung = 1500
xiaomi = 2000
motorola = 1000
sony = 500

print('=== CARDÁPIO DE PRODUTOS ===')
print('1 - iPhone')
print('2 - Samsung')
print('3 - Xiaomi')
print('4 - Motorola')
print('5 - Sony')
print('===========================')

while True:
    opcao = input('Digite o número do produto desejado: ')

    match opcao:
        case '1':
            print(f'Você escolheu iPhone. Preço: R$ {iphone},00')
            break
        case '2':
            print(f'Você escolheu Samsung. Preço: R$ {samsung},00')
            break
        case '3':
            print(f'Você escolheu Xiaomi. Preço: R$ {xiaomi},00')
            break
        case '4':
            print(f'Você escolheu Motorola. Preço: R$ {motorola},00')
            break
        case '5':
            print(f'Você escolheu Sony. Preço: R$ {sony},00')
            break
        case _:
            print('Opção inválida! Tente novamente.\n')

print('= FIM =')