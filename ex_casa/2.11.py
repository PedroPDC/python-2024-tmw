'''
Faça um programa com uma função que recebe uma frase. Para cada palavra nesta frase, inverta a ordem das letras. Exiba o resultado:

	Esta é a frase original

	atsE é a esarf lanigiro
'''

frase = input("Digite uma frase: ")
print(f"\n{frase} \n\n{frase[::-1]}")