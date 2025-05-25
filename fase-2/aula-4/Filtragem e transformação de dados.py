# Filtragem tradicional
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = []
for num in numeros:
    if num % 2 == 0:
        pares.append(num)

# Usando filter()
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # [2, 4, 6, 8, 10]

# Transformação com map()
celsius = [0, 20, 30, 40]
fahrenheit = list(map(lambda c: c * 9/5 + 32, celsius))
print(fahrenheit)  # [32.0, 68.0, 86.0, 104.0]

# Combinando filter e map
# Quadrados dos números pares
resultado = list(map(lambda x: x**2,
                    filter(lambda x: x % 2 == 0, numeros)))
print(resultado)  # [4, 16, 36, 64, 100]