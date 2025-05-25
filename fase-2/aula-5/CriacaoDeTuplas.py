# Criação com parênteses (mais comum e clara)
tupla1 = (1, 2, 3, 4, 5)

# Criação sem parênteses (packing)
tupla2 = 1, 2, 3, 4, 5

# Ambas criam o mesmo objeto
print(tupla1 == tupla2)  # True

# Criação a partir de um iterável
tupla3 = tuple([1, 2, 3, 4, 5])
tupla4 = tuple("Python")  # ('P', 'y', 't', 'h', 'o', 'n')
tupla5 = tuple(range(5))  # (0, 1, 2, 3, 4)

# Tuplas podem conter diferentes tipos
tupla_mista = (1, "Python", 3.14, True, [1, 2, 3])
print(f"Tupla mista: {tupla_mista}")
