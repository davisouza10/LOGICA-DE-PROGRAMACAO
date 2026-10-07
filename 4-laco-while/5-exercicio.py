import os
os.system('cls')

soma_nota = 0
contador = 0


while True:
    nota = float(input('Digite uma nota: '))
    soma_nota += nota
    contador += 1
    resposta = input('Deseja inserir mais uma nota?: (S/N)').strip().upper()

    if resposta == 'N':
        break

    if contador > 0:
        media = soma_nota / contador
        print(f'\nQuantidade de notas inseridas: {contador}')
        print(f'A média aritmetica é: {media:.2f}')
    else:
        print('\nNenhuma nota foi informada.')

