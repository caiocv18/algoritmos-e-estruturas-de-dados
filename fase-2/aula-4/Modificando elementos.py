# Modificando um único elemento
cores = ["vermelho", "verde", "azul"]
cores[1] = "amarelo"
print(cores)  # ["vermelho", "amarelo", "azul"]

# Modificando múltiplos elementos com slicing
numeros = [1, 2, 3, 4, 5, 6, 7, 8]
numeros[2:5] = [30, 40, 50]
print(numeros)  # [1, 2, 30, 40, 50, 6, 7, 8]

# Substituindo com tamanho diferente
letras = ['a', 'b', 'c', 'd', 'e']
letras[1:4] = ['X', 'Y']
print(letras)  # ['a', 'X', 'Y', 'e']