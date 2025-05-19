def fibonacci(n):
    """
    Gera e exibe os N primeiros termos da sequência de Fibonacci.

    Args:
        n: Número de termos a serem gerados
    """
    # Verificação de entrada
    if n <= 0:
        print("O número de termos deve ser positivo.")
        return

    # Inicialização
    termo1, termo2 = 0, 1

    # Caso especial para n=1
    if n == 1:
        print(termo1)
        return

    # Para n >= 2, mostramos os dois primeiros termos
    print(termo1)
    print(termo2)

    # Geramos os termos restantes
    for i in range(3, n + 1):
        proximo_termo = termo1 + termo2
        print(proximo_termo)

        # Atualização para o próximo ciclo
        termo1, termo2 = termo2, proximo_termo

# Execução da função
num_termos = int(input("Digite o número de termos da sequência de Fibonacci: "))
fibonacci(num_termos)
