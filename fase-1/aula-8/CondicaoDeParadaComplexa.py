# Algoritmo iterativo até convergência
x = valor_inicial
tolerancia = 0.0001
while abs(x * x - numero) > tolerancia:
    x = (x + numero/x) / 2