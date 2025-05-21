# Contador simples
contador = 1
while contador <= 5:
    print(f"Iteração {contador}")
    contador += 1  # Incrementa o contador

# Acumulador para soma
total = 0
contador = 1
while contador <= 100:
    total += contador  # Acumula valores
    contador += 1
print(f"A soma dos números de 1 a 100 é: {total}")