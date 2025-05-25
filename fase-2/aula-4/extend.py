lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista1.extend(lista2)
print(lista1)  # [1, 2, 3, 4, 5, 6]

# Diferença entre extend e append
lista3 = [1, 2, 3]
lista3.extend([4, 5])
print(lista3)  # [1, 2, 3, 4, 5]