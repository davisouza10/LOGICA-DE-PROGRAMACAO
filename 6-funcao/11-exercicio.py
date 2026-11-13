import os
os.system('cls')  # Limpa a tela (só funciona no Windows)

# ===== DEFINIÇÃO DAS FUNÇÕES =====
# Definir uma função NÃO executa nada. Ela só ensina o Python
# a fazer a tarefa. A execução acontece quando a função é chamada.

# Recebe dois números (parâmetros) e devolve a soma.
def somar(num1, num2):
    return num1 + num2  # 'return' devolve o resultado para quem chamou

# Recebe dois números e devolve a subtração.
def subtrair(num1, num2):
    return num1 - num2

# Recebe dois números e devolve a divisão.
def dividir(num1, num2):
    # Dividir por zero gera erro, então testamos antes.
    if num2 == 0:
        return 'Não é possível dividir por zero'  # encerra a função aqui
    else:
        return num1 / num2  # só chega aqui se num2 for diferente de 0

# Recebe dois números e devolve a multiplicação.
def multiplicar(num1, num2):
    return num1 * num2

# ===== PROGRAMA PRINCIPAL =====

print('= SOLICITANDO DADOS =')
# input() devolve texto; int() converte para número inteiro.
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

# Aqui as funções são CHAMADAS. O valor que cada uma devolve
# com 'return' é guardado na variável à esquerda do '='.
soma = somar(num1, num2)
subtracao = subtrair(num1, num2)
divisao = dividir(num1, num2)
multiplicacao = multiplicar(num1, num2)

print('= EXIBINDO DADOS =')
# O f antes das aspas permite colocar variáveis dentro das chaves {}.
print(f'Soma: {soma}')
print(f'Subtracao: {subtracao}')
print(f'Divisao: {divisao}')
print(f'Multiplicacao: {multiplicacao}')