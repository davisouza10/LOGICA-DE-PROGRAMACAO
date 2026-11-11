import os
os.system('cls')

print('= INSERINDO NOTAS NO VETOR =')
vetor_nota = []

for i in range(3):
    nota = float(input(f'Digite a {i+1}º nota: '))
    vetor_nota.append(nota)

print('\n= EXIBINDO AS NOTAS DO VETOR =')
for indice, nota in enumerate(vetor_nota, start=1):
    print(f'{indice}º: {nota}')