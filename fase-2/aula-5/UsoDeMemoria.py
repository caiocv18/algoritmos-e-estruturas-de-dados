import sys

# Comparando uso de memória
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tupla_numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print(f"Tamanho da lista: {sys.getsizeof(lista_numeros)} bytes")
print(f"Tamanho da tupla: {sys.getsizeof(tupla_numeros)} bytes")
print(f"Economia: {sys.getsizeof(lista_numeros) - sys.getsizeof(tupla_numeros)} bytes")

# Comparando com diferentes tamanhos
tamanhos = [10, 100, 1000, 10000]
for n in tamanhos:
    lista = list(range(n))
    tupla = tuple(range(n))
    economia = sys.getsizeof(lista) - sys.getsizeof(tupla)
    percentual = (economia / sys.getsizeof(lista)) * 100
    print(f"\nPara {n} elementos:")
    print(f"Lista: {sys.getsizeof(lista)} bytes")
    print(f"Tupla: {sys.getsizeof(tupla)} bytes")
    print(f"Economia: {economia} bytes ({percentual:.1f}%)")
