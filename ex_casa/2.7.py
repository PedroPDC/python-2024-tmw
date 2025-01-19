# Escreva um programa que crie um dicionário com nomes de frutas 
# como chaves e seus respectivos preços como valores. 
# Solicite ao usuário o nome de uma fruta e exiba o preço correspondente.

frutas = {
    "Maçã": 1.50,
    "Pera": 1.25,
    "Goiaba": 2.15,
    "Banana": 2.75,
    "Laranja": 0.65,
    "Abacaxi": 3.20,
    "Uva": 1.90,
    "Limão": 1.25,
    "Jaca": 5.80,
}

fruta = input("Insira o nome de uma fruta [Maçã/Pera/Goiaba/Banana/Laranja/Abacaxi/Uva/Limão/Jaca]: ")

print(f"O preço da {fruta} é de R$ {frutas[fruta]}")