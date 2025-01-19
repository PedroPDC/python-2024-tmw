'''
Faça um programa que receba um número e exiba seu fatorial.
'''

num = int(input("Digite um número: "))

if num == 0:
    print(f"O fatorial de {num} é 1")

else:
    res = 1
    for i in range(1, num):
        res = res * (i + 1)

print(f"O fatorial de {num}! é {res}")