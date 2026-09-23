import os
os.system('cls')

nome_produto = input('Digite o nome do produto: ')
preco_unitario = float(input('Digite o preço do produto (R$): '))
quantidade = int(input('Digite a quantidade: '))

valor_total = preco_unitario * quantidade

print('\n--- RESUMO DO PEDIDO ---')
print(f'Produto: {nome_produto}')
print(f'Quantidade: {quantidade}')
print(f'Total a pagar: R$ {valor_total:.2f}')