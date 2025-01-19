'''
Escreva um programa que solicite ao usuário um número e exiba a tabuada desse número de 1 a 10.
'''

num = int(input("Digite um número que deseja saber a tabuada: "))

for i in range(1, 11):
    res = num * i
    print(f"{num} X {i} = {res}")
