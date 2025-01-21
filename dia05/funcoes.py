# y = f(x) = x + 10
# y = f(x) = x * x + 1

# %%
def funcao(x):
    res = x + 10
    return res


# %%

y = funcao(100)
print(y)

# %%

# Definição da função
def aleatoria():
    print("aleatoria")

# Invocação da função
aleatoria()
# %%

def soma(a, b):
    return a + b

res = soma(10, 5)
print(res)
# %%
def soma(a, b=0):
    return a + b

res = soma(10)
print(res)
# %%
