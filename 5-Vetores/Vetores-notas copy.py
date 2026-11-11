import os
os.system('cls')

print('= INSERINDO NOTAS NO VETOR =')
vetor_nota = []
QUANTIDADE_NOTAS = 3

for i in range(QUANTIDADE_NOTAS):
    nota = float(input(f'Digite a {i+1}º nota: '))
    vetor_nota.append(nota)

# Sum - Somar tudo que está no vetor.
media = sum(vetor_nota) / QUANTIDADE_NOTAS

print('\n= EXIBINDO AS NOTAS DO VETOR =')
for indice, nota in enumerate(vetor_nota, start=1):
    print(f'{indice}º: {nota}')
    
print(f'Média: {media}')