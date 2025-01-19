# %%

minha_lista_vazia = []

print(minha_lista_vazia)
# %%

minha_lista = ["Pedro", "Paulo", 22, 1.77]
print(minha_lista)

# %%

minha_lista[0] # indice 0 da lista

# %%

minha_lista[3]

# %%

len(minha_lista_vazia) # tamanho da lista
minha_lista[len(minha_lista)-1] # ultimo elemento da lista

# %%

minha_lista[-1] # retorna ultimo elemento da lista
# %%

# SLICED Lista (Fatiamento de Listas)

# SINTAXE: minha_lista[inicio:fim]
# minha_lista[0:1]
# qtde de elementos = fim - inicio
# qtde de elementos = 1 - 0
# Ou seja, dessa forma estariamos pegando apenas 1 elemento da lista, o elemento "Pedro"

# Para pegarmos o nome e o sobrenome
minha_lista[0:2]

# %%

minha_lista[0:-1] # Todos os itens menos o ULTIMO

# %%

minha_lista[0:int(len(minha_lista)/2)] # Pegar metade da lista
# %%

minha_lista[:2] # Outra forma de pegarmos o nome e o sobrenome
minha_lista[2:] # Pegamos do 2 elemento até ultimo

# %%

# Pega a lista inteira, pulando de 2 em 2 (step 2)
minha_lista[::2] # start:stop:step

# %%

minha_lista[::-1] # inverte a ordem dos itens da lista

# %%

minha_lista[::-2]
# %%
