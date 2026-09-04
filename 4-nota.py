import os
os.system('cls')

nota = float(input('Digite a nota: '))

if nota >= 0 and nota <= 10:
    print(nota)
else:
    print('Nota deve ser entre 0 e 10')
