import os
os.system('cls')

print('= INSERINDO NÚMEROS DO VETOR =')
vetor_numeros = []
QUANTIDADE_NUMEROS = 6
pares = 0
impares = 0

for i in range(QUANTIDADE_NUMEROS):
    numero = int(input(f"Digite o {i+1}º número: "))
    vetor_numeros.append(numero)
    
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
        
print('\n--- Resultado ---')
print(f'números digitados: {vetor_numeros}')
print(f'Quantidade de números pares: {pares}')
print(f'Quantidade de números impares: {impares}')