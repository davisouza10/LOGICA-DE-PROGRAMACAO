import os
os.system('cls')

# ENTRADA.
peso = float(input('Digite seu peso (kg): '))
altura = float(input('Digite sua altura (m): '))
# PROCESSAMENTO.
imc = peso / (altura ** 2)
print(f'\nSeu IMC é: {imc:2f}')

if imc < 18.5:
    print('Classificação: abaixo do peso')
elif imc < 25:
    print('Classificação: Peso ideal(Parabéns)')
elif imc < 30:
    print('Classificação: Levemente acima do peso')
elif imc < 35:
    print('Classificação: Obesidade Grau I')
elif imc < 40:
    print('Classificação: Obesidade Grau II(severa)')
else:
    print('Classificação: Obesidade Grau III(mórbida)')
# SAIDA.
