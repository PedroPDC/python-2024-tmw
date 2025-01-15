# Faça um programa que verifique se a pessoa pertence à família “calvo”.

nome = input("Por favor, insira o seu nome completo: ")
nome = nome.lower()

if "calvo" in nome:
    print("\nVocê pertence à família Calvo!")
else:
    print("\nVocê não pertence à minha família!")