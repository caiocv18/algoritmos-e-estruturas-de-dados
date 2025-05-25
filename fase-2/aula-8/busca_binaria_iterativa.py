def busca_binaria_iterativa(lista, chave):
  """
  Realiza uma busca binária iterativa em uma lista ORDENADA.
  Retorna o índice do elemento se encontrado, ou None caso contrário.
  """
  inicio = 0
  fim = len(lista) - 1

  while inicio <= fim:
    meio = (inicio + fim) // 2 # Divisão inteira para obter o índice

    if lista[meio] == chave:
      return meio # Encontrou!
    elif lista[meio] < chave:
      inicio = meio + 1 # Chave está na metade direita
    else: # lista[meio] > chave
      fim = meio - 1   # Chave está na metade esquerda

  return None # Não encontrou

# Exemplo de uso
numeros_ordenados = [2, 5, 7, 8, 11, 12, 23, 38, 56, 72, 91]
chave_procurada = 23

posicao = busca_binaria_iterativa(numeros_ordenados, chave_procurada)

if posicao is not None:
  print(f"Elemento {chave_procurada} encontrado na posição {posicao}.")
else:
  print(f"Elemento {chave_procurada} não encontrado na lista.")

chave_procurada = 40
posicao = busca_binaria_iterativa(numeros_ordenados, chave_procurada)

if posicao is not None:
  print(f"Elemento {chave_procurada} encontrado na posição {posicao}.")
else:
  print(f"Elemento {chave_procurada} não encontrado na lista.")

