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
    
    # Função dentro da classe.
    def mostrar_dados(self):
        print(f'Nome: {self.nome}')
        print(f'Telefone: {self.telefone}')
        print(f'E-Mail: {self.email}')
        print('='*30)
        
    # Função somente para enviar e-mails.
    def email_marketing(self):
        print(f'Nome: {self.nome}')
        print(f'E-Mail: {self.email}')
        print('='*30)
        
        # Função somente para enviar whatsapp.
    def whatsapp_marketing(self):
        print(f'Nome: {self.nome}')
        print(f'Telefone: {self.telefone}')
        print('='*30)
        
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
    cliente.mostrar_dados()
    
    print('\n= EXIBINDO E-MAIL MARKETING =')
for cliente in lista_clientes:
    cliente.email_marketing()
    
print('\n= EXIBINDO WHATSAPP MARKETING =')
for cliente in lista_clientes:
    cliente.whatsapp_marketing()