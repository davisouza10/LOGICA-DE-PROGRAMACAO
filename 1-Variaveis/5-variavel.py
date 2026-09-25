import os
os.system('cls')

# Variáveis com dados de entrada
nota1 = float(input('Digite sua primeira Nota: '))
nota2 = float(input('Digite sua segunda Nota: '))

# Processamento (Cálculo da Média)
media = (nota1 + nota2) / 2

# Exibição dos resultados
print(f'Nota 1: {nota1}')
print(f'Nota 2: {nota2}')
print(f'Média: {media:.2f}')