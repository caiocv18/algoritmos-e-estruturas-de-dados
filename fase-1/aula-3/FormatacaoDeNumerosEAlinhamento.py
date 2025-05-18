# Formatação de números
pi = 3.14159265359
print(f"Pi arredondado: {pi:.2f}") # 3.14
# Alinhamento e espaçamento
print(f"{'Esquerda':<10}|{'Centro':^10}|{'Direita':>10}")
# Saída: "Esquerda   |  Centro  |    Direita"
# Formatação de números inteiros
print(f"Decimal: {42:d}, Binário: {42:b}, Octal: {42:o}, Hex: {42:x}")