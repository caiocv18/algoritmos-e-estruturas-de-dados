# Sintaxe básica: [expressão for item in iterável]
quadrados = [x**2 for x in range(10)]
print(quadrados)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Com condição
pares = [x for x in range(20) if x % 2 == 0]
print(pares)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# Transformação de strings
palavras = ["python", "java", "javascript"]
maiusculas = [palavra.upper() for palavra in palavras]
print(maiusculas)  # ['PYTHON', 'JAVA', 'JAVASCRIPT']

# Comprehensions aninhadas
matriz = [[i+j for j in range(3)] for i in range(3)]
print(matriz)  # [[0, 1, 2], [1, 2, 3], [2, 3, 4]]

# Com múltiplas condições
numeros = [x for x in range(100) if x % 3 == 0 if x % 5 == 0]
print(numeros)  # [0, 15, 30, 45, 60, 75, 90]
