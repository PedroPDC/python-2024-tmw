'''
Faça um programa que receba um número. 
Este número corresponde a uma posição na sequência de Fibonacci: 1, 1, 2, 3, 5,...

Exiba o número da sequência cuja posição foi informada:
	A posição x corresponde ao número y

'''

num = int(input("Informe um numero: "))

if num == 1:
    print(f"A posição {num} corresponde ao número 0")

else:
    a = 0
    b = 1 

    for i in range(2, num):
        soma = a + b
        a = b
        b = soma

print(f"A posição {num} corresponde ao numero {b}")