import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 10)
    tentativas = 3

    print("Adivinhe o número entre 1 e 10")

    while tentativas > 0:
        palpite = int(input("Digite seu palpite: "))

        if palpite == numero_secreto:
            print("Parabéns! Você acertou.")
            return
        else:
            tentativas -= 1
            print(f"Errado! Tentativas restantes: {tentativas}")

    print(f"Fim de jogo. O número era {numero_secreto}")

jogo_adivinhacao()
