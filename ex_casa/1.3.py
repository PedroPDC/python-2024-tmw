# Faça um programa que receba o raio de uma circunferencia em centimetros.
# Retorne para o usuário qual é a area e o perimetro desda circunferencia no seguinte formato
# Área: x.xx
# Perímetro: y.yy

raio = float(input("Por favor, insira o raio da circunferencia: "))

area = 3.14 * (raio * raio)
perimetro = 2 * 3.14 * raio

print("\nA área de uma circunferencia de raio:", raio, "é igual a:", round(area,2), "cm²")
print("O perímetro de uma circunferencia de raio:", raio, "é igual a:", round(perimetro,2), "cm²")