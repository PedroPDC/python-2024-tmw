# Faça um programa que conte quantas vezes a letra “a” aparece em uma palavra

palavra = input("Insira uma palavra: ")

qtd = 0
for i in palavra:
    if i == "a":
        qtd += 1

print("\nA palavra", palavra, "possui", qtd, "letras 'A'")