# Matriz 3x3
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Imprimindo a matriz formatada
for linha in matriz:
    for elemento in linha:
        print(f"{elemento:3}", end="")
    print()  # Nova linha após cada linha da matriz

# Calculando a soma de todos os elementos
soma = 0
for linha in matriz:
    for elemento in linha:
        soma += elemento
print(f"Soma: {soma}")