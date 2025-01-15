''' Faça o programa de uma sorveteria, onde o usuário pode escolher:
Tipo de sorvete: casquinha (R$1,00), cascão (R$2,50), cestinha (R$4,00)
Sabor do sorvete: morango, creme, chocolate
Cobertura: Caramelo (R$1,50), morango (R$1,50), chocolate (R$1,50), sem cobertura (R$0,00)
Apresente o valor a ser pago '''

print("Olá! Qual será o seu pedido?")

tipo_sorvete = input("Selecione o tipo de sorvete que você quer! casquinha (R$1,00), cascão (R$2,00), cestinha (R$4,00): ")
tipo_sorvete = tipo_sorvete.upper()

sabor = input("Selecione o sabor do sorvete! Morango, Creme ou Chocolate: ")
sabor = sabor.upper()

cobertura = input("Selecione a cobertura que você quer! Caramelo (R$1,50), morango (R$1,50), chocolate (R$1,50), sem cobertura (R$0,00): ")
cobertura = cobertura.upper()

valor = 0.0

# Essa parte é do tipo de sorvete
if tipo_sorvete == "CASQUINHA":
    valor += 1.0
elif tipo_sorvete == "CASCÃO" or tipo_sorvete == "CASCAO":
    valor += 2.0
elif tipo_sorvete == "CESTINHA":
    valor += 4.0
else:
    print("Selecione uma opção válida!")

# Essa parte é da cobertura
if cobertura == "CARAMELO":
    valor += 1.50
elif cobertura == "MORANGO":
    valor += 1.50
elif cobertura == "CHOCOLATE":
    valor += 1.50
elif cobertura == "SEM" or cobertura == "SEM COBERTURA" or cobertura == "":
    pass
else:
    print("Selecione uma opção válida!")

print("\nVocê escolheu o sorvete tipo: ", tipo_sorvete, ", sabor: ", sabor, " e cobertura: ", cobertura)
print("Valor total a ser pago: R$", round(valor, 2))
