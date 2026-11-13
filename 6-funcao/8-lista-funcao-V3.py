import os
os.system('cls')

# Função com parâmetro e com retorno.
def calcular_media(nota1, nota2):
    resultado = (nota1 + nota2) / 2
    return resultado

def verificar_resultado(media):
    if media >= 7:
        resultado = 'Aprovado'
    else:
        resultado = 'Reprovado'
    return resultado

print('= SOLICITANDO DADOS =')
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

# Usando a função com parâmetro e
# inserindo o retorno na variável media.
media = calcular_media(nota1, nota2)
situacao = verificar_resultado(media)

print('= EXIBINDO DADOS =')
print(f'Média: {media}')
print(f'Resultado: {situacao}')
