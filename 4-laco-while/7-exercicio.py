import os
os.system('cls')

total_salario = 0
total_pessoas = 0
maior_idade = 0
menor_idade = 0
mulheres_5k = 0

opcao = ""

while opcao != "3":
    print("1 - Adicionar pessoa")
    print("2 - Exibir resultados")
    print("3 - Sair")
    opcao = input("Opcao: ")

    match opcao:
        case "1":
            idade = int(input("Idade: "))
            sexo = input("Sexo (M/F): ")
            salario = float(input("Salario: "))

            if total_pessoas == 0:
                maior_idade = idade
                menor_idade = idade
            else:
                if idade > maior_idade:
                    maior_idade = idade
                if idade < menor_idade:
                    menor_idade = idade

            total_salario += salario
            total_pessoas += 1

            if (sexo == "F" or sexo == "f") and salario >= 5000:
                mulheres_5k += 1

        case "2":
            if total_pessoas > 0:
                print("Media salario:", total_salario / total_pessoas)
                print("Maior idade:", maior_idade)
                print("Menor idade:", menor_idade)
                print("Mulheres com salario >= 5000:", mulheres_5k)
            else:
                print("Nenhuma pessoa cadastrada.")

        case "3":
            print("Saindo...")

        case _:
            print("Opcao invalida!")