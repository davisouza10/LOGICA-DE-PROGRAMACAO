from dataclasses import dataclass
import os
os.system('cls')

@dataclass
class Clientes:
    nome: str
    idade: int
    altura: float
    
lista_clientes = []

# Lendo um arquivo.
arquivo = 'dados_clientes.csv'
with open(arquivo, 'r') as arquivo_clientes:
    for linha in arquivo_clientes:
        nome, idade, altura = linha.strip().split(',')
        lista_clientes.append(Clientes(
            nome=nome, idade=int(idade), altura=float(altura)
        ))
        
print('\nExibindo dados dos clientes: ')
for cliente in lista_clientes:
    print(f'Nome: {cliente.nome}')
    print(f'Idade: {cliente.idade}')
    print(f'Altura: {cliente.altura}')
    print('==========================')