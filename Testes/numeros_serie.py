import os
os.system('csl')

while True:
    nome = input('Digite um nome: ')
    match nome:
        case 'João':
          print('Ai não!')
          break
        case 'Davi':
          print('Ai Sim!')
          break
        case _:
          print('Não Indentificado!')
          print('Tente de Novo!')