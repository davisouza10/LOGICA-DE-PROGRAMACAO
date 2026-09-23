import os
os.system('cls')

#print('MOSTRANDO OS NÚMEROS PARES ENTRE 1 E 10.')
#for i in range(1, 11):
  #  if i % 2 == 0:
     #   print(f'{i} é par.')

#print('FIM')

numero = int(input('Digite um número: '))
if numero % 2 == 1:
    print(f'{numero} é impar.')
else:
    print(f'{numero} é par.')

print('FIM')