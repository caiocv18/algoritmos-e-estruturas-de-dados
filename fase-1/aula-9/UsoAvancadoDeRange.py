# range(fim) - de 0 até fim-1
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# range(início, fim) - de início até fim-1
for i in range(5, 10):
    print(i)  # 5, 6, 7, 8, 9

# range(início, fim, passo) - de início até fim-1, saltando passo
for i in range(0, 10, 2):
    print(i)  # 0, 2, 4, 6, 8

# range com passo negativo - contagem regressiva
for i in range(10, 0, -1):
    print(i)  # 10, 9, 8, 7, 6, 5, 4, 3, 2, 1