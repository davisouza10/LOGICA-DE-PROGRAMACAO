import os
os.system('cls')

# Escreva um programa que permita ler 3 notas de um aluno,
# usando laço de repetição e vetor, informe por meio de uma
# função a média;

#notas = []

#def calcular_media(notas):
    #return sum(notas) / len(notas)

#print('= SOLICITANDO DADOS =')
#for i in range(3):
    #nota = float(input(f'Digite a nota {i + 1}: '))
    #notas.append(nota)

#media = calcular_media(notas)

#print('= EXIBINDO DADOS =')
#rint(f'Notas: {notas}')
#print(f'Média: {media:.2f}')

# Escreva um programa que permita ler 3 notas de um aluno,
# usando laço de repetição e vetor, informe por meio de uma
# função a média;

def calcular_notas(lista_notas):
    return sum(lista_notas) / len(lista_notas)

def mostrar_resultado(media, lista_notas):
    print('\n= EXIBINDO NOTAS =')
    for nota in lista_notas:
        print(f'Nota: {nota}')
        
    print(f'\nMédia: {media:.2f}')
    
lista_notas = []

for i in range(3):
    nota = float(input('Digite uma nota: '))
    lista_notas.append(nota)
    
media = calcular_notas(lista_notas)

mostrar_resultado(media, lista_notas)