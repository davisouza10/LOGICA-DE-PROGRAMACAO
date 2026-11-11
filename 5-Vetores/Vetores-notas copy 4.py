import os
os.system('cls')

print('= INSERINDO NÚMEROS NO VETOR =')
vetor_nota = []
QUANTIDADE_NUMEROS = 5

# 1. Entrada de dados
for i in range(QUANTIDADE_NUMEROS):
    nota = int(input(f'Digite o {i+1}º número: '))
    vetor_nota.append(nota)

# 2. Descobrindo o Maior e o Menor
maior_numero = max(vetor_nota)
menor_numero = min(vetor_nota)

# 3. Exibição dos dados
print('\n= EXIBINDO OS NÚMEROS DO VETOR =')
for indice, nota in enumerate(vetor_nota, start=1):
    print(f'{indice}º número: {nota}')

print(f'\nMaior número digitado: {maior_numero}')
print(f'Menor número digitado: {menor_numero}')