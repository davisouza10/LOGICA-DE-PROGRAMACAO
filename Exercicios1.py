import os
os.system('cls')

# ENTRADA.
nome = input('Digite o nome do aluno: ')
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

# PROCESSAMENTO.
media = (nota1 + nota2) / 2
if media >= 9:
    conceito = 'A'
    resultado = 'Aprovado'
elif media >= 7.5:
    conceito = 'B'
    resultado = 'Aprovado'
elif media >= 6:
    conceito = 'C'
    resultado = 'Reprovado'
elif media >= 4:
    conceito = 'D'
    resultado = 'Reprovado'
else:
    conceito = 'E'
    resultado = 'Reprovado'

# SAIDA.
print('Aluno:', nome)
print('Media:', media)
print('Conceito:', conceito)
print('Resultado:', resultado)