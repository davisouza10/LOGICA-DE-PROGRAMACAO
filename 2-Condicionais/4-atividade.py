import os
os.system('cls')

# ENTRADA.
num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))

# PROCESSAMENTO.
print('Os 2 numeros informados são: ', num1, 'e' , num2)
if num1 > num2:
    print('o maior numero é: ', num1)
    print('O menor numero é: ', num2)
elif num2 > num1:
    print('O maior numero é: ', num2)
    print('O menor numero é: ', num1)
else:
    print('Os dois numeros são iguais: ', num1)

# SAIDA.