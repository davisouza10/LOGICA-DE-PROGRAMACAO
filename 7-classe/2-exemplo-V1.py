from dataclasses import dataclass
import os
os.system('cls')

# CRIE UMA CLASSE PARA OS DADOS DE UM CLIENTE.
# DADOS: NOME, TELEFONE E E-MAIL.

@dataclass
class Cliente:
    # Nome da variavel : tipo da variavel
    nome: str
    telefone: str
    email: str

lista_clientes = []

print('= SOLICITANDO DADOS DE DOIS CLIENTES =')
for i in range(2):
    dados = Cliente(
        nome= input('Digite o nome do cliente: '),
        telefone= input('Digite seu número: '),
        email= input('Digite seu e-mail: ')
    )
    lista_clientes.append(dados)
    
print('\n= EXIBINDO DADOS =')
for cliente in lista_clientes:
    print(f'Nome: {cliente.nome}')
    print(f'Telefone: {cliente.telefone}')
    print(f'E-Mail: {cliente.email}')
    print('='*30)