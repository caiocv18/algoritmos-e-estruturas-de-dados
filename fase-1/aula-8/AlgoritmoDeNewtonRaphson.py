# Algoritmo de Newton-Raphson para encontrar raiz quadrada
def raiz_quadrada(n, precisao=0.0001):
    """Calcula a raiz quadrada de n usando o método de Newton-Raphson."""
    if n < 0:
        raise ValueError("Não é possível calcular raiz quadrada de número negativo")
    
    # Palpite inicial
    x = n / 2 if n > 1 else n
    
    # Iterações
    iteracoes = 0
    while True:
        iteracoes += 1
        
        # Fórmula de Newton-Raphson para raiz quadrada
        x_novo = 0.5 * (x + n / x)
        
        # Verificar convergência
        if abs(x_novo - x) < precisao:
            break
        
        x = x_novo
    
    print(f"Convergiu em {iteracoes} iterações")
    return x

# Testando a função
numero = float(input("Digite um número para calcular a raiz quadrada: "))
raiz = raiz_quadrada(numero)
print(f"A raiz quadrada de {numero} é aproximadamente {raiz:.6f}")
print(f"Para comparação, math.sqrt({numero}) = {__import__('math').sqrt(numero):.6f}")