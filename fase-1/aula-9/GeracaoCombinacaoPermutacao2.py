import itertools

# Todas as permutações de ['A', 'B', 'C']
for perm in itertools.permutations(["A", "B", "C"]):
    print(perm)

# Todas as combinações de 2 elementos de [1, 2, 3, 4]
for comb in itertools.combinations([1, 2, 3, 4], 2):
    print(comb)

# Produto cartesiano de ['a', 'b'] e [1, 2]
for prod in itertools.product(["a", "b"], [1, 2]):
    print(prod)