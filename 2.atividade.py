import os
os.system('cls')

# ENTRADA.
primeiro_numero = int(input('Digite o primeiro numero: '))
segundo_numero = int(input('Digite o segundo numero: '))
# PROCESSAMENTO.
soma = (primeiro_numero + segundo_numero)
media = (primeiro_numero + segundo_numero) / 2
produto = (primeiro_numero + segundo_numero)
if primeiro_numero < segundo_numero:
    menor = primeiro_numero
    maior = segundo_numero
else:
    menor = segundo_numero
    maior = primeiro_numero
if primeiro_numero == segundo_numero:
    iguais = 'Os números são iguais'
else:
    iguais = 'Os números são diferentes'
# SAIDA>
print('Media:', media)
print('Soma', soma)
print('Produto', produto)
print('Menor Valor', menor)
print('Maior Valor', maior)
print(iguais)