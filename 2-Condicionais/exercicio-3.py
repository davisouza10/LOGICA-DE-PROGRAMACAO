import os
os.system('cls')

dia = int(input('Digite o numero do dia da semana: '))

match dia:
    case 1 | 7:
        resultado = 'Final de semana'
    case 2 | 3 | 4 | 5 | 6:
        resultado = 'Dia útil'
    case _:
        resultado = 'Inválido'

print(f'Resultado {resultado}')        