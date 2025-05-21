# Processar uma lista até encontrar um valor negativo
dados = [5, 8, 13, 21, -3, 8, 13]
indice = 0
soma = 0

while indice < len(dados) and dados[indice] >= 0:
    soma += dados[indice]
    indice += 1

print(f"Soma dos valores positivos: {soma}")
print(f"Primeiro valor negativo na posição: {indice if indice < len(dados) else 'Não encontrado'}")