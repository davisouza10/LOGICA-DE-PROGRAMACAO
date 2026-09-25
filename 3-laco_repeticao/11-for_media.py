import os
os.system('cls')

soma = 0

for i in range(1, 5):
    nota = float(input(f'Digite a {i} nota: '))
    soma = soma + nota

media = soma / 4

print(f'Média: {media:.2f}')