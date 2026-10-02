import os
os.system('cls')

voto = input('Digite o número do seu candidato(a): ')

match voto:
    case '13':
        print('Lula')
    case '14':
        print('Renan Santos')
    case '22':
        print('Flavio Bolsonaro')
    case _:
        print('Nenhum candidato encontrado!')

