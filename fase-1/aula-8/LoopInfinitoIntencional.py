import random

numero_secreto = random.randint(1, 100)
tentativas = 0

print("Jogo da Adivinhação: Tente adivinhar o número entre 1 e 100!")

while True:
    tentativas += 1
    try:
        palpite = int(input("Seu palpite: "))
        
        if palpite < 1 or palpite > 100:
            print("Por favor, digite um número entre 1 e 100.")
            continue
        
        if palpite < numero_secreto:
            print("Muito baixo! Tente um número maior.")
        elif palpite > numero_secreto:
            print("Muito alto! Tente um número menor.")
        else:
            print(f"Parabéns! Você acertou em {tentativas} tentativas!")
            break
            
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")