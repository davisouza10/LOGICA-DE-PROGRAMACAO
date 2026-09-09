import os
os.system('cls')

codigo = int(input('Digite o codigo do prato: '))

match codigo:
    case 1:
        prato = 'Picanha'
        valor = 25,00
    case 2:
        prato = 'Lasanha'
        valor = 20,00
    case 3:
        prato = 'Strogonoff'
        valor = 18,00
    case 4:
        prato = 'Bife Acebolado'
        valor = 15,00
    case 5:
        prato = 'Pão com ovo'
        valor = 5,00
    case _:
        prato = 'Codigo Inválido'
        valor = 0

print(f'Prato {prato}')
print(f'Valor: {valor}')