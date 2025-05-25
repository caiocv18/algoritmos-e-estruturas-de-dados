# Criando uma matriz 3x3
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Acessando elementos
print(matriz[0][0])  # 1
print(matriz[1][2])  # 6

# Iterando sobre matriz
for linha in matriz:
    for elemento in linha:
        print(elemento, end=" ")
    print()  # Nova linha

# Transposta de uma matriz
transposta = [[matriz[j][i] for j in range(len(matriz))]
              for i in range(len(matriz[0]))]
print(transposta)  # [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

# Soma de matrizes
matriz1 = [[1, 2], [3, 4]]
matriz2 = [[5, 6], [7, 8]]
soma = [[matriz1[i][j] + matriz2[i][j]
         for j in range(len(matriz1[0]))]
         for i in range(len(matriz1))]
print(soma)  # [[6, 8], [10, 12]]