import os

def logo_senai():
    os.system('cls')
    print('=========')
    print('  SENAI')
    print('=========')

def mostrar_dados(nome, idade):
    print(f'{nome} tem {idade} anos.')
    
logo_senai()
print('\n= SOLICITando DADOS =')
nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))

logo_senai()
print('\n= EXIBINDO DADOS =')
mostrar_dados(nome, idade)