# Suponha uma matriz (lista de listas) de n x n elementos
contador = 0
for i in range(n): # Loop externo executa n vezes
  for j in range(n): # Loop interno executa n vezes PARA CADA execução do externo
    contador = contador + 1 # 2 ops DENTRO do loop mais interno
                            # Total aqui: n * n * 2 operações
# Total aproximado: 2n² operações.