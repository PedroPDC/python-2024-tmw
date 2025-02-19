# Números
# 1
# 10.0
# -5
# -7.54

# Booleanos
True
False

condicao = 12 > 18

if condicao:
    print("Isso é verdade")
else:
    print("Isso nunca vai acontecer")

# %%

idade = int(input("Entre com a sua idade: "))
cnh = input("Você tem CNH? ")

if idade >= 18 and cnh == "sim":
    print("Siga em frente!")
else:
    print("Preso em nome da lei!")

condicao = idade >= 18 and cnh == "sim"
print(condicao)

# %%

print(True * 100) # -> True vale 1
print(False * 100) # -> False vale 0

# %%

print(True * True)
print(False * True)
print(True * False)
print(False * False)

# E é MULTIPLICAÇÃO
print("True e True =", bool(1 * 1))
print("False e True =", bool(0 * 1))
print("True e False =", bool(1 * 0))
print("False e False =", bool(0 * 0))

# %%
# Ou é SOMA
print("True ou True =", bool(1 + 1))
print("False ou True =", bool(0 + 1))
print("True ou False =", bool(1 + 0))
print("False ou False =", bool(0 + 0))