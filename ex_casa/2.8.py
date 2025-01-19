'''
Refaça o exercício 2.4 utilizando for e listas para receber as notas dos alunos
'''

notas = []

for i in range(4):
    notas.append(float(input("Digite as suas notas: ")))

media = sum(notas) / len(notas)

print("\nA média das notas é igual a:", media)
print("A menor nota é:", min(notas))
print("A maior nota é:", max(notas))
