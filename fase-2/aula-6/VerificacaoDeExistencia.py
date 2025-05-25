# Criando um dicionário para exemplo
produto = {"nome": "Notebook", "preco": 3000, "estoque": 5}

# Verificando se uma chave existe
if "nome" in produto:
    print("Produto tem nome")

# Verificando se um valor existe
if 3000 in produto.values():
    print("Existe um produto com esse preço")
