# Desempacotamento básico
ponto = (3, 4)
x, y = ponto
print(f"x = {x}, y = {y}")

# Desempacotamento com mais elementos
data = (2024, 11, 25, "Segunda-feira")
ano, mes, dia, dia_semana = data
print(f"{dia}/{mes}/{ano} - {dia_semana}")

# Desempacotamento com asterisco (*)
numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
primeiro, *meio, ultimo = numeros
print(f"Primeiro: {primeiro}, Meio: {meio}, Último: {ultimo}")

# Ignorando valores com underscore
coordenada_3d = (10, 20, 30)
x, y, _ = coordenada_3d  # Ignoramos z
print(f"Apenas x e y: ({x}, {y})")

# Desempacotamento em loops
pontos = [(1, 2), (3, 4), (5, 6), (7, 8)]
for x, y in pontos:
    print(f"Ponto: ({x}, {y}), Distância da origem: {(x**2 + y**2)**0.5:.2f}")

# Troca de variáveis elegante
a = 10
b = 20
print(f"Antes: a = {a}, b = {b}")
a, b = b, a  # Isso cria uma tupla temporária!
print(f"Depois: a = {a}, b = {b}")
