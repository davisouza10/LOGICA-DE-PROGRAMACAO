import os
os.system('cls')

print('= INSERINDO NÚMEROS DO VETOR =')
vetor_numeros = []
QUANTIDADE_NUMEROS = 3
pares = 0
impares = 0

for i in range(QUANTIDADE_NUMEROS):
    numero = float(input(f"Digite o {i+1}º número: "))
    vetor_numeros.append(numero)