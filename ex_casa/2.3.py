# Escreva um programa que solicite ao usuário um nome e uma idade, 
# e crie um dicionário com essas informações. 
# Em seguida, exiba o dicionário.

nome = input("Digite um nome: ")
idade = int(input("Digite uma idade: "))

dados = {"nome": nome, "idade": idade}
print(dados)
