# Escreva um programa que solicite ao usuário duas strings e 
# as concatene em uma única String. 
# Em seguida, exiba a String resultante.

lista = []

for i in range(2):
    lista.append(input("Digite uma string: "))

lista_concatenada = "".join(lista)

print(lista_concatenada)