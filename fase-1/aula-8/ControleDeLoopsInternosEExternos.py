import random

# Jogo de adivinhar: três tentativas para cada número
total_numeros = 3
acertos = 0
i = 1

while i <= total_numeros:
    numero_secreto = random.randint(1, 10)
    print(f"\nRodada {i}: Tente adivinhar o número entre 1 e 10!")
    
    tentativas = 1
    max_tentativas = 3
    acertou = False
    
    while tentativas <= max_tentativas and not acertou:
        try:
            palpite = int(input(f"Tentativa {tentativas}/{max_tentativas}: "))
            
            if palpite == numero_secreto:
                print(f"Parabéns! Você acertou o número {numero_secreto}!")
                acertos += 1
                acertou = True
            else:
                dica = "maior" if palpite < numero_secreto else "menor"
                print(f"Errou! O número secreto é {dica} que {palpite}.")
                tentativas += 1
        
        except ValueError:
            print("Por favor, digite um número válido.")
    
    if not acertou:
        print(f"Suas tentativas acabaram. O número era {numero_secreto}.")
    
    i += 1

print(f"\nJogo encerrado. Você acertou {acertos} de {total_numeros} números.")