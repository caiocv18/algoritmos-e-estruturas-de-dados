# Sintaxe: [expressão for item in iterável if condição]

# Números pares de 1 a 20
pares = [n for n in range(1, 21) if n % 2 == 0]
print(pares)  # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Palavras com mais de 5 letras
palavras = ["casa", "computador", "dados", "algoritmo", "python"]
palavras_longas = [palavra for palavra in palavras if len(palavra) > 5]
print(palavras_longas)  # ['computador', 'algoritmo', 'python']