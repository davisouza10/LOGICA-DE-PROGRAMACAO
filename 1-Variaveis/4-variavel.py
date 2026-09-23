import os
os.system('cls')
# ENTRADAS (Valores guardados em variáveis)
preco_produto = 50.00
quantidade = 3
taxa_desconto = 0.10   #10%

# Cálculos usando as variáveis
subtotal = preco_produto * quantidade
desconto = subtotal * taxa_desconto
valor_final = subtotal - desconto

print(f'Subtotal: R$ {subtotal:2f}')
print(f'Desconto: R$ {desconto:2f}')
print(f'Total a pagar: R$ {valor_final:2f}')