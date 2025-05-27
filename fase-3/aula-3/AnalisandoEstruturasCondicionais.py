# n = tamanho da lista
# Pior caso: a condição do if nunca é verdadeira, ou sempre é.
# O bloco dentro do if/else é O(1).
for item in lista: # O(n)
  if condicao_qualquer(item): # O(1) para avaliar a condição
    # faz algo O(1)
    pass
  else:
    # faz outra coisa O(1)
    pass
# Complexidade total: O(n) * O(1) = O(n)