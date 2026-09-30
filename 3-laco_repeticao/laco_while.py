import os
os.system('cls')

while True:
    numero = int(input('Digite um número entre 1 e 10: '))
    if numero < 1 or numero > 10:
        print() # Pular uma linha
        print('Número invalido, tente novamente!')
    else:
        print() # Assim como o \n
        print('O número está entre 1 e 10.')
        break # Serve para parar o laço de repetição.

print('= FIM =')