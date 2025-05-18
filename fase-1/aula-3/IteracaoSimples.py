# Iteração básica com for
numeros = [1, 2, 3, 4, 5]
for numero in numeros:
    print(numero, end=" ")# 1 2 3 4 5# Iteração com índices
for i in range(len(numeros)):
    print(f"Índice {i}: {numeros[i]}")

# Iteração com enumerate (obtém índice e valor)
for indice, valor in enumerate(numeros):
    print(f"Posição {indice}: {valor}")

# Iteração simultânea de múltiplas listas com zip
nomes = ["Ana", "Bruno", "Carla"]
idades = [25, 30, 22]
for nome, idade in zip(nomes, idades):
    print(f"{nome} tem {idade} anos")