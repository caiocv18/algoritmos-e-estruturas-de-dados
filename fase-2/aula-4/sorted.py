original = [3, 1, 4, 1, 5, 9, 2, 6]
ordenada = sorted(original)
print(original)  # [3, 1, 4, 1, 5, 9, 2, 6] (não modificada)
print(ordenada)  # [1, 1, 2, 3, 4, 5, 6, 9]

# Com parâmetros personalizados
pessoas = [("Ana", 25), ("Bruno", 30), ("Carlos", 22)]
por_idade = sorted(pessoas, key=lambda x: x[1])
print(por_idade)  # [('Carlos', 22), ('Ana', 25), ('Bruno', 30)]