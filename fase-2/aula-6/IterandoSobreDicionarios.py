# Criando um dicionário para exemplo
aluno = {"nome": "Pedro", "nota1": 8.5, "nota2": 9.0}

# Iterando sobre chaves (padrão)
for chave in aluno:
    print(chave)

# Iterando sobre valores
for valor in aluno.values():
    print(valor)

# Iterando sobre pares chave-valor
for chave, valor in aluno.items():
    print(f"{chave}: {valor}")
