# Faça um programa que verifique se a pessoa pertence à família “calvo” ou “silva”.

nome = input("Por favor, insira o seu nome completo: ")
nome = nome.lower()

if "calvo" in nome or "silva" in nome:
    print("\nVocê pertence à família Calvo ou à família Silva!")
else:
    print("\nVocê não pertence à minha família")