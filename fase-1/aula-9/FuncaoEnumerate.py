frutas = ["maçã", "banana", "laranja", "abacaxi"]

# Sem enumerate (menos elegante)
for i in range(len(frutas)):
    print(f"{i+1}. {frutas[i]}")

# Com enumerate (mais pythônico)
for i, fruta in enumerate(frutas, 1):  # O segundo parâmetro define o valor inicial
    print(f"{i}. {fruta}")