# Concatenação de tuplas
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
tupla3 = tupla1 + tupla2
print(f"Concatenação: {tupla3}")  # (1, 2, 3, 4, 5, 6)

# Repetição de tuplas
tupla_repetida = (0, 1) * 4
print(f"Repetição: {tupla_repetida}")  # (0, 1, 0, 1, 0, 1, 0, 1)

# Construindo tuplas incrementalmente (não eficiente para muitos elementos)
tupla_acumulada = ()
for i in range(5):
    tupla_acumulada += (i,)  # Cria nova tupla a cada iteração
print(f"Tupla acumulada: {tupla_acumulada}")

# Forma mais eficiente: criar lista e converter
elementos = []
for i in range(5):
    elementos.append(i)
tupla_eficiente = tuple(elementos)
print(f"Tupla eficiente: {tupla_eficiente}")
