# %%

# "w" reescreve o arquivo
# "a" adiciona ao arquivo
arquivo = open("arquivo.txt", "w")

# %%
arquivo.write("Pedro Paulo")

# %%
arquivo.close()
# %%

arquivo = open("arquivo.txt", "r")
conteudo = arquivo.read()
arquivo.close()

print(conteudo)
print(type(conteudo))

# %%

arquivo = open("arquivo.txt", "r")
linhas = arquivo.readlines()
arquivo.close()

print(linhas)
# %%

with open("arquivo.txt", "r") as file:
    conteudo = file.read()

print(conteudo)