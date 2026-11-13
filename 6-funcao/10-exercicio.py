import os
os.system('cls')

# Faça uma função que recebe um valor inteiro 
# e verifica se o valor é positivo ou negativo.

def valor_positivo_ou_negativo(valor):
    if valor > 0:
        resultado = 'Positivo'
    elif valor < 0:
        resultado = 'Negativo'
    else:
        resultado = 'Neutro'
    return resultado

print('= SOLICITANDO DADOS =')
valor = int(input('Digite um valor inteiro: '))

verificacao = valor_positivo_ou_negativo(valor)

print('= EXIBINDO DADOS =')
print(f'O valor: {valor} é {verificacao}')
