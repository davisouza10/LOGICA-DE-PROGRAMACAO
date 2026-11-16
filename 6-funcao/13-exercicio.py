import os
from datetime import date
os.system('cls')

# Escreva um programa que solicite ao usuário o ano de
# nascimento e, utilizando uma função, retorne com a idade
# do usuário.

def calcular_idade(ano_nascimento):
    ano_atual = date.today().year
    return ano_atual - ano_nascimento

print('= SOLICITANDO DADOS =')
ano_nascimento = int(input('Digite seu ano de nascimento: '))

idade_usuario = calcular_idade(ano_nascimento)

print('\n= EXIBINDO DADOS =')
print(f'Voce nasceu em: {ano_nascimento} e tem: {idade_usuario} anos.')