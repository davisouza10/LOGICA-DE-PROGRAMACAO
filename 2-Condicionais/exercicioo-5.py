import os
os.system('cls')

# ENTRADA.
print('== MERCADINHO SENAI ==')
valor_produto = float(input('Digite o preço do produto: '))

print('''
\n== FORMA DE PAGAMENTO ==
1- Pagamento à vista
2- Pagamento à prazo
''')
forma_de_pagamento = int(input('Digite um número para forma de pagamento: '))

# PROCESSAMENTO
match forma_de_pagamento:
    case 1:
        valor_do_desconto = valor_produto * 0.10
        valor_final = valor_produto - valor_do_desconto

        # SAÍDA.
        print(f'\nValor do produto: R$ {valor_produto:.2f}')
        print('Forma de pagamento: à vista')
        print(f'Valor do desconto: R$ {valor_do_desconto:.2f}')
        print(f'Total a pagar: R$ {valor_final:.2f}')
    case 2:
        quantidade_parcelas = int(input('Digite a quantidade de parcelas: '))
        if quantidade_parcelas > 6:
            print('Quantidade de parcelas inválida.')
            exit() # FIM DO PROGRAMA.

        valor_por_parcela = valor_produto / quantidade_parcelas

        # SAÍDA.
        print(f'\nValor do produto: R$ {valor_produto:.2f}')
        print('Forma de pagamento: à prazo')
        print(f'Quantidade de parcelas: {quantidade_parcelas}')
        print(f'Valor por parcela: R$ {valor_por_parcela:.2f}')
        print(f'Total a pagar R$: {valor_produto:.2f}')

    case _:
        print('Opção inválida.')