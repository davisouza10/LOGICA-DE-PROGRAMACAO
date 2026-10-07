import os
os.system('cls')

soma = 0
quantidade = 0

while True:
    num = int(input('Digite um número (1 a 9): '))

    match num:
        case 2 | 3 | 4 | 5 | 6 | 7 | 9:
            print('Número correto!')
            soma += num
            quantidade += 1
            break
        case 1 | 8:
            print('Número invalido! tente novamente.')
        case _:
            print('Numero incorreto! Tente novamnete.')
print('Media:', soma / quantidade)