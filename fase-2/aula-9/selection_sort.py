def selection_sort(lista):
  n = len(lista)
  # Loop para percorrer cada posição da lista
  for i in range(n - 1):
    # Encontra o índice do menor elemento na parte não ordenada da lista
    indice_menor_atual = i
    for j in range(i + 1, n):
      if lista[j] < lista[indice_menor_atual]:
        indice_menor_atual = j

    # Troca o menor elemento encontrado com o primeiro elemento da parte não ordenada
    if indice_menor_atual != i:
      lista[i], lista[indice_menor_atual] = lista[indice_menor_atual], lista[i]
  return lista

# Exemplo de uso
numeros = [64, 25, 12, 22, 11]
print(f"Lista original: {numeros}")
numeros_ordenados = selection_sort(numeros.copy()) # Usamos .copy() para não alterar a original
print(f"Lista ordenada com Selection Sort: {numeros_ordenados}")