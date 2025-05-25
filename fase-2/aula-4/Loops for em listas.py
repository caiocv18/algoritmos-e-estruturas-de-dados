# Iteração simples
frutas = ["maçã", "banana", "laranja"]
for fruta in frutas:
    print(f"Eu gosto de {fruta}")

# Processamento com acumulador
precos = [10.50, 25.00, 35.75, 15.90]
total = 0
for preco in precos:
    total += preco
print(f"Total: R$ {total:.2f}")

# Modificação durante iteração (use com cuidado!)
numeros = [1, 2, 3, 4, 5]
for i in range(len(numeros)):
    numeros[i] = numeros[i] ** 2
print(numeros)# [1, 4, 9, 16, 25]