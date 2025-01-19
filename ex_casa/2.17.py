'''
Escreva um programa que solicite ao usuário uma palavra e verifique se a palavra é um palíndromo 
(ou seja, é a mesma palavra quando lida de trás para frente).
Exemplos de palíndromos: Osso, Ana, Radar, Roma é amor
'''

palavra = input("Digite uma palavra: ").lower()
reverso = palavra[::-1]

if palavra == reverso:
    print(f"A palavra: {palavra} é palíndromo")
else:
    print(f"A palavra: {palavra} não é palíndromo")