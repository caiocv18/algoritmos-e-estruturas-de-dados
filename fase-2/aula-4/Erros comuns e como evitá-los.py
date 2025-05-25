# Erro 1: Modificar lista durante iteração
numeros = [1, 2, 3, 4, 5]

# ERRADO:
for num in numeros:
    if num % 2 == 0:
        numeros.remove(num)  # Pode pular elementos!

# CORRETO:
numeros = [num for num in numeros if num % 2 != 0]
# ou
numeros[:] = [num for num in numeros if num % 2 != 0]

# Erro 2: Referências compartilhadas
# ERRADO:
matriz = [[0] * 3] * 3  # Todas as linhas apontam para a mesma lista!
matriz[0][0] = 1
print(matriz)  # [[1, 0, 0], [1, 0, 0], [1, 0, 0]]

# CORRETO:
matriz = [[0] * 3 for _ in range(3)]
matriz[0][0] = 1
print(matriz)  # [[1, 0, 0], [0, 0, 0], [0, 0, 0]]

# Erro 3: IndexError
lista = [1, 2, 3]

# ERRADO:
# print(lista[3])  # IndexError

# CORRETO:
if len(lista) > 3:
    print(lista[3])
else:
    print("Índice fora do alcance")

# Erro 4: Assumir ordem após operações
numeros = [3, 1, 4, 1, 5]
numeros_ordenados = numeros.sort()  # sort() retorna None!

# CORRETO:
numeros.sort()  # Modifica in-place
# ou
numeros_ordenados = sorted(numeros)  # Retorna nova lista
