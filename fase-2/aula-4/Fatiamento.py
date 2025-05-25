numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Sintaxe: lista[início:fim:passo]
print(numeros[2:5])  # [2, 3, 4] (índices 2 até 4)
print(numeros[:4])  # [0, 1, 2, 3] (do início até índice 3)
print(numeros[5:])  # [5, 6, 7, 8, 9] (do índice 5 até o fim)
print(numeros[::2])  # [0, 2, 4, 6, 8] (elementos de 2 em 2)
print(numeros[1::2])  # [1, 3, 5, 7, 9] (ímpares)
print(numeros[::-1])  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] (reverso)