import time

# Comparação de métodos de adição
def teste_append(n):
    start = time.time()
    lista = []
    for i in range(n):
        lista.append(i)
    return time.time() - start

def teste_comprehension(n):
    start = time.time()
    lista = [i for i in range(n)]
    return time.time() - start

def teste_extend(n):
    start = time.time()
    lista = []
    lista.extend(range(n))
    return time.time() - start

# Teste com 1 milhão de elementos
n = 1_000_000
print(f"append: {teste_append(n):.4f}s")
print(f"comprehension: {teste_comprehension(n):.4f}s")
print(f"extend: {teste_extend(n):.4f}s")

# Dicas de otimização:
# 1. Use list comprehension quando possível
# 2. Evite append em loops grandes - considere extend
# 3. Para muitas inserções/remoções no início, use deque
# 4. Para busca frequente, considere set ou dict
