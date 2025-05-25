numeros = [1, 2, 3]
numeros.append(4)
print(numeros)  # [1, 2, 3, 4]

# Cuidado: append adiciona o objeto como um único elemento
numeros.append([5, 6])
print(numeros)  # [1, 2, 3, 4, [5, 6]]