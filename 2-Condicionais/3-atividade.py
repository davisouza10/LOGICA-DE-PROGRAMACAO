import os
os.system('cls')

# ENTRADA.
idade = int(input('Digite sua idade: '))

# PROCESSAMENTO.
if idade < 16:
    print('Não podem Votar')
elif idade <= 17:
    print('Voto Opcional')
elif idade <= 65:
    print('Voto Obrigatorio')
else:
    print('Não é obrigado a votar')


# SAIDA.
