import os
os.system('cls')

sexo = input('Digite o sexo (M/F): ').upper()
altura = float(input('Digite a altura: '))

match sexo:
    case 'M':
        peso_ideal = (72.7 * altura) - 58
        print(f'Peso ideal: {peso_ideal:.2f} kg')

    case 'F':
        peso_ideal = (62.1 * altura) - 44.7
        print(f'Peso ideal: {peso_ideal:.2f} kg')

    case _:
        print('Sexo inválido!')