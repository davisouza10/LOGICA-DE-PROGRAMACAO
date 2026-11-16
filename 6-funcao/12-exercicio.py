import os
os.system('cls')

# Fazer um programa que solicita o preço de um produto
# e inflaciona esse preço em 10% se ele for menor que
# 100 e 20% se ele for maior ou igual a 100.

def inflacionar_preco(preco):
    if preco < 100:
        return preco * 1.10
    else:
        return preco * 1.20
    
print('= SOLICITANDO DADOS =')
preco = float(input('Digite o valor do produto: '))

# Chamando a Função.
novo_preco = inflacionar_preco(preco)

print('\n= EXIBINDO DADOS =')
print(f'Preço Inicial: R$: {preco:.2f}')
print(f'Preço Inflacionado: R$ {novo_preco:.2f}')
