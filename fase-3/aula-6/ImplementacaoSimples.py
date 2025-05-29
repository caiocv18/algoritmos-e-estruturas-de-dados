def percurso_em_ordem(no_atual):
    if no_atual is not None: # Condição de parada da recursão
        percurso_em_ordem(no_atual.esquerda) # 1. Vai para a esquerda
        print(no_atual.valor, end=" ")       # 2. Visita o nó (imprime o valor)
        percurso_em_ordem(no_atual.direita)  # 3. Vai para a direita

# Usando a árvore que criamos antes:
#       10
#      /  \
#     5    15
#    / \    \
#   3   7    20

print("Percurso Em-ordem:")
percurso_em_ordem(raiz) # Saída esperada: 3 5 7 10 15 20
print("\n")
# Se fizermos o pré-ordem, a saída seria: 10 5 3 7 15 20
# Se fizermos o pós-ordem, a saída seria: 3 7 5 20 15 10