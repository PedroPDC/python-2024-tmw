# Faça um programa que receba um número em segundos, 
# converta esse numero para horas, minutos e segundos. Exemplos:
# Entrada 556 -> Saída: 0:9:16
# Entrada 140153 -> 38:55:53

segundos = int(input("Digite um número em segundos: "))

horas = segundos // (60 * 60) # Horas inteiras

segundos = segundos % (60 * 60) # Resto de segundos da divisão por hora

minutos = segundos // 60 # Minutos inteiros

segundos = segundos % 60 # Resto de segundos da divisão por minuto

print(horas, minutos, segundos, sep=":")