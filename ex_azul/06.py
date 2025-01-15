# Faça um programa que verifique se o item que a pessoa escolheu para comprar na loja está na lista: laranja, cerveja, miojo, carvão, picanha.

lista = "laranja", "cerveja", "miojo", "carvão", "picanha"
item = input("Qual item deseja levar dessa loja? [laranja, cerveja, miojo, carvão, picanha] ")

if item in lista:
    print("O item:", item, "está em nossa lista de compras!")
else:
    print("O item:", item, "NÃO está em nossa lista de compras!")