import os
os.system('cls')

CANDIDATO_1 = '13'
CANDIDATO_2 = '22'
CANDIDATO_3 = '14'

voto = input('Digite número do seu Candidato(a): ')

if voto == CANDIDATO_1:
    print('Lula')
elif voto == CANDIDATO_2:
    print('Flavio Bolsonaro')
elif voto == CANDIDATO_3:
    print('Renan Santos')
else:
    print('Nenhum candidato encontrado!')

print('= FIM =')