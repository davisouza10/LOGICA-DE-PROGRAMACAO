import os
os.system('cls')

num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero:  '))
operador = input('Digite o operador (+, -, *, /):')

match operador:
    case '+':
        resultado = num1 + num2
    case '-':
        resultado = num1 - num2
    case '*':
        resultado = num1 * num2
    case '/':
        resultado = num1 / num2
    case _:
        resultado = 'Operador inválido'

print(f'Primeiro número: {num1}')
print(f'Segundo número: {num2}')
print(f'Operador escolhido: {operador}')
print(f'Resultado: {resultado}')

