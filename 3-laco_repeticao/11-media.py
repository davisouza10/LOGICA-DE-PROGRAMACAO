import os
os.system('cls')

# ENTRADA.
print('= Solicitando notas =')
soma = 0

for i in range(1, 5):
    nota = float(input(f'Digite a {i}ª nota: '))
    soma = soma + nota

# PROCESSAMENTO.
media = soma / 4

# SAÍDA.
print('\n= Exibindo resultado =')
print(f'Média: {media:.2f}')

