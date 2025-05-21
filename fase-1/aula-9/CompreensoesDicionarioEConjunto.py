# Compreensão de dicionário
# {chave: valor for item in iterável}
quadrados = {n: n**2 for n in range(1, 6)}
print(quadrados)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Compreensão de conjunto (set)
# {expressão for item in iterável}
vogais_texto = {char for char in "Algoritmos e Estruturas de Dados" if char.lower() in "aeiou"}
print(vogais_texto)  # {'a', 'e', 'i', 'o', 'u'}