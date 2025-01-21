numero_sorte = 7

for i in range(3):
    
    while True:
        try: 
            numero = int(input("Entre com um número entre 1 e 15: "))
            break

        except ValueError:
            print("Ô animal, eu pedi um numero")

    if numero == numero_sorte:
        print("Você acertou!!")
        break

    elif numero > numero_sorte:
        print("Você errou! Tente um numero menor!")
    else:
        print("Você errou! Tente um numero maior!")
