# Erro comum em loops while: esquecer de incrementar o contador
contador = 0
while contador < 10:
    print(contador)
    # Esqueceu de incrementar! Isso causa um loop infinito
    # contador += 1