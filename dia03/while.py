# %%

qtde = int(input("Quantas mensagens você quer? "))

count = 1
while count <= qtde:
    print("Alguma mensagem qualquer!")
    count += 1  # count = count + 1
# %%

while True:
    senha = input("Entre com a senha: ")

    if senha == "verdadeira":
        break
    
    elif senha == "pedro":
        print("quase...")
        continue

    print("Senha incorreta!")

print("Pronto! Saímos do laço.")
# %%

contador = 1

while contador <= 15:
    if contador % 2 == 0:
        print(contador)

    contador += 1
# %%
