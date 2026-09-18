import os
os.system('cls')

# ENTRADA.
faltas = int(input('Digite o numero de faltas: '))
media = float(input('Digite a media: '))
# PROCESSAMENTO.
if media >= 7 and faltas <= 40:
    print('Aprovado!')
else:
    print('Reprovado!')

# SAIDA.