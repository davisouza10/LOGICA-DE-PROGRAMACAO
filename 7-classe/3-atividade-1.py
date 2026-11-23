from dataclasses import dataclass
import os
os.system('cls')

# CRIE UMA CLASSE PARA UM PACIENTE.
# DADOS: NOME, IDADE, TELEFONE, ENDEREÇO.

# CRIE A FUNÇÃO PARA MOSTRAR:
# - TODOS OS DADOS
# - NOME E IDADE
# - NOME E TELEFONE

@dataclass
class Paciente:
    nome: str
    idade: int
    telefone: str
    endereco: str
    
    def mostrar_dados(self):
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')
        print(f'Telefone: {self.telefone}')
        print(f'Endereço: {self.endereco}')
        print('='*30)
        
    def mostrar_nome_idade(self):
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')
        print('='*30)

    def mostrar_nome_telefone(self):
        print(f'Nome: {self.nome}')
        print(f'Telefone: {self.telefone}')
        print('='*30)
        
lista_pacientes = []

for i in range(2):
    dados = Paciente(
        nome= input('Digite o nome do paciente: '),
        idade= int(input('Digite sua idade: ')),
        telefone= input('Digite o seu número: '),
        endereco= input('Digite seu endereço: ')
    )
    lista_pacientes.append(dados)
    
print('\n= EXIBINDO DADOS =')
for pacientes in lista_pacientes:
    pacientes.mostrar_dados()
    
print('\n= EXIBINDO NOME E IDADE =')
for pacientes in lista_pacientes:
    pacientes.mostrar_nome_idade()
    
print('\n= EXIBINDO NOME E TELEFONE =')
for pacientes in lista_pacientes:
    pacientes.mostrar_nome_telefone()