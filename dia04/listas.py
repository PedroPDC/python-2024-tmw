# %%

minha_lista = []
print(minha_lista)
# %%

minha_lista = ["Pedro", "Paulo", 22, 1.77]
print(minha_lista)
# %%

# Primeiro elemento
minha_lista[0]

# %%

# Segundo elemento
minha_lista[1]

# %%

# Ultimo elemento
minha_lista[-1]

# %%

# Fatiamento de listas

# Primeiros dois elementos da lista
minha_lista[:2]


# %%

# Ultimos dois elementos da lista
minha_lista[-2:]

# %%

# Cria uma copia da lista
nova_lista = minha_lista[:]
print(nova_lista)

# %%

# Inverte a lista de trás pra frente
minha_lista[::-1]
# %%

# Mostra a lista de 2 em 2 elementos
minha_lista[::2]

# %%

notas = []
nota = 7.75

notas.append(nota) 
print(notas)

notas.append(10) 
print(notas)

# Se usassemos o metodo append estariamos adicionando uma lista dentro de outra...
# O que no nosso caso, nao seria o correto
# Portanto utilizaremos o metodo extend
notas.extend([5.75, 6.24])
print(notas)

# Outra forma de fazermos uma adição de valores a uma lista
notas = notas + [10, 9.25]
print(notas)

# %%

notas.remove(10)
print(notas)

# %%

nomes = ["pedro", "teo", "paulo", "maria"]
for i in nomes:
    print(i.title())

nomes.extend(["jose", "lais"])
print(nomes)
 # %%

dados = ["Teo", "Calvo", 31, ["Maria", "Josefina", "Elaine"], ["Joana"]]
dados[3][-1]

# %%

dados[-1][0][0]
# %%
