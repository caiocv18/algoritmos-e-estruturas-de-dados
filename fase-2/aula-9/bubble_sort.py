def bubble_sort(lista):
  n = len(lista)
  # Loop para controlar as passadas pela lista
  for i in range(n - 1):
    # Loop para comparar os elementos adjacentes
    # A cada passada, o maior elemento "flutua" para o final
    # Por isso, o range do loop interno diminui (n - 1 - i)
    for j in range(n - 1 - i):
      if lista[j] > lista[j+1]:
        # Troca os elementos de lugar
        lista[j], lista[j+1] = lista[j+1], lista[j]
  return lista

# Exemplo de uso
numeros = [5, 1, 4, 2, 8]
print(f"Lista original: {numeros}")
numeros_ordenados = bubble_sort(numeros.copy()) # Usamos .copy() para não alterar a original
print(f"Lista ordenada com Bubble Sort: {numeros_ordenados}")