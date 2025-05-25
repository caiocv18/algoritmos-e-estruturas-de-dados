# Ordenação básica
numeros = [3, 1, 4, 1, 5, 9, 2, 6]
numeros.sort()
print(numeros)  # [1, 1, 2, 3, 4, 5, 6, 9]

# Ordenação reversa
numeros.sort(reverse=True)
print(numeros)  # [9, 6, 5, 4, 3, 2, 1, 1]

# Ordenação com chave personalizada
palavras = ["Python", "Java", "C", "JavaScript"]
palavras.sort(key=len)  # Ordena por comprimento
print(palavras)  # ['C', 'Java', 'Python', 'JavaScript']