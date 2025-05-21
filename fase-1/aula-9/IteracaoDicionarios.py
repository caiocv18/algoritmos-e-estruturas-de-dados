aluno = {
    "nome": "Ana Silva",
    "idade": 21,
    "curso": "Ciência da Computação",
    "semestre": 4
}

# Iteração nas chaves (padrão)
for chave in aluno:
    print(chave)

# Iteração explícita nas chaves
for chave in aluno.keys():
    print(chave)

# Iteração nos valores
for valor in aluno.values():
    print(valor)

# Iteração em pares chave-valor
for chave, valor in aluno.items():
    print(f"{chave}: {valor}")