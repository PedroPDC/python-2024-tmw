# %%

def soma(*args):
    total = 0

    for i in args:
        total += i

    return total

soma(10, 20, 100)
# %%

def operacao(op, *num):
    total = 0

    if op == "soma":
        for i in num:
            total += i
    
    elif op == "multi":
        total = 1
        for i in num:
            total *= i
    
    return total

operacao("multi", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# %%

dados = ["Teo", "Calvo", 31, ["Maria", "Elaine", "Josefina"]]

# descompactando uma lista
# Dessa forma, atribui os dois primeiros elementos as seguintes variaveis,
# e o restante joga no "lixo" (variavel *lixo), normalmente utilizam *_
nome, sobrenome, *lixo, ex = dados

print(nome)
print(sobrenome)
print(ex)

# %%

# Inverter o valor das variaveis - FORMA "CLASSICA"
a = 10
b = 20
print(a, b)

c = a
a = b
b = c

print(a, b)
# %%

# No Python podemos fazer da seguinte maneira:
a = 10
b = 20
print(a, b)

# Jogamos uma tupla (b, a) para elementos novos (a, b)
a, b = b, a
print(a, b)
# %%

x = 10, 20 # é uma tupla
type(x)

# %%
