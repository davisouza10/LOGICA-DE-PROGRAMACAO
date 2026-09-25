import os
os.system('cls')

#soma = 0
#for i in range(1, 4):
    #soma += float(input(f'Nota {i}: '))

#media = soma / 3
#print(f'Media: {media:.2f}')

#if media >= 7:
    #print('Aprovado')
#elif media < 4:
    #print('Reprovado')
#else:
    #print('Recuperação')

# CONSTANTES.
QUANTIDADE_NOTAS = 3

# ENTRADA.
print('= Solicitando notas =')
soma = 0

for i in range(1, QUANTIDADE_NOTAS + 1):
    nota = float(input(f'Digite a {i} nota: '))
    soma += nota

# PROCESSAMENTO.
media = soma / QUANTIDADE_NOTAS

if media >= 7:
    resultado = 'Aprovado'
elif media <= 3:
    resultado = 'Reprovado'
else:
    resultado = 'Recuperação'

# SAIDA.
print('\n= Exibindo resultados =')
print(f'Média: {media}')
print(f'resultado: {resultado}')