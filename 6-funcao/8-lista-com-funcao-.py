import os
os.system('cls')

# Função com parâmetro e com retorno.
def calcular_notas(nota1, nota2):
    resultado = nota1 + nota2
    return resultado

print('= SOLICITANDO DADOS =')
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

# Usando a função com parâmetro e
# inserindo o retorno na variável soma.
soma = calcular_notas(nota1, nota2)

print('= EXIBINDO DADOS =')
print(f'Soma: {soma}')