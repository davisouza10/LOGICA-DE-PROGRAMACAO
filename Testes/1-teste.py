import os
os.system('cls')

# ENTRADA.
nota = int(input('Digite sua nota: '))
# PROCESSAMENTO.
if nota >= 7:
    print('Aprovado!')
elif nota == 6:
    print('Aprovado Arrastado!')
else:
    print('Reprovado')

# SAIDA.