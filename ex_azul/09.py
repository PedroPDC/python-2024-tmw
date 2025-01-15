# Faça um programa que receba uma quantidade indefinida de valores correspondentes a “saldo em conta”, 
# mas quando o usuário apertar “enter” sem digitar valor algum, o programa para de receber valores, 
# e exibe a soma te todos os valores digitados anteriormente.

saldo = []

while True:
    num = input("Insira um valor (ou pressione Enter para finalizar): R$")
    
    if num == "":
        break

    if num.replace(".", "", 1).replace("-", "", 1).isdigit():
        saldo.append(float(num))
    else:
        print("Entrada inválida! Por favor, insira um número válido.")

saldo_total = sum(saldo)
print("\nO seu saldo total é de R$", saldo_total)

