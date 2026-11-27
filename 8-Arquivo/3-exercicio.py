from dataclasses import dataclass
import os
os.system('cls')

# Crie um programa usando uma classe com
# as informacoes abaixo e salve em um
# arquivo fornecedor.csv:
# Fornecedor
# Nome, E-Mail, Telefone, Endereço
# Escreva em outro arquivo Python para
#  ler os dados de fornecedor.csv e mostrar
# de forma organizada no terminal

from dataclasses import dataclass
import os
os.system('cls' if os.name == 'nt' else 'clear')


@dataclass
class Fornecedor:
    nome: str
    email: str
    telefone: str
    endereco: str


arquivo = 'fornecedor.csv'

print('=== Cadastro de Fornecedores ===')
while True:
    fornecedor = Fornecedor(
        nome=input('Nome: ').strip(),
        email=input('E-Mail: ').strip(),
        telefone=input('Telefone: ').strip(),
        endereco=input('Endereço: ').strip(),
    )

    # Gravando no arquivo (modo 'a' adiciona sem apagar o que já existe).
    with open(arquivo, 'a', encoding='utf-8') as arquivo_fornecedor:
        arquivo_fornecedor.write(
            f'{fornecedor.nome},{fornecedor.email},'
            f'{fornecedor.telefone},{fornecedor.endereco}\n'
        )

    print(f'\nFornecedor {fornecedor.nome} salvo em {arquivo}!\n')

    if input('Cadastrar outro? (s/n): ').strip().lower() != 's':
        break