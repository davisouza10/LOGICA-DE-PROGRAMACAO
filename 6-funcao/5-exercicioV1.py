from dataclasses import dataclass
import os
os.system('cls')

@dataclass
class Produto:
    nome: str
    preco: float

lista_produtos = []

def solicitar_dados():
    for i in range(3):
        print(f'\nProduto {i + 1}')
        nome = input('Digite o nome do produto: ')
        preco = float(input('Digite o preço do produto: ').replace(',', '.'))
        produto = Produto(nome, preco)
        lista_produtos.append(produto)


def mostrar_dados(lista_produtos):
    for i, produto in enumerate(lista_produtos, start=1):
        print(f'{i} - {produto.nome} | R$ {produto.preco:.2f}')


print('= SOLICITANDO DADOS =')
solicitar_dados()

print('\n= EXIBINDO DADOS =')
mostrar_dados(lista_produtos)