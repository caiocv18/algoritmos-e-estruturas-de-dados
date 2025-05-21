# Calcular quantos números da sequência de Fibonacci são menores que 1000
a, b = 0, 1
count = 0
while a < 1000:
    print(a, end=" ")
    a, b = b, a + b
    count += 1
print(f"\nExistem {count} números de Fibonacci menores que 1000")