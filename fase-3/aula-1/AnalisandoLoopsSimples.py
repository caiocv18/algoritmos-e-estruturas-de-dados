# Suponha uma lista com 'n' elementos
minha_lista = [1, 2, 3, ..., n]
soma_elementos = 0              # 1 operação

for elemento in minha_lista:    # Este loop executa 'n' vezes
  soma_elementos = soma_elementos + elemento # 2 ops (adição, atribuição) DENTRO do loop
                                            # Total dentro do loop: n * 2 operações

print(soma_elementos)           # 1 operação
# Total aproximado: 1 (antes) + 2*n (no loop) + 1 (depois) = 2n + 2 operações.
