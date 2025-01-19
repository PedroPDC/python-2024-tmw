'''
Faça um programa que receba um número. Verifique se o número informado é par ou ímpar. Exiba o resultado da seguinte maneira:

	O número x é impar
ou
	O número x é par '''

num = int(input("Digite um numero: "))

if num % 2 == 0:
    print("\nO numero:", num, "é PAR.")
else:
    print("\nO numero:", num, "é IMPAR.")