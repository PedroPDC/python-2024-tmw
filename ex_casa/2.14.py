'''
Considere a seguinte lista:
[123, 435, 987, 1984, 2, 19, 423, -178, 320]

Faça um programa que retorne a posição do menor e do maior valor encontrado:

O maior valor está na posição x
O menor valor está na posição y

'''

numeros = [123, 435, 987, 1984, 2, 19, 423, -178, 320]

for i in range(len(numeros)):
    pos_maior = numeros.index(max(numeros))
    pos_menor = numeros.index(min(numeros))

print(f"O maior valor {max(numeros)}, está na posição {pos_maior}")
print(f"O menor valor {min(numeros)}, está na posição {pos_menor}")


