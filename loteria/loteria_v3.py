def valida_entrada():
    while True:
        try: 
            numero = int(input("Entre com um número entre 1 e 15: "))

        except ValueError:
            print("Ô animal, eu pedi um numero")
            continue

        if 1 <= numero <= 15:
            return numero
        else:
            print("Entre com um número válido!")

numero_sorte = 7

for i in range(3):
    
    numero = valida_entrada()

    if numero == numero_sorte:
        print("Você acertou!!")
        break

    elif numero > numero_sorte:
        print("Você errou! Tente um numero menor!")
    else:
        print("Você errou! Tente um numero maior!")
