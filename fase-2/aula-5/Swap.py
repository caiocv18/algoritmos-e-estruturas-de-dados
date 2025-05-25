# Swap tradicional (outras linguagens)
# temp = a
# a = b
# b = temp

# Swap Pythônico usando tuplas
a, b = 10, 20
print(f"Antes: a = {a}, b = {b}")
a, b = b, a  # Cria tupla (b, a) e desempacota
print(f"Depois: a = {a}, b = {b}")

# Swap múltiplo
x, y, z = 1, 2, 3
x, y, z = z, x, y  # Rotação circular
print(f"Após rotação: x = {x}, y = {y}, z = {z}")

# Swap condicional
def ordenar_dois_numeros(a, b):
    """Retorna os números em ordem crescente"""
    return (a, b) if a <= b else (b, a)

menor, maior = ordenar_dois_numeros(15, 7)
print(f"Ordenados: {menor}, {maior}")

# Swap em lista usando tuplas
lista = [1, 2, 3, 4, 5]
lista[0], lista[4] = lista[4], lista[0]
print(f"Lista após swap: {lista}")  # [5, 2, 3, 4, 1]

# Aplicação prática: Bubble Sort simplificado
def bubble_sort_com_tuplas(lista):
    """Bubble sort usando swap com tuplas"""
    lista = lista.copy()  # Não modifica original
    n = len(lista)

    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                # Swap elegante
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return lista

numeros = [64, 34, 25, 12, 22, 11, 90]
ordenados = bubble_sort_com_tuplas(numeros)
print(f"Original: {numeros}")
print(f"Ordenado: {ordenados}")
