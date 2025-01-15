# Faça um programa que vende uma garrafa de água:
# A) Se o cliente escolher água mineral natural, será cobrado R$1,50
# B) Se o cliente escolher água mineral com gás, será cobrado R$2,50

print("Olá! Escolha o tipo de água que você quer:")
print("A) Água mineral natural, preço: R$ 1,50")
print("B) Água mineral com gás, preço: R$ 2,50\n")

tipo = input("Escolha A ou B: ")
tipo = tipo.upper()

if tipo == "A":
    print("\nMuito obrigado pela compra da água mineral natural, valor total: R$ 1,50")
elif tipo == "B":
    print("\nMuito obrigado pela compra da água mineral com gás, valor total: R$ 2,50")
else:
    print("\nPor favor, escolha uma opção válida!")