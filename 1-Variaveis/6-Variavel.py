import os
os.system('cls')

a = 5
b = 10

#1. Guardamos o valor de 'a' no 'copo de apoio'
temp = a   #temp passa a valer 5

#2. Agora podemos sobrescrever 'a' com o valor de 'b'
a = b  # 'a' passa a valer 10

#3. Passamos o valor guardado em 'temp' para 'b'
b = temp  # 'b' passa a valer 5

print(f'a: {a}')  # Imprime: 10
print(f'b: {b}')  # Imprime: 5