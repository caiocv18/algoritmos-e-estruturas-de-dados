# Criando os nós
raiz = No(10)
raiz.esquerda = No(5)
raiz.direita = No(15)

raiz.esquerda.esquerda = No(3)
raiz.esquerda.direita = No(7)
raiz.direita.direita = No(20)

# Nossa árvore agora se parece com:
#       10
#      /  \
#     5    15
#    / \    \
#   3   7    20