import os
os.system('cls')

print('= INSERINDO NOTAS NO VETOR =')
vetor_nota = []
QUANTIDADE_NOTAS = 4

for i in range(QUANTIDADE_NOTAS):
    nota = float(input(f'Digite a {i+1}º nota: '))
    vetor_nota.append(nota)
# Sum - Somar tudo que está no vetor.
media = sum(vetor_nota) / QUANTIDADE_NOTAS

if media >= 7:
        resultado = 'Aprovado'
elif media >= 5:
        resultado = 'Recuperação'
else:
        resultado = 'Reprovado'
        

print('\n= EXIBINDO AS NOTAS DO VETOR =')
for indice, nota in enumerate(vetor_nota, start=1):
    print(f'{indice}º nota: {nota}')
    
print(f'Média: {media:.1f}')
print(f'Resultado: {resultado}')
