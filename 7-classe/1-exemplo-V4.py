from dataclasses import dataclass
import os
os.system('cls')

@dataclass
class Cliente:
    # Nome da variavel : tipo da variavel
    nome: str
    idade: int
    altura: float

lista_clientes = []

print('SOLICITANDO DADOS DE DOIS CLIENTES')
for i in range(2):
    dados_do_cliente = Cliente(
        nome= input('Digite o nome do cliente: '),
        idade= int(input('Digite sua idade: ')),
        altura= float(input('Digite sua altura: '))
    )
    lista_clientes.append(dados_do_cliente)

print('\nEXIBINDO DADOS')
for cliente in lista_clientes:    
    print(f'Nome: {cliente.nome}')
    print(f'Idade: {cliente.idade}')
    print(f'Idade: {cliente.altura}')
    print('='*15)