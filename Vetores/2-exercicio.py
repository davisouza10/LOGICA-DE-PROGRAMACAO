import os
os.system('cls')

print('=== INSERINDO NÚMEROS DO VETOR ===')
vetor_numeros = []
QUANTIDADE_NUMEROS = 5
quantidade_negativo = 0
soma_positiva = 0

for i in range(QUANTIDADE_NUMEROS):
    numero = float(input('Digite o {i+1}º número: '))
    vetor_numeros.append(numero)
# NUMEROS POSITIVOS
    if numero < 0:
        quantidade_negativo += 1
    elif numero > 0:
        soma_positiva += numero
        
print("\n--- Resultados ---")
print(f"Vetor preenchido: {vetor_numeros}")
print(f"Quantidade de números negativos: {quantidade_negativo}")
print(f"Soma dos números positivos: {soma_positiva}")
