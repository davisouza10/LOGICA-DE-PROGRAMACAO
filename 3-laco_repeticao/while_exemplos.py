import os
os.system('cls')

#Inivia a variavel soma com zero.
#Para evitar dar erro quando acumular os valores
#na variavel soma.
soma = 0
QUANTIDADE_NOTAS = 2

for i in range(QUANTIDADE_NOTAS):
    while True:
        nota = float(input(f'Digite a {i+1}ª nota entre 0 e 10: '))
        if nota >= 0 and nota <= 10:
            soma = soma + nota
            break # Serve para parar o laço de repetição.
        else:
            print() # Pular uma linha.
            print('Nota inválida, tente novamnete!')

media = soma / QUANTIDADE_NOTAS

print(f'Média: {media}')
print('= FIM =')