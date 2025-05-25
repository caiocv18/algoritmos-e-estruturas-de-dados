# Criando um dicionário de quadrados
quadrados = {x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Filtrando itens
pares = {k: v for k, v in quadrados.items() if v % 2 == 0}
