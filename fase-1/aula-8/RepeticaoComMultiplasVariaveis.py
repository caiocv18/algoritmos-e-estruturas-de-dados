# Encontra o primeiro par de números consecutivos cuja soma dos quadrados é um quadrado perfeito
a, b = 1, 2
limite = 100  # Para evitar loops muito longos

print("Buscando pares de números consecutivos (a,b) onde a²+b² é um quadrado perfeito...")

while a < limite:
    soma_quadrados = a**2 + b**2
    raiz = soma_quadrados ** 0.5
    
    if raiz.is_integer():  # Verifica se é um quadrado perfeito
        c = int(raiz)
        print(f"Encontrado: {a}² + {b}² = {soma_quadrados} = {c}²")
        print(f"({a},{b}) é o primeiro par com esta propriedade.")
        break
    
    # Incrementa ambas as variáveis para manter consecutivos
    a += 1
    b += 1
else:
    print(f"Nenhum par encontrado dentro do limite de {limite}.")