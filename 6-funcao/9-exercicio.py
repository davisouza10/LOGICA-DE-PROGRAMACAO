import os
os.system('cls')

# Crie uma função que receba um número e mostre
# uma mensagem informando se o número é par ou ímpar.

def verificar_numero(numero):
    if numero % 2 == 0:
        resultado = f'{numero} é par.'
    else:
        resultado = f'{numero} é ímpar.'
    return resultado
    

print('= SOLICITANDO DADOS =')
numero = int(input('Digite um número: '))

verificacao = verificar_numero(numero)


print('= EXIBINDO DADOS =')
print(f'Resultado: {verificacao}')