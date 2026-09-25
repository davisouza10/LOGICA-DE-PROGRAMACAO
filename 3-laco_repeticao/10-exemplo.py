import os
os.system('cls')

print('ACUMULANDO VALORES EM UMA VARIAVEL.')
soma = 0

print(f'Valor INICIAL da variavel soma: {soma}')

for i in range(3):
    numero = int(input('\nDigite um número para somar: '))
    soma = soma + numero
    print(f'Valor TEMPORÁRIO da variável soma: {soma}')

print(f'Valor FINAL da variavel soma: {soma}')