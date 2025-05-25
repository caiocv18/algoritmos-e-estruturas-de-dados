# Concatenação com +
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista_completa = lista1 + lista2
print(lista_completa)  # [1, 2, 3, 4, 5, 6]

# Repetição com *
padrao = [0, 1]
repetido = padrao * 3
print(repetido)  # [0, 1, 0, 1, 0, 1]

# Criando matriz inicializada
linha = [0] * 5
matriz = [linha[:] for _ in range(3)]  # Cuidado com referências!
print(matriz)  # [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]