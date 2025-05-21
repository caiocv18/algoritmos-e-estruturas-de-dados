# Geração de um padrão de asteriscos (triângulo)
linhas = 5
i = 1

while i <= linhas:
    # Loop interno para imprimir asteriscos
    j = 1
    while j <= i:
        print("*", end=" ")
        j += 1
    
    # Nova linha após cada linha de asteriscos
    print()
    i += 1

# Geração de uma matriz de multiplicação
tamanho = 5
i = 1

print("\nTabela de multiplicação:")
while i <= tamanho:
    j = 1
    while j <= tamanho:
        produto = i * j
        print(f"{produto:3d}", end=" ")
        j += 1
    print()
    i += 1