# Faça um programa que receba 4 alturas, armazene em uma lista e depois mostre a soma dessas alturas.

alturas = []

for i in range(4):
    alturas.append(float(input("Informe uma altura (em metros): ")))

soma_alturas = sum(alturas)

print("A soma das alturas é igual a:", soma_alturas,"metros")