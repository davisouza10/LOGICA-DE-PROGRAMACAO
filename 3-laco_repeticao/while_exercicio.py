import os
os.system('cls')

while True:
    numero = int(input('Digite a nota do aluno: '))
    if numero < 0 or numero >10:
        print('Número invalido, tente novamente!')
    elif numero >= 6 and numero <= 10:
        print(numero)
        print('Aprovado!')
        break
    else:
        print('Reprovado!')
        break

print('= FIM =')
    
