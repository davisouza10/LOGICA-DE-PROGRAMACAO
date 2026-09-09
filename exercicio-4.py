import os
os.system('cls')

mes_ano = int(input('Digite um mês do ano: '))

match mes_ano:
    case 1:
        resultado = 'Janeiro'
    case 2:
        resultado = 'Fevereiro'
    case 3:
        resultado = 'Março'
    case 4:
        resultado = 'Abril'
    case 5:
        resultado = 'Maio'
    case 6:
        resultado = 'Junho'
    case 7:
        resultado = 'Julho'
    case 8:
        resultado = 'Agosto'
    case 9:
        resultado = 'Setembro'
    case 10:
        resultado = 'Outubro'
    case 11:
        resultado = 'Novembro'
    case 12:
        resultado = 'Dezembro'
    case _:
        resultado = 'Mês inválido'

print(f'Resultado: {resultado}')
