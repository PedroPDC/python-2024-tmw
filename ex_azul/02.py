# Faça um programa que vende uma garrafa de água:
# A) Se o cliente escolher água mineral natural, será cobrado R$1,50
# B) Se o cliente escolher água mineral com gás, será cobrado R$2,50
# Altere o programa anterior para considerar a quantidade de água.

print("Olá! Escolha o tipo de água que você quer:")
print("A) Água mineral natural, preço: R$ 1,50")
print("B) Água mineral com gás, preço: R$ 2,50\n")

tipo = input("Escolha A ou B: ")
tipo = tipo.upper()

quantidade = int(input("Quantas àguas você deseja? "))

if tipo == "A":
    total = 1.5 * quantidade
    print("\nMuito obrigado pela compra da água mineral natural, valor total: R$", total)
elif tipo == "B":
    total = 2.5 * quantidade
    print("\nMuito obrigado pela compra da água mineral com gás, valor total: R$", total)
else:
    print("\nPor favor, escolha uma opção válida!")