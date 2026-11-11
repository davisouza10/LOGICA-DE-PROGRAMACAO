import os
os.system('cls')

vetor_numeros = []
QUANTIDADE_NUMEROS = 5

for i in range(QUANTIDADE_NUMEROS):
    numeros = int(input(f'Digite o (i+1)º número: '))
    
    if numeros < 0:
        numeros = 0

    vetor_numeros.append(numeros)
    
print('\n--- Resultado ---')       
for posicao, numeros in enumerate(vetor_numeros, start=1):
    print(f'{posicao}º) {numeros}')

