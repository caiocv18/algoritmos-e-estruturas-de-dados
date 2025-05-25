# Acesso direto pode gerar erro
# print(produto["desconto"])  # KeyError!

# Acesso seguro com get()
desconto = produto.get("desconto", 0)  # Retorna 0 se não existir
