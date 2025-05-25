# Tuplas podem ser usadas como chaves de dicionário
coordenadas_cidades = {
    (-23.550520, -46.633308): "São Paulo",
    (-22.906847, -43.172897): "Rio de Janeiro",
    (-15.794229, -47.882166): "Brasília"
}

# Listas NÃO podem ser usadas como chaves
try:
    coords_erro = {
        [-23.550520, -46.633308]: "São Paulo"  # Erro!
    }
except TypeError as e:
    print(f"Erro com lista como chave: {e}")

# Criando um cache usando tuplas como chaves
cache_fibonacci = {}

def fibonacci_cached(n, a=0, b=1):
    """Fibonacci com cache usando tupla como chave"""
    chave = (n, a, b)

    if chave in cache_fibonacci:
        return cache_fibonacci[chave]

    if n == 0:
        resultado = a
    elif n == 1:
        resultado = b
    else:
        resultado = fibonacci_cached(n-1, b, a+b)

    cache_fibonacci[chave] = resultado
    return resultado

# Testando
for i in range(10):
    print(f"Fib({i}) = {fibonacci_cached(i)}")

# Tuplas em sets (conjuntos)
pontos_unicos = {(1, 2), (3, 4), (1, 2), (5, 6)}
print(f"Pontos únicos: {pontos_unicos}")  # {(1, 2), (3, 4), (5, 6)}
