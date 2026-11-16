import os
os.system('cls')

def calcular_notas(lista_notas):
    return sum(lista_notas) / len(lista_notas)

def mostrar_notas(lista_notas):
    print('\n= EXIBINDO NOTAS =')
    for nota in lista_notas:
        print(f'Nota: {nota}')
   
def status_do_aluno(media):
    if media >= 7:
        resultado = 'Aprovado'
    else:
        resultado = 'Reprovado'
    return resultado

lista_notas = []

print('= SOLICITANDO NOTAS =')
for i in range(2):
    while True:
        nota = float(input('Digite uma nota: '))
        if nota >= 0 and nota <= 10:
            lista_notas.append(nota)
            break
        else:
            print('Nota inválida, tente novamente!\n')
   
media = calcular_notas(lista_notas)
status_aluno = status_do_aluno(media)

print('\n= EXIBINDO RESULTADOS =')
mostrar_notas(lista_notas)
print(f'\nMédia: {media}')
print(f'Situação do aluno: {status_aluno}')