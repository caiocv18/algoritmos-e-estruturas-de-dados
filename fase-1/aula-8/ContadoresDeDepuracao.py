numeros = [15, 8, 3, 12, 6, 20, 1]
positivos = 0
negativos = 0
pares = 0
impares = 0
grandes = 0  # > 10

for num in numeros:
    if num > 0:
        positivos += 1
    else:
        negativos += 1
    
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    
    if num > 10:
        grandes += 1

print(f"Positivos: {positivos}, Negativos: {negativos}")
print(f"Pares: {pares}, Ímpares: {impares}")
print(f"Números > 10: {grandes}")