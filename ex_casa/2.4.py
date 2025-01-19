'''Faça um programa que receba 4 notas de um aluno. Retorne a média dessas notas, a menor e a maior nota:

Média: x
Menor: y
Maior: z
'''

n1 = float(input("Entre com a 1º nota: "))
n2 = float(input("Entre com a 2º nota: "))
n3 = float(input("Entre com a 3º nota: "))
n4 = float(input("Entre com a 4º nota: "))

menor = n1

if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3
if n4 < menor:
    menor = n4

maior = n1

if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3
if n4 > maior:
    maior = n4

media = (n1 + n2 + n3 + n4) / 4

print("\nA média das notas é igual a:", media)
print("A menor nota é:", menor)
print("A maior nota é:", maior)
