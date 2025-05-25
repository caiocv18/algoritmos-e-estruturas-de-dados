# Criando uma tupla para demonstração
coordenadas = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)

# Acesso por índice positivo
primeiro = coordenadas[0]  # 10
quinto = coordenadas[4]  # 50

# Acesso por índice negativo
ultimo = coordenadas[-1]  # 100
penultimo = coordenadas[-2]  # 90

# Fatiamento básico
primeiros_tres = coordenadas[:3]  # (10, 20, 30)
ultimos_tres = coordenadas[-3:]  # (80, 90, 100)
meio = coordenadas[3:7]  # (40, 50, 60, 70)

# Fatiamento com passo
pares = coordenadas[::2]  # (10, 30, 50, 70, 90)
impares = coordenadas[1::2]  # (20, 40, 60, 80, 100)
reverso = coordenadas[::-1]  # (100, 90, 80, ..., 20, 10)

print(f"Primeiros três: {primeiros_tres}")
print(f"Elementos pares (índices): {pares}")
print(f"Tupla reversa: {reverso}")

# Verificando se elemento existe
if 50 in coordenadas:
    print(f"50 está na posição {coordenadas.index(50)}")
