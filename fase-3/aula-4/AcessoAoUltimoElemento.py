# Criando uma "pilha" usando uma lista
pilha_de_livros = []

# Empilhando livros (push)
pilha_de_livros.append("O Senhor dos Anéis")
pilha_de_livros.append("Harry Potter")
pilha_de_livros.append("Crônicas de Nárnia")
print(f"Pilha atual: {pilha_de_livros}")

# Espiando o topo (peek)
if pilha_de_livros: # Verifica se não está vazia
    print(f"Livro no topo: {pilha_de_livros[-1]}")

# Desempilhando um livro (pop)
if pilha_de_livros:
    livro_retirado = pilha_de_livros.pop()
    print(f"Livro retirado: {livro_retirado}")
print(f"Pilha após pop: {pilha_de_livros}")

# Verificando se está vazia (isEmpty)
if not pilha_de_livros: # ou if len(pilha_de_livros) == 0:
    print("A pilha de livros está vazia.")