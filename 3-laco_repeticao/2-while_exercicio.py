import os
os.system('cls')

while True:
    primeira_nota = float(input('Digite a primeira nota (0 a 10): '))
    if primeira_nota >= 0 and primeira_nota <= 10:
        break
    else:
        print('Nota inválida! Tente novamnete.')

while True:
    segunda_nota = float(input('Digite a segunda nota (0 a 10): '))
    if segunda_nota >= 0 and segunda_nota <= 10:
        break
    else:
        print('Nota inválida! Tente novamente.')

media = (primeira_nota + segunda_nota) / 2

print(f'\nA primeira nota foi: {primeira_nota} ')
print(f'A segunda nota foi: {segunda_nota}')
print(f'A média aritmética é: {media:.2f}')

