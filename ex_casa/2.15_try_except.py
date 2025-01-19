'''
Escreva um programa que receba uma lista de números do usuário e conte quantas vezes um número específico aparece na lista. 
Solicite ao usuário um número e exiba a contagem.
'''

numeros = []

while True:

    try:
        num = input("Digite um numero a ser adicionado na lista [Pressione ENTER para sair]: ")

        if num == "":
            break

        numeros.append(int(num))

    except ValueError:
        print("Entrada inválida! Digite um NÚMERO INTEIRO.")

try:
    ocorre = int(input("Digite o número que deseja saber a quantidade de ocorrências: "))

    if ocorre in numeros:
        qtd = numeros.count(ocorre)
        print(f"O numero {ocorre} aparece {qtd} vezes")

    else:
        print(f"O numero {ocorre} não aparece nenhuma vez")
except ValueError:
    print("Entrada inválida! Digite um NÚMERO INTEIRO.")