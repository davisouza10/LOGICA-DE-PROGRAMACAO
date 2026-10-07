import os
os.system('cls')


total_salario = 0
total_filhos = 0
total_familias = 0
maior_salario = 0
menor_salario = 0

opcao = ""

while opcao != "2":
    print("1 - Adicionar familia")
    print("2 - Sair e exibir resultados")
    opcao = input("Opcao: ")

    match opcao:
        case "1":
            salario = float(input("Salario: "))
            filhos = int(input("Numero de filhos: "))

            # Se for a PRIMEIRA familia, ela tem o maior e o menor salario de todos
            if total_familias == 0:
                maior_salario = salario
                menor_salario = salario
            else:
                if salario > maior_salario:
                    maior_salario = salario
                if salario < menor_salario:
                    menor_salario = salario

            total_salario += salario
            total_filhos += filhos
            total_familias += 1

        case "2":
            if total_familias > 0:
                print("Total familias:", total_familias)
                print("Media salario:", total_salario / total_familias)
                print("Media filhos:", total_filhos / total_familias)
                print("Maior salario:", maior_salario)
                print("Menor salario:", menor_salario)
            else:
                print("Nenhuma familia cadastrada.")

        case _:
            print("Opcao invalida!")