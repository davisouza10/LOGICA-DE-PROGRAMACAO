import os
os.system('cls')

print('= INSERINDO NOTAS NO VETOR =')
vetor_nota = []
QUANTIDADE_NOTAS = 4

# 1. Entrada de dados
for i in range(QUANTIDADE_NOTAS):
    nota = float(input(f'Digite a {i+1}ª nota: '))
    vetor_nota.append(nota)

# 2. Cálculo da Média
media = sum(vetor_nota) / QUANTIDADE_NOTAS

# 3. Exibição das Notas
print('\n= EXIBINDO AS NOTAS DO VETOR =')
for indice, nota in enumerate(vetor_nota, start=1):
    print(f'{indice}ª nota: {nota:.1f}')

print(f'\nMédia final: {media:.1f}')

# 4. Verificação se passou ou não com base na MÉDIA
if media >= 7.0:
    print('Situação: APROVADO! 🎉')
elif media >= 5.0:
    print('Situação: RECUPERAÇÃO! ⚠️')
else:
    print('Situação: REPROVADO! ❌')