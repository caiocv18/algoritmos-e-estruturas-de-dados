# Fórmula simples: área de um círculo
import math
raio = float(input("Digite o raio do círculo: "))
area = math.pi * raio ** 2
print(f"Área do círculo: {area:.2f}")

# Fórmula mais complexa: equação do segundo grau
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

# Cálculo do discriminante
delta = b ** 2 - 4 * a * c

if delta < 0:
    print("Esta equação não possui raízes reais.")
elif delta == 0:
    x = -b / (2 * a)
    print(f"Esta equação possui uma raiz real: x = {x:.2f}")
else:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print(f"Esta equação possui duas raízes reais: x1 = {x1:.2f} e x2 = {x2:.2f}")