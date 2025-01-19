# %%

dados = ["pedro", "paulo", 22]

nome = dados[0]

# %%

# Isso é um dicionario.
# chave: valor
dados = {"nome": "Téo",
         "sobrenome": "Calvo",
         "idade": 31,
         "ex": ["Nah", "Josefina", "Elaine"],
         "filhos": [ {"nome": "Maria", "idade": 2}, {"nome": "Raul", "idade": 1} ]
         }

nome = dados["nome"]

# pegando a idade do primeiro filho
idade = dados["filhos"][0]["idade"]

print(idade)

print(nome)
# %%

# Retorna as chaves
dados.keys()

# %%

# Retorna os valores
valores = dados.values()
# converte valores para uma lista
print(list(valores))

# %%

# Retorna os pares chave : valor
dados.items()
# %%

